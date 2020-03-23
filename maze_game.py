import pygame,random,time
from pygame.locals import*

pygame.init()

width=100
height=100

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Maze Game")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

clock=pygame.time.Clock()


class Empty:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def draw(self, x , y):
        pygame.draw.rect(screen,white,(x*self.height, y*self.width, self.width, self.height))

class Player:
    def __init__(self, width, height):
        self.width=width
        self.height=height
        self.vel=10
    def draw(self, x , y):
        pygame.draw.rect(screen,green,(x*self.width, y*self.height, self.width, self.height))
    def collide(self):
        pass

class Wall:
    def __init__(self, width, height):
        self.width=width
        self.height=height

    def draw(self, x , y):
        pygame.draw.rect(screen,black,(x*self.height, y*self.width, self.width, self.height))

class Foe:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.vel=10
    def draw(self,x,y):
        if world[x][y]==f:
            pygame.draw.rect(screen,red,(x*self.height, y*self.width, self.width, self.height))

w=Wall(10,10)
e=Empty(10,10)
f=Foe(10,10)

world=[[w,w,w,w,w,w,w,w,w,w],
      [w,e,e,e,e,e,e,e,e,w],
      [w,e,e,w,w,w,e,w,e,w],
      [w,w,e,w,e,e,e,w,e,w],
      [w,e,e,e,e,w,w,w,e,w],
      [w,e,e,w,w,w,e,w,e,w],
      [w,e,e,e,e,e,e,w,e,w],
      [w,e,e,w,w,w,e,e,e,w],
      [w,e,e,e,e,e,e,e,f,w],
      [w,w,w,w,w,w,w,w,w,w]]

player=Player(10,10)
px=2
py=2
world[px][py]=player
def drawMap():
    screen.fill(white)
    for x in range(0,10,1):
            for y in range(0,10,1):
                world[x][y].draw(x,y)



def MovePlayer(shift_x, shift_y):
    global px
    global py
    if world[px+shift_x][py+shift_y]==e:
        world[px][py]=e
        world[px+shift_x][py+shift_y]=player
        px+=shift_x
        py+=shift_y

while True:
    drawMap()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_w or event.key==K_UP:
                MovePlayer(0,-1)
            if event.key==K_s or event.key==K_DOWN:
                MovePlayer(0,1)
            if event.key==K_a or event.key==K_LEFT:
                MovePlayer(-1,0)
            if event.key==K_d or event.key==K_RIGHT:
                MovePlayer(1,0)
    pygame.display.update()
