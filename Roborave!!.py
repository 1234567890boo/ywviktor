Rp1=12
Rp2=12
Lp1=12
Lp2=12
F=50
Startdc=50
import RPI.GPIO as GPIO
def clens():
    GPIO.cleanup()
def start():
    R1p.start(Startdc)
    R2p.start(Startdc)
    L1p.start(Startdc)
    L2p.start(Startdc)
def Setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pn,GPIO.IN)
    R1p=GPIO.PWM(Rp1,F)
    R2p=GPIO.PWM(Rp1,F)
    L1p=GPIO.PWM(Rp1,F)
    L2p=GPIO.PWM(Rp1,F)
def front():
    Startdc

    
