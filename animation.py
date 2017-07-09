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
runcat=['runcat1.png','runcat2.png','runcat3.png','runcat4.png','runcat5.png','runcat6.png','runcat7.png','runcat8.png',]
while True:
    for var in runcat:
        img=pygame.image.load(var)
        screen.fill(black)
        screen.blit(img,(10,10))
        pygame.display.update()
