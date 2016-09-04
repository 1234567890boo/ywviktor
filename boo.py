'''
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
g=26
y=6
r=19
o=13
b=5
lites=[g,y,r,b,o]
GPIO.setup(lites,GPIO.OUT)
def ike():
    while True:
        GPIO.output(lites,1)
        time.sleep(0.1)
        GPIO.output(lites,0)
        time.sleep(0.1)
    GPIO.cleanup()
ike()
'''
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
g=5
y=6
r=13
o=19
b=26
lites=[g,y,r,o,b]
for n in lites:
    GPIO.setup(n,GPIO.OUT)
    
def ike():
    for n in lites:
        GPIO.output(n,1)
        time.sleep(1)
        GPIO.output(n,0)
        time.sleep(1)
def boo():
    for n in range (0,5,1):
        GPIO.output(lites,1)
        time.sleep(0.1)
        GPIO.output(lites,0)
        stime.sleep(0.1)
while True:
    ike()
    boo()
GPIO.cleanup()
