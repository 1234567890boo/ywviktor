import time
import random  
import pygame
from pygame.locals import*
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong!")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
while True:
    pygame.display.update()
    screen.fill(white)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==KEYDOWN:
            if event.key==K_LEFT:
                print('Left key pressed')
            elif event.key==K_RIGHT:
                print('Right key pressed')
            elif event.key==K_DOWN:
                print('Down key pressed')
            elif event.key==K_UP:
                print('Up key pressed')
