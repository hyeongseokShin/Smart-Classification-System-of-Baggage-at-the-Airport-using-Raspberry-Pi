# Smart Classification System of Baggage at the Airport using Raspberry Pi
In this project, We uses reserved data to divide the baggage by seats, It gets the sorted baggage back to the front passengers of airline. Passengers leave their baggage at the airport, their baggage will be gathered in the order that formalities for entry. In this case, when passengers get their baggage back after they arrive at their destination, passengers will have a considerable difficulty finding their baggage at random. Therefore, in this project, we create a system that classifies baggage by seats and their barcodes, and we uses a barcode generator and barcode recognizer. 

# Project Output
## Case A
### Case A-1
#### When we start this machine.
#### ![Case A-1](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20A-1.png)

### Case A-2
#### When a box is moving, this image shows that webcam is processing a barcode. 
#### ![Case A-2](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20A-2.png)

### Case A-3
#### If barcode information and ultrasonic sensor are matched, output represents case(A). 
#### Then a motor will activate.
#### ![Case A-3](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20A-3.png)

## Case B
### Case B-1
#### When a box is moving, this image shows that webcam is processing a barcode.
#### ![Case B-1](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20B-1.png)

### Case B-2
#### If barcode information and ultrasonic sensor are matched, output represents case(A). 
#### Then a motor will activate.
#### ![Case B-2](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20B-2.png)

## Case C
### Case C-1
#### When a box is moving, this image shows that webcam is processing a barcode.
#### ![Case C-1](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20C-1.png)

### Case C-2
#### If barcode information and ultrasonic sensor are matched, output represents case(A). 
#### Then a motor will activate.
#### ![Case C-2](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/Case%20C-2.png)

## The whole images
### The whole image 1 (Diagonal)
#### ![The whole image 1](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/%EC%A0%84%EC%B2%B4%EC%A0%81%20%EC%82%AC%EC%A7%841.jpg)

### The whole image 2 (Side)
#### ![The whole image 2](https://github.com/hyeongseokShin/Smart-Classification-System-of-Baggage-at-the-Airport-using-Raspberry-Pi/blob/master/assets/%EC%A0%84%EC%B2%B4%EC%A0%81%20%EC%82%AC%EC%A7%842.jpg)


# Used Language 
## We used Python language(Opencv 3.3/ Zbar 0.10) and Raspberry Pi OS raspbian(Linux). 
## you can see and use programming code in this project.
## If you want to know more about programming code, you would reference attached files.
## 'barcode Scan and Detect.py' contains informations about barcode scan and detect using Opencv 3.3, Zbar 0.10.
## 'Ultrasonic sensor(HC-SRO 4) and Stepmotor Fusion.py' contains informations about recognize object.
## 'Stepmotor2ps.py' contains information about control two motors.
