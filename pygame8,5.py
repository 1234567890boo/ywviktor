import time
import random
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((300,300))
pygame.display.set_caption("tictactoe")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
boo={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'}
#this is a comint
def box_x(x,y):
    pygame.draw.line(screen,white,(x,y),(x+100,y+100),5)
    pygame.draw.line(screen,white,(x+100,y),(x,y+100),5)
def box_o(x,y):
    pygame.draw.circle(screen,white,(x+50,y+50),50,5)
pygame.draw.line(screen,white,(100,0),(100,300),5)
pygame.draw.line(screen,white,(200,0),(200,300),5)
pygame.draw.line(screen,white,(0,100),(300,100),5)
pygame.draw.line(screen,white,(0,200),(300,200),5)
while True:
   for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            #print('mouse at:',event.pos)
            x=event.pos[0]-event.pos[0]%100
            y=event.pos[1]-event.pos[1]%100
            number=int(x/100)+int(y/100)*3+1
            print(number)
            box_o(x,y)
            box_x(x,y)
        pygame.display.update()
