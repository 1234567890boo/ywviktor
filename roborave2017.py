import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
Rpin1=23
Rpin2=24
Lpin1=25
Lpin2=8
RW=Rpin1,Rpin2
LW=Lpin1,Lpin2
GPIO.setup(Rpin1,GPIO.OUT)
GPIO.setup(Lpin1,GPIO.OUT)
GPIO.setup(Rpin2,GPIO.OUT)
GPIO.setup(Lpin2,GPIO.OUT)
def straight():
    forward()
    time.sleep(1)
    
def forward ():
    GPIO.output(Rpin1,GPIO.HIGH)
    GPIO.output(Lpin1,GPIO.LOW)
    GPIO.output(Rpin2,GPIO.LOW)
    GPIO.output(Lpin2,GPIO.HIGH)
def right():
    GPIO.output(Rpin1,GPIO.HIGH)
    GPIO.output(Lpin1,GPIO.LOW)
    GPIO.output(Rpin2,GPIO.HIGH)
    GPIO.output(Lpin2,GPIO.LOW)
def left():
    GPIO.output(Rpin1,GPIO.LOW)
    GPIO.output(Lpin1,GPIO.HIGH)
    GPIO.output(Rpin2,GPIO.LOW)
    GPIO.output(Lpin2,GPIO.HIGH)
def backward():
    GPIO.output(Rpin1,GPIO.LOW)
    GPIO.output(Lpin1,GPIO.HIGH)
    GPIO.output(Rpin2,GPIO.HIGH)
    GPIO.output(Lpin2,GPIO.LOW)
def stop():
    GPIO.output(Rpin1,GPIO.LOW)
    GPIO.output(Lpin1,GPIO.LOW)
    GPIO.output(Rpin2,GPIO.LOW)
    GPIO.output(Lpin2,GPIO.LOW)
straight()
GPIO.cleanup()
quit()
