import time
import random
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((300,400))
pygame.display.set_caption("tictactoe")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
chance=1
boo={'1':'','2':'','3':'','4':'','5':'','6':'','7':'','8':'','9':''}
tie_var=0
boo2={(0,0):'1',(100,0):'2',(200,0):'3',(0,100):'4',(100,100):'5',(200,100):'6',(0,200):'7',(100,200):'8',(200,200):'9'}
v="X win's"
b="O win's"
t="Tie"
def WIN():
    pygame.display.update()
    for n in range(1,8,3):
        m=str(n+1)
        l=str(n+2)
        n=str(n)
        if boo[n]==boo[m]==boo[l]=='x':
            print(v)
            show_text(v,50,350,blue)
            time.sleep(1)
            exit()
        if boo[n]==boo[m]==boo[l]=='o':
            print(b)
            show_text(b,50,350,blue)
            time.sleep(1)
            exit()
    for n in range(1,4,1):
        m=str(n+3)
        l=str(n+6)
        n=str(n)
        if boo[n]==boo[m]==boo[l]=='x':
            print(v)
            show_text(v,50,350,blue)
            exit()
        if boo[n]==boo[m]==boo[l]=='o':
            print(b)
            show_text(b,50,350,blue)   
            exit()
    if (boo['1']==boo['5']==boo['9']=='o') or ( boo['3']==boo['5']==boo['7']=='o'):
        print(b)
        show_text(b,50,350,blue)        
        exit()
    if (boo['1']==boo['5']==boo['9']=='x' ) or (boo['3']==boo['5']==boo['7']=='x'):
        print(v)
        show_text(v,50,350,blue)        
        exit()
def tie():
    global tie_var
    for k in boo:
        if boo[k]=='':
            tie_var = 1
    if tie_var==0:
        print('tie')
        show_text(t,50,350,blue)
        quit()
    tie_var=0     
def show_text(msg,x,y,color):
    fontobj= pygame.font.SysFont("freesans",60)
    msgobj = fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
    pygame.display.update()
    
def box_x(x,y):
    pygame.draw.line(screen,white,(x,y),(x+100,y+100),5)
    pygame.draw.line(screen,white,(x+100,y),(x,y+100),5)
def box_o(x,y):
    pygame.draw.circle(screen,white,(x+50,y+50),50,5)
pygame.draw.line(screen,white,(100,0),(100,300),5)
pygame.draw.line(screen,white,(200,0),(200,300),5)
pygame.draw.line(screen,white,(0,100),(300,100),5)
pygame.draw.line(screen,white,(0,200),(300,200),5)
pygame.draw.line(screen,white,(0,300),(300,300),5)
while True:
   pygame.display.update()
   for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            x=event.pos[0]-event.pos[0]%100
            y=event.pos[1]-event.pos[1]%100
            number=int(x/100)+int(y/100)*3+1
            box_num=(boo2[x,y])
            if boo[box_num]=='':
                if chance%2==1:
                    box_o(x,y)
                    boo[box_num]='o'
                else:
                    box_x(x,y)
                    boo[box_num]='x'
                chance=chance+1
                WIN()
                tie()
