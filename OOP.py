import pygame,random
from pygame.locals import*

pygame.init()

width=1000
height=1000

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Snake OOP")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

points=0
clock=pygame.time.Clock()

def show_text(msg,x,y,color):
  fontobj=pygame.font.SysFont("freesans",32)
  msgobj=fontobj.render(msg,False,color)
  screen.blit(msgobj,(x,y))

class Food:
    def __init__(self):
        self.x=(random.randint(30,970)//20)*20
        self.y=(random.randint(30,970)//20)*20
        self.width=20
        self.height=20
    def draw(self):
        pygame.draw.rect(screen,red,(self.x,self.y,self.width,self.height))

class Snake:
    def __init__(self):
        self.x=500
        self.y=500
        self.width=20
        self.height=20
        self.vel=20
        self.up=False
        self.down=False
        self.left=False
        self.right=False
    def draw(self):
        pygame.draw.rect(screen,green,(self.x,self.y,self.width,self.height))
        
def grid():
    x=20
    y=20
    for n in range(0,101,1):
        pygame.draw.line(screen,white,(x,0),(x,1000),1)
        pygame.draw.line(screen,white,(0,y),(1000,y),1)
        x+=20
        y+=20
    
snake=Snake()
food=Food()

while True:
    screen.fill(black)
    show_text('points='+str(points),20,900,red)
    food.draw()
    grid()
    snake.draw()
    clock.tick(10)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_w and snake.down==False:
                snake.up=True
                snake.down=False
                snake.left=False
                snake.right=False
            elif event.key==K_s and snake.up==False:
                snake.down=True
                snake.up=False
                snake.left=False
                snake.right=False
            elif event.key==K_a and snake.left==False:
                snake.right=True
                snake.left=False
                snake.up=False
                snake.down=False
            elif event.key==K_d and snake.right==False:
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
    if snake.x==food.x and snake.y==food.y:
        food.x=(random.randint(30,970)//20)*20
        food.y=(random.randint(30,970)//20)*20
        points+=1
    
#Homework: make left and right movement and be able to eat food







