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
                print('W key pressed')               
                LP_U=1
            elif event.key==K_s:
                print('S key pressed')               
                LP_D=1
            if event.key==K_UP:
                print('UP key pressed')
                RP_U=1
            elif event.key==K_DOWN:
                print('DOWN key pressed')
                RP_D=1               
        elif event.type==KEYUP:
            if event.key==K_w:
                print('W key pressed')
                LP_U=0
            elif event.key==K_s:
                print('S key pressed')
                LP_D=0
            if event.key==K_UP:
                print('UP key pressed')
                RP_U=0
            elif event.key==K_DOWN:
                print('DOWN key pressed')
                RP_D=0                
    pygame.draw.rect(screen,blue,(10,LPY,10,150))
    pygame.draw.rect(screen,green,(590,RPY,10,150))
    pygame.draw.circle(screen,black,(320,240),10)
    if LP_U==1:
        LPY=LPY-5
    if LP_D==1:
        LPY=LPY+5
    if RP_U==1:
        RPY=RPY-5
    if RP_D==1:
        RPY=RPY+5        
    
    
