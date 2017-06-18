import time
import random  
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((500,500))
pygame.display.set_caption("Snowfall")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
bcx=random.randint(5,495)
bcy=0
bob=[]
for n in range(0,200,1):
    a=[random.randint(0,490),random.randint(0,490)]
    bob.append(a)
while True:
    bcy=bcy+1
    screen.fill(white)
    #pygame.draw.circle(screen,blue,(bcx,bcy),5)
    for n in bob:
        pygame.draw.circle(screen,blue,(n[0],n[1]),5)
        n[1]=n[1]+1
        if n[1]==500:
            n[0]=random.randint(5,495)
            n[1]=0
        if a==500:
            bcx=0
            bcx=bcx+1
    pygame.display.update()
