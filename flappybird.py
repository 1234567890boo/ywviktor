import random
import pygame
import time
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
x1=600
y1=0
y2=450
ychange=0
points=0
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",32)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
while True:
  screen.fill(white)
  show_text('points='+str(points),450,10,blue)
  pygame.draw.circle(screen,blue,(x,y,),20)
  y=y+ychange 
  for event in pygame.event.get():
    if event.type==QUIT:
      pygame.quit()
      exit() 
    if event.type==KEYDOWN:
      if event.key==K_SPACE:
        ychange=-1.5
    if event.type==KEYUP:
      if event.key==K_SPACE:
        ychange=1.5
        if y==600:
          quit()
  if y==0:
    quit() 
  pygame.draw.rect(screen,red,(x1,0,50,y1))
  pygame.draw.rect(screen,red,(x1,y1+150,50,600))
  x1=x1-1.5
  if x1==0:
    x1=601
    x1=x1-1.5
    y1=random.randint(50,450)
  if x1==x and 0<y<y1:
    quit()
  if x1==x and y1+150<y<y1+600:
    quit()
  if x==y+1 and x1==x and y1+150<y<y1+600:
    points=points+1
    show_text('points='+str(points),450,10,blue)
  if points==5:
    screen.fill(white)
    show_text('You Win!!'+str(points),300,300,blue)
  pygame.display.update()
