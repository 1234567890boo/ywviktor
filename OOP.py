import pygame,random,time
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
    def __init__(self,color,x,y):
      self.x=x
      self.y=y
      self.width=20
      self.height=20
      self.vel=20
      self.points=0
      self.color=color
      self.up=True
      self.down=False
      self.left=False
      self.right=False
      self.snak=[]
      
    def draw(self):
      for n in self.snak:
        pygame.draw.rect(screen,self.color,(n[0],n[1],self.width,self.height))
        
    def move(self):
      self.snak.insert(0,(self.x,self.y))
      self.draw()
      if self.up==True:
        self.y-=self.vel
      elif self.down==True:
        self.y+=self.vel
      elif self.left==True:
        self.x-=self.vel
      elif self.right==True:
        self.x+=self.vel
      self.snak.pop()
        
    def food_collide(self,Food):
      if self.x==food.x and self.y==food.y:
        self.points+=1
        self.snak.append((self.x,self.y))
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

    def is_game_over(self):
      if len(self.snak)>0:
        if self.snak[0] in self.snak[1:]:
          screen.fill(black)
          if snake2.points>snake.points:
            show_text('Game over. Player 2 wins',500,450,red)
          else:
            show_text('Game over. Player 1 wins.',500,450,red)
          pygame.display.update()
          time.sleep(5)
          global return
        
def grid():
    x=20
    y=20
    for n in range(0,101,1):
        pygame.draw.line(screen,white,(x,0),(x,900),1)
        pygame.draw.line(screen,white,(0,y),(1000,y),1)
        x+=20
        y+=20
    
snake=Snake(blue,0,0)
snake2=Snake(green,100,90)
food=Food()

def player2():
  while True:    
      screen.fill(black)
      
      show_text('p1 points= '+str(snake.points),800,20,green)
      show_text('p2 points= '+str(snake2.points),100,20,green)
      
      food.draw()
      
      grid()
      
      clock.tick(10)
      
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

              if event.key==K_UP and snake2.down==False:
                snake2.set_direction('up')
              elif event.key==K_DOWN and snake2.up==False:
                snake2.set_direction('down')
              elif event.key==K_LEFT and snake2.right==False:
                snake2.set_direction('left')
              elif event.key==K_RIGHT and snake2.left==False:
                snake2.set_direction('right')
                  
      snake.move()
      snake2.move()
      
      if snake.food_collide(food)==True:
        food.randomize()
        
      if snake2.food_collide(food)==True:
        food.randomize()

      snake.wall_collide()
      snake2.wall_collide()
      
      pygame.display.update()
      
      snake.is_game_over()
      snake2.is_game_over()
#Homework: make player 2 and do sqlite commands

'''import pygame,random,time
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
    def __init__(self,color,x,y):
      self.x=x
      self.y=y
      self.width=20
      self.height=20
      self.vel=20
      self.points=0
      self.color=color
      self.up=True
      self.down=False
      self.left=False
      self.right=False
      self.snak=[]
      
    def draw(self):
      for n in self.snak:
        pygame.draw.rect(screen,self.color,(n[0],n[1],self.width,self.height))
        
    def move(self):
      self.snak.insert(0,(self.x,self.y))
      self.draw()
      if self.up==True:
        self.y-=self.vel
      elif self.down==True:
        self.y+=self.vel
      elif self.left==True:
        self.x-=self.vel
      elif self.right==True:
        self.x+=self.vel
      self.snak.pop()
        
    def food_collide(self,Food):
      if self.x==food.x and self.y==food.y:
        self.points+=1
        self.snak.append((self.x,self.y))
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

    def is_game_over(self):
      if (self.x,self.y) in self.snak[1:]:
        screen.fill(black)
        show_text('Game over. You loose',500,450,red)
        print('collision')
        pygame.display.update()
        time.sleep(1)
        quit()
        
        
def grid():
    x=20
    y=20
    for n in range(0,101,1):
        pygame.draw.line(screen,white,(x,0),(x,900),1)
        pygame.draw.line(screen,white,(0,y),(1000,y),1)
        x+=20
        y+=20

snake=[Snake(blue,0,0)]
snake.append(Snake(green,20,0))
food=Food()

while True:    
    screen.fill(black)
    
    show_text('p1 points= '+str(snake[0].points),800,20,green)
    show_text('p2 points= '+str(snake[1].points),100,20,green)
    
    food.draw()
    
    grid()
    
    clock.tick(10)
    
    snake[0].is_game_over()
    snake[1].is_game_over()
    
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

            if event.key==K_UP and snake2.down==False:
              snake2.set_direction('up')
            elif event.key==K_DOWN and snake2.up==False:
              snake2.set_direction('down')
            elif event.key==K_LEFT and snake2.right==False:
              snake2.set_direction('left')
            elif event.key==K_RIGHT and snake2.left==False:
              snake2.set_direction('right')
                
    snake.move()
    snake2.move()
    
    if snake.food_collide(food)==True:
      food.randomize()
      
    if snake2.food_collide(food)==True:
      food.randomize()

    snake.wall_collide()
    snake2.wall_collide()
    pygame.display.update()'''
