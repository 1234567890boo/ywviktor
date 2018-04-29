import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
l1=6
GPIO_TRIGGER=18
GPIO_ECHO=16
GPIO.setup(l1,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)
while True:
    temperature=20
    speedSound=33100+(0.6*temperature)
    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER,False)
    start=time.time()
    while GPIO.input(GPIO_ECHO)==0:
        start=time.time()

    while GPIO.input(GPIO_ECHO)==1:
        stop=time.time()
    elapsed=start-stop
    distance=elapsed*speedSound
    distance=distance/2
    print(distance)
    if distance<-200:
        GPIO.output(l1,1)
    else:
        GPIO.output(l1,0)
        
