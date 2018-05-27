import RPi.GPIO as GPIO
import time
import threading

def main():
   s = motor1()
    
   s.start()

   d = motor2()
   d.start()

class motor1(threading.Thread):
        def run(self):

            GPIO.setmode(GPIO.BCM) # GPIO set mode setting (BCM,BOARD)
            
            ControlPin = [16,12,25,18] # Pin Number setting
            
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
            
            # Infinite rotation
            for i in range(512000): 
                for halfstep in range(8):
                        for pin in range(4):
                                GPIO.output(ControlPin[pin], seq[halfstep][pin])
                                
                        time.sleep(0.005) # motor speed
            GPIO.cleanup()
            
class motor2(threading.Thread):
        def run(self):

            GPIO.setmode(GPIO.BCM) # GPIO set mode setting (BCM,BOARD)
            
            ControlPin2 = [5,6,13,26] # Pin Number setting
            
            for pin in ControlPin2:
                GPIO.setup(pin,GPIO.OUT)
                GPIO.output(pin,1)
                
            seq = [ [1,0,0,0],
                    [1,1,0,0],
                    
                    [0,1,0,0],
                    [0,1,1,0],
                    [0,0,1,0],
                    [0,0,1,1],
                    [0,0,0,1],
                    [1,0,0,1] ]

            # Infinite rotation
            for i in range(512000):
                for halfstep in range(8):
                        for pin in range(4):
                                GPIO.output(ControlPin2[pin], seq[halfstep][pin])
                                
                        time.sleep(0.002) # motor speed
            GPIO.cleanup()

if __name__ == '__main__':
    main()
            
            
