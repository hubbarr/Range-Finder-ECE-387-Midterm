import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

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

while True:
    dist= distance()
    print(dist)
    if (dist > 10):
        GPIO.output(22, False)
    if (dist < 10):
        while(dist < 10):
            print(dist)
            GPIO.output(22, True)
            dist = distance()
        sleep(5)
        GPIO.output(22, False)
        
    
    
    
    
    
    
    