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
bcx=250
bcy=0
a=[random.randint(0,490) ,random.randint(0,490)]
while True:
    bcy=bcy+1
    screen.fill(white)
    pygame.draw.circle(screen,blue,(bcx,bcy),5)
    pygame.display.update()
