import pygame,random,time,OOP
from pygame.locals import*

pygame.init()

width=1000
height=900

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Snake menu")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

points=0
clock=pygame.time.Clock()

def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",100)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))

'''while True:
    screen.fill(black)
    show_text('One player',20,20,green)
    show_text('Two players',550,20,green)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==MOUSEBUTTONDOWN and event.button==1:
            if event.pos[0]>=20 and event.pos[0]<=385 and event.pos[1]>=20 and event.pos[1]<=100:
                OOP.player(num=1)
            if event.pos[0]>=550 and event.pos[0]<=850 and event.pos[1]>=20 and event.pos[1]<=100:
                OOP.player(num=2)
    pygame.display.update()'''

num=1
while True:
    screen.fill(black)
    show_text('Players: '+str(num),350,200,green)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
          if event.key==K_UP:
            num+=1
            if num>=2:
              num=2
          if event.key==K_DOWN:
            num-=1
            if num<=0:
              num=0
          if event.key==K_RETURN:
            OOP.player(num)
    pygame.display.update()
