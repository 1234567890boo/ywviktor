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
runcatr=['runcatr1.png']
runcat=['runcat1.png','runcat2.png','runcat3.png','runcat4.png','runcat5.png','runcat6.png','runcat7.png','runcat8.png',]
while True:
##    for var in runcat:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit
            exit()
        if event.type==KEYDOWN:
            if event.key==K_d:
                screen.fill(black)
                x=x+10
                img=pygame.image.load(runcat[a])
                a=a+1
                if a==7:
                    a=0
                screen.blit(img,(x,y))
                if x==1000:
                    x=0
            if event.key==K_a:
                screen.fill(black)
                x=x-10
                img=pygame.image.load(runcatr[0])
                screen.blit(img,(x,y))
##                    a=a+1
##                    if a==0:
##                        a=0
        pygame.display.update()
