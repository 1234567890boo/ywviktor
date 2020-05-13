import pygame,random,time
from pygame.locals import*

width=450
height=300

pygame.init()
screen = pygame.display.set_mode((width, height))

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

class View:
    pass

class Empty:
    def draw(self,x,y,width,height):
        pass

class PlayerView: #Extends View
    def __init__(self,color,keys):
        self.color=color
        
        self.keys=keys
    def draw(self,x,y,width,height):
        pygame.draw.rect(screen,self.color,(x,y,width,height))
    def handleKey(self,key):
         command=self.keys.get(key,'')
         if command=='up':
             self.y-=10
         if command=='down':
             self.y+=10
         if command=='left':
             self.x-=10
         if command=='right':
             self.x+=10
            


class MapView:
    def __init__(self,gridwidth,gridheight):
        self.grid=[]
        self.gridwidth=gridwidth
        self.gridheight=gridheight
        for x in range(0,gridwidth,1):
            column=[]
            for y in range(0,gridheight,1):
                column.append(Empty())
            self.grid.append(column)
    def putobj(self,x,y,obj):
        self.grid[x][y]=obj
    def draw(self,x,y,width,height):
        cellwidth=int(width/self.gridwidth)
        cellheight=int(height/self.gridheight)
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobject=self.grid[xgrid][ygrid]
                self.grid[xgrid][ygrid].draw(x+xgrid*cellwidth,y+ygrid*cellheight,cellwidth,cellheight)
            
clock=pygame.time.Clock()

players=[PlayerView(green,{pygame.K_w:'up',pygame.K_s:'down',pygame.K_a:'left',pygame.K_d:'right'}),
         PlayerView(blue,{pygame.K_UP:'up',pygame.K_DOWN:'down',pygame.K_LEFT:'left',pygame.K_RIGHT:'right'})]

mainmap=MapView(30,30)
mainmap.putobj(2,2,players[0])
mainmap.putobj(4,4,players[1])

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    for p in players:
                        p.handleKey(key)
                       
        screen.fill((white))
        mainmap.draw(0,0,300,300)
        clock.tick(60)
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
