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
LPY=120
RPY=120
LP_U=0
LP_D=0
RP_U=0
RP_D=0
BXM=320
BYM=240
RX=random.randint(-1,1)
RY=random.randint(-1,1)
LP=0
RP=0
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",32)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
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
    RX=random.randint(0,2)
    RY=random.randint(0,2)
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
    pygame.draw.rect(screen,blue,(10,LPY,15,110))
    pygame.draw.rect(screen,green,(600,RPY,15,110))
    pygame.draw.circle(screen,red,(BXM,BYM),10)
    if BXM==600 and RPY<BYM<RPY+110:
        RX=-RX
        RY=-RY
    if BXM==15 and LPY<BYM<LPY+110:
        RX=-RX
        RY=-RY    
    if LP_U==1:
        LPY=LPY-2
    if LP_D==1:
        LPY=LPY+2
    if RP_U==1:
        RPY=RPY-2
    if RP_D==1:
        RPY=RPY+2
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
    if BXM==640:
        LP=LP+1
        print('LP=',LP)
    if BXM==0:
        RP=RP+1
    if RP==10:
        show_text("RP wins!"+str(RP),5,580,blue)
        exit()
    if LP==10:
        show_text("LP wins!"+str(LP),5,20,blue)
        exit()
    show_text("LP points="+str(LP),5,20,blue)
    show_text("RP points="+str(RP),5,580,blue)
