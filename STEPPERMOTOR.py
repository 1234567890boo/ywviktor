import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
pins=[26,19,13,6]
GPIO.setup(pins,GPIO.OUT)
p1=[(0,0,0,1),(0,0,1,0),(0,1,0,0),(1,0,0,0)]
print('how many turns?')
Z=int(input())
for x in range(0,Z,1):
    for n in p1:
        GPIO.output(pins,n)
        time.sleep(0.002)

