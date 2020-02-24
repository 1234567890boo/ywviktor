import pygame,random
from pygame.locals import*

pygame.init()

width=500
height=500

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Snake OOP")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

class Food:
    def __init__(self):
        self.x=random.randint(30,470)
        self.y=random.randint(30,470)
        self.width=10
        self.height=10
    def draw(self):
        pygame.draw.rect(screen,red,(self.x,self.y,self.width,self.height))

class Snake:
    def __init__(self):
        self.x=250
        self.y=250
        self.width=10
        self.height=10
        self.vel=0.25
        self.up=False
        self.down=False
        self.left=False
        self.right=False
    def draw(self):
        pygame.draw.rect(screen,green,(self.x,self.y,self.width,self.height))

snake=Snake()
food=Food()

while True:
    screen.fill(black)
    snake.draw()
    food.draw()
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_w:
                snake.up=True
                snake.down=False
                snake.left=False
                snake.right=False
            elif event.key==K_s:
                snake.down=True
                snake.up=False
                snake.left=False
                snake.right=False
            elif event.key==K_a:
                snake.right=True
                snake.left=False
                snake.up=False
                snake.down=False
            elif event.key==K_d:
                snake.left=True
                snake.right=False
                snake.up=False
                snake.down=False
    if snake.up==True:
        snake.y-=snake.vel
    elif snake.down==True:
        snake.y+=snake.vel
    elif snake.left==True:
        snake.x+=snake.vel
    elif snake.right==True:
        snake.x-=snake.vel
#Homework: make left and right movement and be able to eat food







