import cv2
import zbar
import numpy as np


# conent Webcam
cap = cv2.VideoCapture(0)

# set frame height,width
cap.set(3,320)
cap.set(4,480)

# create a reader
scanner = zbar.ImageScanner()

# configure the reader
scanner.parse_config('enable')	

while(True):
    # ret : frame capture(boolean)
    # frame : Capture frame
    ret, frame = cap.read()

    #convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    
    #calculate x & y gradient
    gradX = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 1, dy = 0, ksize = -1)
    gradY = cv2.Sobel(gray, ddepth = cv2.CV_32F, dx = 0, dy = 1, ksize = -1)

    #substract the y-gradient from the x-gradient 
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    #blur and threshold the image 
    blurred = cv2.blur(gradient, (3,3))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)

    # construct a closing kernel and apply it to the thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # perform a series of erosions and dilations 
    closed = cv2.erode(closed, None, iterations = 4)
    closed = cv2.dilate(closed, None, iterations = 4)

    # find the contours in the thresholded image, then sort the contours
    # by their area, keeping only the largest one
    im2,cnts,hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(cnts) > 0:
        c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    else:
        print "Sorry No contour Found."

    # compute the rotated bounding box of the largest contour
    rect = cv2.minAreaRect(c)
    box = np.int0(cv2.boxPoints(rect))

    # draw a bounding box arounded the detected barcode and display the frame

    cv2.drawContours(frame, [box], -1, (0, 255, 0), 2)
    


    # Find height and width
    height, width = gray.shape

    # Get raw image bytes
    raw = gray.tobytes()

    # Wrap image data in a zbar image  
    image = zbar.Image(width, height, 'Y800', raw)

    # Scan the image for barcodes and QRCodes
    scanner.scan(image)



    # Print results and save data
    for symbol in  image:
        print('Type : ', symbol.type); 
        print('Data :', symbol.data,'\n');
        f=open('test.txt','w')
        f.write(symbol.data)
        f.write('\n')
        f.close()


    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
