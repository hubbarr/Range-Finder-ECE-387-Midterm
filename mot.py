import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

GPIO.setwarnings(False)
servoPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO_TRIGGER = 25
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance



p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization
try:
    while (True):
        z=3
        while z>0:
            x = 1
            while x < 8: 
                p.ChangeDutyCycle(x)
                dist = distance()
                print ("Measured Distance = %.1f cm" % dist)
                dist = dist * 0.39370
                print ("Measured Distance = %.1f inches" % dist)
                plt.scatter(x, dist)
                time.sleep(.01)
               
                x = x+.1
            y=8
            while y>1:
                p.ChangeDutyCycle(y)
                dist = distance()
                print ("Measured Distance = %.1f cm" % dist)
                dist = dist * 0.39370
                print ("Measured Distance = %.1f inches" % dist)
                time.sleep(.01)
               
                y=y-.1
            z=z-1
        plt.ylim(0,20)
        plt.show()
        

except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()