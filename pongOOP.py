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
p1x=635
p1y=240
p1color=blue
p1xy=20,5
L=0
R=0
LPP=0
RPP=0
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
class paddle:
    def __init__(self,x,y,color,w,h):
        self.x=x
        self.y=y
        self.color=color
        self.w=w
        self.h=h
    def move(self,ychange):
        self.y=self.y+ychange
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.w,self.h))
ball1=ball(320,240,blue,14)
ball2=ball(320,240,red,14)
paddle2=paddle(10,240,green,20,160)
paddle1=paddle(610,240,blue,20,160)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
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
        if event.type==KEYDOWN:
            if event.key==K_w:          
                L=-1
            elif event.key==K_s:               
                L=1
            if event.key==K_UP:
                R=-1
            elif event.key==K_DOWN:
                R=1               
        elif event.type==KEYUP:
            if event.key==K_w:
                L=0
            elif event.key==K_s:
                L=0
            if event.key==K_UP:
                R=0
            elif event.key==K_DOWN:
                R=0    
    ball1.draw()
    ball1.move(xc,yc)
    paddle1.draw()
    paddle2.draw()
    paddle1.move(R)
    paddle2.move(L)
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
    if ball1.x>=paddle1.x and paddle1.y<ball1.y<paddle1.y+160:
        xc=-xc
    if ball2.x>=paddle1.x and paddle1.y<ball2.y<paddle1.y+160:
        xc2=-xc2
    if ball2.x<=paddle2.x+30 and paddle2.y<ball2.y<paddle2.y+160:
        xc2=-xc2
    if ball1.x<=paddle2.x+30 and paddle2.y<ball1.y<paddle2.y+160:
        xc=-xc
    if ball1.x==635:
        RPP=RPP+1
    if ball1.x==5:
        LPP=LPP+1
    if ball2.x==635:
        RPP=RPP+1
    if ball2.x==5:
        LPP=LPP+1
    if LPP==10:
        show_text("LP wins!",320,240,blue)
        pygame.display.update()
        time.sleep(0.5)
        quit()
    if RPP==10:
        show_text("LP wins!",320,240,blue)
        pygame.display.update()
        time.sleep(0.1)
        quit()
    show_text("LP points="+str(LPP),5,20,blue)
    show_text("RP points="+str(RPP),5,400,green)
