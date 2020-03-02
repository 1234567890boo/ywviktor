import pygame,random
from pygame.locals import*

pygame.init()

width=1000
height=900

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
      self.x=(random.randint(30,870)//20)*20
      self.y=(random.randint(30,870)//20)*20
      self.width=20
      self.height=20
    def draw(self):
      pygame.draw.rect(screen,red,(self.x,self.y,self.width,self.height))
    def randomize(self):
      self.x=(random.randint(30,870)//20)*20
      self.y=(random.randint(30,870)//20)*20
        

class Snake:
    def __init__(self):
      self.x=500
      self.y=500
      self.width=20
      self.height=20
      self.vel=20
      self.points=0
      self.up=False
      self.down=False
      self.left=False
      self.right=False
    def draw(self):
      pygame.draw.rect(screen,green,(self.x,self.y,self.width,self.height))
    def move(self):
      if self.up==True:
        self.y-=self.vel
      elif self.down==True:
        self.y+=self.vel
      elif self.left==True:
        self.x-=self.vel
      elif self.right==True:
        self.x+=self.vel
    def food_collide(self,Food):
      if self.x==food.x and self.y==food.y:
        self.points+=1
        return True
      else:
        return False
    def wall_collide(self):
      if self.x<0:
        self.x=1000
      if self.x>1000:
        self.x=0
      if self.y<0:
        self.y=1000
      if self.y>1000:
        self.y=0
    def set_direction(self,direction):
      self.up=False
      self.down=False
      self.left=False
      self.right=False
      if direction=='up':
        self.up=True
      elif direction=='down':
        self.down=True
      elif direction=='left':
        self.left=True
      elif direction=='right':
        self.right=True
        
def grid():
    x=20
    y=20
    for n in range(0,101,1):
        pygame.draw.line(screen,white,(x,0),(x,900),1)
        pygame.draw.line(screen,white,(0,y),(1000,y),1)
        x+=20
        y+=20
    
snake=Snake()
food=Food()

while True:
    screen.fill(black)
    show_text('points='+str(snake.points),900,20,green)
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
              snake.set_direction('up')
            elif event.key==K_s and snake.up==False:
              snake.set_direction('down')
            elif event.key==K_a and snake.right==False:
              snake.set_direction('left')
            elif event.key==K_d and snake.left==False:
              snake.set_direction('right')
                
    snake.move()
    if snake.food_collide(food)==True:
      food.randomize()
    snake.wall_collide()
    pygame.display.update()
    
#Homework: Make snake grow







