import RPi.GPIO as GPIO
import time
import sys
import signal
import threading 


GPIO.setmode(GPIO.BCM) # setmode setting(BCM,BOARD)
TRIG = 23  # TRIG
ECHO = 24  # ECHO

                
MAX_DISTANCE_CM = 300
MAX_DURATION_TIMEOUT = (MAX_DISTANCE_CM * 2 * 29.1) #17460us = 300cm



# Press CTRL+C on keyboard to process
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        GPIO.cleanup()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)



# Cm conversion function
def distanceInCm(duration):
    
    return (duration/2)/29.1


# Distance can be adjusted according to the situation.
# if distance < 9.3cm -> The step motor is in motion.
def print_distance(distance):


    # # if distance < 9.3cm -> The step motor is in motion.
    if distance < 9.3:
            
            distanceReal = distance
        

        

            # Check barcode scan results 
            with open("test.txt","r") as file:
                        textm = file.read()
                        arrange = list(textm)
                        time.sleep(1)
       
                        
            barcode = int(arrange[10])*10 + int(arrange[11]) # The 11th and 12th digits in front
            if distanceReal == 0:
                        distanceMsg = 'Distance : out of range                   \r'
            # A case 
            elif (distanceReal < 9.3) and (barcode < 33):
                ControlPin = [4,17,27,22] # Forward rotation
                for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]
                
                # Right angle rotation
                for i in range(32): 
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005)
                print "Barcode number( Case A ) : " + str(barcode) # Output for confirmation
                print ("Distance : " + str(distance) + "cm   \r" )  # Output for confirmation
                time.sleep(8) # Reset wait time
                
                            
                ControlPin = [22,27,17,4] # Reverse rotation

                for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]
                
                # Left angle rotation
                for i in range(32):
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005) # motor speed
                

                distanceReal = 0 # distance reset
             
            # C case               
            elif (distanceReal < 9.3) and (barcode > 66):
                ControlPin = [22,27,17,4] # Reverse rotation
                for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]
                
                # Left angle rotation
                for i in range(32):
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005) # motor speed
                            
                print "Barcode number( Case C ) : " + str(barcode)  # Output for confirmation
                print ("Distance : " + str(distance) + "cm     \r" )  # Output for confirmation
                time.sleep(8) # Reset wait time
                
                ControlPin = [4,17,27,22] # Forward rotation
                for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]
                
                # Right angle rotation
                for i in range(32):
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005)
                            
                # distance reset      
                distanceReal = 0 
           
            # B case
            elif (distanceReal < 9.3) and (barcode < 66) and (barcode > 33):
                 ControlPin = [4,17,27,22] # Forward rotation
                 for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                 seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]
                 # Right half angle rotation
                 for i in range(16):
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005) # motor speed
                 print "Barcode number( Case B ) : " + str(barcode) # Output for confirmation
                 print ("Distance : " + str(distance) + "cm     \r" ) # Output for confirmation
                            
                 ControlPin = [22,27,17,4] # Revers rotation
                 for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                 seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]
                 
                 # Left angle rotation
                 for i in range(32):
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005) # motor speed
                
                          
                 ControlPin = [4,17,27,22]   # Forward rotation 
                 for pin in ControlPin:
                            GPIO.setup(pin,GPIO.OUT)
                            GPIO.output(pin,0)
            
    
                 seq = [ [1,0,0,0],
                                [1,1,0,0],
                                [0,1,0,0],
                                [0,1,1,0],
                                [0,0,1,0],
                                [0,0,1,1],
                                [0,0,0,1],
                                [1,0,0,1] ]

                 
                 # Right half angle rotation
                 for i in range(16):
                    for halfstep in range(8):
                            for pin in range(4):
                                    GPIO.output(ControlPin[pin], seq[halfstep][pin])
                            time.sleep(0.005) # motor speed
                 time.sleep(8) # Reset wait time

                 # distance reset
                 distanceReal = 0
                            
                 #sys.stdout.write(distanceMsg)
                 sys.stdout.flush()
    else:
        print "NOT WORKING" # Output for confirmation
        print ("Distance : " + str(distance) + "cm     \r" ) # Output for confirmation
    
                
           

def main():
   s = motorhc()
   s.start() # motor and HC-SRO4 Start

 
    


class motorhc (threading.Thread):
        def run(self):
            GPIO.setup(TRIG, GPIO.OUT) # TRIG output
            GPIO.setup(ECHO, GPIO.IN)  # ECHO input

            print('To Exit, Press the CTRL+C Keys')
            

            # HC-SR04 Wait a few minutes before starting
            GPIO.output(TRIG, False)
            print('Waiting For Sensor To Ready')
            time.sleep(1) # 1s
            

            # Start
            print('Start!!')
            while True:
                    
                # # Improved communication problem in the middle       
                fail = False
                time.sleep(0.1)


                # Set the trigger high for 10us to low.
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                # Wait until signal is received by ECHO
                timeout = time.time()
                while GPIO.input(ECHO) == 0:

                        
                    # Save start time to variable
                    pulse_start = time.time()
                    if ((pulse_start - timeout)*1000000) >= MAX_DURATION_TIMEOUT:

                        # Improved communication problem in the middle  
                        fail = True
                        break
                        
                # Improved communication problem in the middle         
                if fail:
                    continue

                
                # Wait until end of recognition with ECHO
                timeout = time.time()
                while GPIO.input(ECHO) == 1:

                        
                    # Save to end time variable
                    pulse_end = time.time()
                    if ((pulse_end - pulse_start)*1000000) >= MAX_DURATION_TIMEOUT:
                        print_distance(0) 

                        # Improved communication problem in the middle 
                        fail = True
                        break

                # Improved communication problem in the middle      
                if fail: 
                    continue

                # Distance Recognition Time 
                pulse_duration = (pulse_end - pulse_start) * 1000000

                # Convert time to cm
                distance = distanceInCm(pulse_duration)
                
                # Round digits
                distance = round(distance, 2)
                

                # Motor control with distance
                print_distance(distance)

            GPIO.cleanup()


if __name__ == '__main__':
    main()
