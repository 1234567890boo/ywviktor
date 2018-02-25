import time
import random  
import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((490,490))
pygame.display.set_caption("OOP snake")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
n=pygame.time.Clock()
snake1=[]
up=0
down=0
left=0
right=0
ychange=5
xchange=5
snakex=(random.randint(10,490)//10)*10
snakey=(random.randint(10,490)//10)*10
foodx=(random.randint(10,490)//10)*10
foody=(random.randint(10,490)//10)*10
points=0
def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",32)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))
class snake:
    def __init__(self,x,y,color,width,hight):
        self.x=x
        self.y=y
        self.width=width
        self.hight=hight
        self.color=color
    def move(self,xchange,ychange):
        self.x=self.x+xchange
        self.y=self.y+ychange
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.hight))
class food:
    def __init__(self,x,y,color,width,hight):
        self.x=x
        self.y=y
        self.color=color
        self.width=width
        self.hight=hight
    def move(self,xchange2,ychange2):
        self.y=self.y+ychange
        self.x=self.x+xchange
    def draw(self):
       pygame.draw.rect(screen,self.color,(self.x,self.y,self.width,self.hight))
snake=snake(snakex,snakey,green,10,10)
food=food(foodx,foody,red,10,10)
snake.draw()
snake.move(snake.x,snake.y)
food.draw()
food.move(food.x,food.y)
snake.x=(random.randint(10,490)//10)*10
snake.y=(random.randint(10,490)//10)*10
food.x=(random.randint(10,490)//10)*10
food.y=(random.randint(10,490)//10)*10
while True:
    n.tick(15)
    screen.fill(black)
    food.draw()
    snake1.insert(0,[snake.x,snake.y])
    show_text('points='+str(points),150,10,red)
    for segment in snake1:
        pygame.draw.rect(screen,green,segment+[10,10])
    snake1.pop()
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
        snake.y=snake.y+10
    if up:
        snake.y=snake.y-10
    if left:
        snake.x=snake.x-10
    if right:
        snake.x=snake.x+10
    if food.x==snake.x and food.y==snake.y:
        food.x=(random.randint(0,450)//10)*10
        food.y=(random.randint(0,450)//10)*10
        snake1.insert(0,[snake.x,snake.y])
        points=points+1
    if [snake.x,snake.y] in snake1[1:]:
      screen.fill(black)
      show_text('Game over. You loose',100,240,red)
      pygame.display.update()
      time.sleep(1)
      quit()
    if snake.y==0:
      screen.fill(black)
      show_text('Game over. You loose',100,240,red)
      pygame.display.update()
      time.sleep(1)
      quit()
    if snake.y==500:
      screen.fill(black)
      show_text('Game over. You loose',100,240,red)
      pygame.display.update()
      time.sleep(1)
      quit()
    if snake.x==0:
      screen.fill(black)
      show_text('Game over. You loose',100,240,red)
      pygame.display.update()
      time.sleep(1)
      quit()
    if snake.x==500:
      screen.fill(black)
      show_text('Game over. You loose',100,240,red)
      pygame.display.update()
      time.sleep(1)
      quit()

    pygame.display.update()
