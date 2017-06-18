import time
import random  
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Flappy Bird!")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
x=300
y=300
ychange=0
while True:
  screen.fill(white)
  pygame.draw.circle(screen,blue,(x,y,),15)
  y=y+ychange 
  for event in pygame.event.get():
    if event.type==QUIT:
      pygame.quit()
      exit() 
    if event.type==KEYDOWN:
      if event.key==K_SPACE:
        ychange=-9
        print('space key pressed')
    if event.type==KEYUP:
      if event.key==K_SPACE:
        ychange=1
        print('space key relesed')
  pygame.display.update()
