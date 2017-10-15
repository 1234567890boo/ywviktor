import time
import random  
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Pong!")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
xc=1
yc=1
xc2=-1
yc2=-1
class ball:
    def __init__(self,x,y,color,radius):
        self.x=x
        self.y=y
        self.color=color
        self.radius=radius
    def move(self,xchange,ychange):
        self.x=self.x+xchange
        self.y=self.y+ychange
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius)

ball1=ball(320,240,blue,14)
ball2=ball(320,240,red,14)
while True:
    screen.fill(white)
    ball1.draw()
    ball1.move(xc,yc) 
    if ball1.x>639:
        xc=-xc
    if ball1.y>479:
        yc=-yc
    if ball1.y<1:
        yc=-yc
    if ball1.x<1:
        xc=-xc
    ball2.draw()
    ball2.move(xc2,yc2) 
    if ball2.x>639:
        xc2=-xc2
    if ball2.y>479:
        yc2=-yc2
    if ball2.y<1:
        yc2=-yc2
    if ball2.x<1:
        xc2=-xc2
    if ball1.x in range(ball2.x-14,ball2.x+14) and ball1.y in range(ball2.y-14,ball2.y+14):
        xc=-xc
        yc=-yc
        xc2=-xc2
        yx2=-yc2
    pygame.display.update()
