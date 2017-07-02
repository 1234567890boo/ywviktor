import time
import random
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((640,480))
pygame.display.set_caption("Snake")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
foodx=(random.randint(0,640)//10)*10
foody=(random.randint(0,480)//10)*10
snakex=(random.randint(0,640)//10)*10
snakey=(random.randint(0,480)//10)*10
up=0
down=0
left=0
right=0
points=0
n=pygame.time.Clock()
snake=[]
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",32)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
while True:
    screen.fill(black)
    n.tick(10)
    snake.insert(0,[snakex,snakey])
    pygame.draw.rect(screen,red,(foodx,foody,10,10))
    for segment in snake:
        pygame.draw.rect(screen,green,segment+[10,10])
    snake.pop()
    for event in pygame.event.get():
        if event.type==KEYDOWN:
            if event.key==K_UP:
                up=1
                down=0
                left=0
                right=0
        if event.type==KEYDOWN:
            if event.key==K_DOWN:
                up=0
                down=1
                left=0
                right=0
        if event.type==KEYDOWN:
            if event.key==K_LEFT:
                up=0
                down=0
                left=1
                right=0
        if event.type==KEYDOWN:
            if event.key==K_RIGHT:
                up=0
                down=0
                left=0
                right=1
    if down:
        snakey=snakey+10
    if up:
        snakey=snakey-10
    if left:
        snakex=snakex-10
    if right:
        snakex=snakex+10
    if foodx==snakex and foody==snakey:
        foodx=(random.randint(0,640)//10)*10
        foody=(random.randint(0,480)//10)*10
        snake.insert(0,[snakex,snakey])
        points=points+1
    show_text('points='+str(points),320,10,red)
    if [snakex,snakey] in snake[1:]:
        screen.fill(black)
        show_text('Game over. You loose',100,240,red)
        pygame.display.update()
        time.sleep(1)
        quit()
    pygame.display.update()
