import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("animation")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
screen.fill(black)
x=10
y=10
a=0
change=0
runcatr=['runcatr1.png','runcatr2.png','runcatr3.png','runcatr4.png','runcatr5.png','runcatr6.png','runcatr7.png','runcatr8.png']
runcat=['runcat1.png','runcat2.png','runcat3.png','runcat4.png','runcat5.png','runcat6.png','runcat7.png','runcat8.png',]
while True:
##    for var in runcat:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit
            exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                change=1        
        if event.type==KEYUP:
            if event.key==K_d:
                change=0
        if event.type==KEYDOWN:
            if event.key==K_a:
                change=2
        if event.type==KEYUP:
            if event.key==K_a:
                change=0

    if change==1:
        screen.fill(black)
        x=x+10
        img=pygame.image.load(runcat[a])
        time.sleep(0.05)
        a=a+1
        if a==8:
            a=0
        screen.blit(img,(x,y))
        if x==1000:
            x=0
    if change==2:
        screen.fill(black)
        x=x-10
        img=pygame.image.load(runcatr[a])
        time.sleep(0.05)
        a=a+1
        if a==8:
            a=0
        screen.blit(img,(x,y))
        if x==0:
            x=1000
    pygame.display.update()
    
