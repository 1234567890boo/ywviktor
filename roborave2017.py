import RPI.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from __future__ import division
import threading
import time
from sr import *
R = Robot()
Rpin1=1
Rpin2=2
Lpin1=3
Lpin2=4
def setup():             
    GPIO.setup(Rpin1,GPIO.OUT)
    GPIO.setup(Lpin1,GPIO.OUT)
    GPIO.setup(Rpin2,GPIO.OUT)
    GPIO.setup(Lpin2,GPIO.OUT)
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
def backword():
    GPIO.output(Rpin1,GPIO.LOW)
    GPIO.output(Lpin1,GPIO.HIGH)
    GPIO.output(Rpin2,GPIO.HIGH)
    GPIO.output(Lpin2,GPIO.LOW)
def stop():
    GPIO.output(Rpin1,GPIO.LOW)
    GPIO.output(Lpin1,GPIO.LOW)
    GPIO.output(Rpin2,GPIO.LOW)
    GPIO.output(Lpin2,GPIO.LOW)
class Encoder(threading.Thread):
    def __init__(self, motor, pin, div=16):
        self.motor = motor
        self.pin = pin
        self.div = div
        self.count = 0
        threading.Thread.__init__(self)

    def run(self):
        while True: 
            wait_for(R.io[0].input[self.pin].query.d)
            self.count += 1

    def rotations(self, angle, start_speed=50):
        seg = 360/self.div
        startcount = self.count
        current_dist = angle #Distance away from target
        R.motors[self.motor].target = start_speed
        while current_dist > 360:
            newcount = self.count - startcount
            current_dist = angle - newcount*seg
            R.motors[self.motor].target = 50
        while abs(current_dist) > seg/2:  
            newcount = self.count - startcount
            current_dist = angle - newcount*seg
            current_speed = start_speed * current_dist / 360
            if current_speed < 5:
                R.motors[self.motor].target = 5
            else:
                R.motors[self.motor].target = current_speed
        R.motors[self.motor].target = 0

WheelLeft = Encoder(0,0)
WheelLeft.start()
WheelRight = Encoder(1,3)
WheelRight.start()

WheelRight.rotations(720)
WheelLeft.rotations(720)
