import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins=[26,19,13,6]
GPIO.setup(pins,GPIO.OUT)
p1=[(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]
def dg90():
    for i in range(0,125,1):
        for n in p1:
            GPIO.output(pins,n)
            time.sleep(0.002)
def dg180():
    for i in range(0,250,1):
        for n in p1:
            GPIO.output(pins,n)
            time.sleep(0.002)
def dg270():
    for i in range(0,375,1):
        for n in p1:
            GPIO.output(pins,n)
            time.sleep(0.002)
def dg360():
    for i in range(0,500,1):
        for n in p1:
            GPIO.output(pins,n)
            time.sleep(0.002)
while True:
    print('how many degrees? 90,180,270 or 360?')
    Z=int(input())
    if Z==90:
        dg90()
    if Z==180:
        dg180()
    if Z==270:
        dg270()
    if Z==360:
        dg360()
