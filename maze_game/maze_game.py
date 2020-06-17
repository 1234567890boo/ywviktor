import pygame,random,time
from pygame.locals import*

from classes.view import *
from classes.empty import *
from classes.player import *
from classes.enemy import *
from classes.utils import *
from classes.mapView import *
from classes.wall import *


width=450
height=300

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)


        
clock=pygame.time.Clock()

mainmap=MapView(30,30)

def wallplacey(x,spos,epos):
    for y in range(spos,epos+1):
        mainmap.putobj(x,y,Wall())
def wallplacex(y,spos,epos):
    for x in range(spos,epos+1):
        mainmap.putobj(x,y,Wall())


wallplacex(0,0,29)
wallplacex(29,0,29)
wallplacey(0,0,29)
wallplacey(29,0,29)

wallplacex(6,1,15)
wallplacex(24,5,23) 
wallplacey(11,1,1)

def placeRandom(pview,obj):
    randomx=random.randint(1,28)
    randomy=random.randint(1,28)
    while pview.getobj(randomx,randomy).kind()!="Empty":
        randomx=random.randint(1,28)
        randomy=random.randint(1,28)
    pview.putobj(randomx,randomy,obj)
    
placeRandom(mainmap,PlayerView(green,{pygame.K_w:'up',pygame.K_s:'down',pygame.K_a:'left',pygame.K_d:'right'}))
placeRandom(mainmap,PlayerView(blue,{pygame.K_i:'up',pygame.K_k:'down',pygame.K_j:'left',pygame.K_l:'right'}))
for n in range(1,20):
        placeRandom(mainmap,EnemyView())

pygame.init()
screen = pygame.display.set_mode((width, height))

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    key=event.key
                    mainmap.handleKey(key,None,0,0)
        mainmap.handleCycle(None,0,0)
        screen.fill((white))
        mainmap.draw(screen,0,0,300,300)
        clock.tick(7)
        pygame.display.flip()

    
'''
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
    def __init__(self,pos_x,pos_y,width,height):
        self.pos_x=pos_x
        self.pos_y=pos_y
        self.width=width
        self.height=height
        self.vel=10
    def draw(self,x,y):
        if world[x][y]==f:
            pygame.draw.rect(screen,red,(x*self.height, y*self.width, self.width, self.height))
    def Movefoe(self,shift_xf, shift_yf):
        if world[self.pos_x+shift_xf][self.pos_y+shift_yf]==e:
            world[self.pos_x][self.pos_y]=e
            world[self.pos_x+shift_xf][self.pos_y+shift_yf]=f
            self.pos_x+=shift_xf
            self.pos_y+=shift_yf
    def fmove(self):
        n=random.randint(1,4)
        if n==1:
            self.Movefoe(0,-1)
        elif n==2:
            self.Movefoe(0,1)
        elif n==3:
            self.Movefoe(-1,0)
        elif n==4:
            self.Movefoe(1,0)
w=Wall(10,10)
e=Empty(10,10)
foes=[Foe(7,7,10,10),Foe(8,2,10,10)]

world=[[w,w,w,w,w,w,w,w,w,w],
      [w,e,e,e,e,e,e,e,e,w],
      [w,e,e,w,w,w,e,w,e,w],
      [w,w,e,w,e,e,e,w,e,w],
      [w,e,e,e,e,w,w,w,e,w],
      [w,e,e,w,w,w,e,w,e,w],
      [w,e,e,e,e,e,e,w,e,w],
      [w,e,e,w,w,w,e,e,e,w],
      [w,e,e,e,e,e,e,e,e,w],
      [w,w,w,w,w,w,w,w,w,w]]

player=Player(10,10)
px=2
py=2
world[px][py]=player
for f in foes:
    world[f.pos_x][f.pos_y]=f
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
    for f in foes:
        f.fmove()
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
    pygame.display.update()'''
