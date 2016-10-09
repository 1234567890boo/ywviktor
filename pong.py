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
LPY=120
RPY=120
LP_U=0
LP_D=0
RP_U=0
RP_D=0
BXM=320
BYM=240
RX=random.randint(-2,2)
RY=random.randint(-2,2)
def BBB(RR,BXM):
    RA=random.randint(-2,2)
    if RA<0 and RR<0:
        RA=-RA
        RR=RA
    if RA>0 and RR>0:
        RA=-RA
        RR=RA
    return RA
while RX==0:
    RX=random.randint(-5,5)
    RY=random.randint(-5,5)
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
                LP_U=1
            elif event.key==K_s:               
                LP_D=1
            if event.key==K_UP:
                RP_U=1
            elif event.key==K_DOWN:
                RP_D=1               
        elif event.type==KEYUP:
            if event.key==K_w:
                LP_U=0
            elif event.key==K_s:
                LP_D=0
            if event.key==K_UP:
                RP_U=0
            elif event.key==K_DOWN:
                RP_D=0                
    pygame.draw.rect(screen,blue,(10,LPY,10,100))
    pygame.draw.rect(screen,green,(610,RPY,10,100))
    pygame.draw.circle(screen,red,(BXM,BYM),10)
    if LP_U==1:
        LPY=LPY-5
    if LP_D==1:
        LPY=LPY+5
    if RP_U==1:
        RPY=RPY-5
    if RP_D==1:
        RPY=RPY+5
    BXM=BXM+RX
    BYM=BYM+RY
    if BXM==640:
        RX =-RX
    if BYM==480:
        RY =-RY
    if BXM==0:
        RX =-RX
    if BYM==0:
        RY =-RY 
