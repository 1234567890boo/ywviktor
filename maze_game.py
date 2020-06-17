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

import utils

class View:
    def kind(self):
        return "View"
    def canReplace(self,obj):
        return False
    def handleCycle(self,pview,x,y):
        pass
    
class Empty(View):
    def kind(self):
        return "Empty"
    def draw(self,x,y,width,height):
        pass
    def handleKey(self,key,pview,x,y):
        pass
    def canReplace(self,obj):
        return True
    
class PlayerView(View): #Extends View
    def kind(self):
        return "Player"
    def __init__(self,color,keys):
        self.color=color
        self.keys=keys
    def draw(self,x,y,width,height):
        pygame.draw.rect(screen,self.color,(x,y,width,height))
    def handleKey(self,key,pview,x,y):
         command=self.keys.get(key,'')
         if command=='up':
             pview.moveobj(x,y,x,y-1)
         if command=='down':
             pview.moveobj(x,y,x,y+1)
         if command=='left':
             pview.moveobj(x,y,x-1,y)
         if command=='right':
             pview.moveobj(x,y,x+1,y)
         if command!='':
             return True
         return False
        
class EnemyView(View):
    def kind(self):
        return "Enemy"
    def __init__(self):
        pass
    def draw(self,x,y,width,height):
        pygame.draw.rect(screen,red,(x,y,width,height))
    def handleKey(self,key,pview,x,y):
        return False
    def canReplace(self,obj):
        return False
    def handleCycle(self,pview,x,y):
        movements={0:(-1,0),
                   1:(1,0),
                   2:(0,-1),
                   3:(0,1)}
        # get all players 
        players=pview.get_items("Player")
        
        # leave only visible players [(player, x, y)]
        playersVisible=[]
        ecoord=(x,y)
        for player in players:
            pcoords=(player[1],player[2])
            if pview.hasPath(ecoord,pcoords):
                playersVisible.append(player)
        
        if len(playersVisible)>0:
            # pick closest from visible
            closestVisibleCoords=(playersVisible[0][1],playersVisible[0][2])
            closestDist=len(utils.get_line(ecoord,closestVisibleCoords))
            for player in playersVisible:
                pcoords=(player[1],player[2])
                dist=len(utils.get_line(ecoord,pcoords))
                if dist<closestDist:
                    closestDist=dist
                    closestVisibleCoords=pcoords
                
            # get direction
            shift=pview.giveShift(ecoord,closestVisibleCoords)
        else:
            #nothing was visible. move random
            shift=movements[random.randint(0,3)]
        # Move enemy
        newx=x+shift[0]
        newy=y+shift[1]
        pview.moveobj(x,y,newx,newy)
    
class MapView(View):
    def kind(self):
        return "Map_View"
    def __init__(self,gridwidth,gridheight):
        self.grid=[]
        self.gridwidth=gridwidth
        self.gridheight=gridheight
        for x in range(0,gridwidth,1):
            column=[]
            for y in range(0,gridheight,1):
                column.append(Empty())
            self.grid.append(column)
    def handleKey(self,key,pview,x,y):
        res=False
        for xgrid in range(0,self.gridwidth,1):
            if res: break
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                res=gobj.handleKey(key,self,xgrid,ygrid)
                if res: break
    def handleCycle(self,pview,x,y):
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                res=gobj.handleCycle(self,xgrid,ygrid)
    def hasPath(self,p1,p2):
        path=utils.get_line(p1,p2)
        path.pop(0)
        path.pop(len(path)-1)
        for p in path:
            kind=self.getobj(p[0],p[1]).kind()
            if kind!="Empty" and kind!="Enemy":
                return False
        return True
    def giveShift(self,source,dest):
        path=utils.get_line(source,dest)
        nextPoint=path[1]
        shift=(nextPoint[0]-source[0],nextPoint[1]-source[1])
        return shift
    def putobj(self,x,y,obj):
        self.grid[x][y]=obj
    def getobj(self,x,y):
        return self.grid[x][y]
    def moveobj(self,sx,sy,dx,dy):
        sobj=self.getobj(sx,sy)
        dobj=self.getobj(dx,dy)
        if dobj.canReplace(sobj):
            self.putobj(dx,dy,sobj)
            self.putobj(sx,sy,Empty())
    def draw(self,x,y,width,height):
        cellwidth=int(width/self.gridwidth)
        cellheight=int(height/self.gridheight)
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                self.getobj(xgrid,ygrid).draw(x+xgrid*cellwidth,y+ygrid*cellheight,cellwidth,cellheight)
    def get_items(self,kind):
        items=[]
        for xgrid in range(0,self.gridwidth,1):
            for ygrid in range(0,self.gridheight,1):
                gobj=self.getobj(xgrid,ygrid)
                if gobj.kind()==kind:
                    items.append((kind,xgrid,ygrid))
        return items

class Wall(View):
    def kind(self):
        return "Wall"
    def draw(self,x,y,width,height):
        pygame.draw.rect(screen,black,(x,y,width,height))
    def handleKey(self,key,pview,x,y):
        pass
def wallplacey(x,spos,epos):
    for y in range(spos,epos+1):
        mainmap.putobj(x,y,Wall())
def wallplacex(y,spos,epos):
    for x in range(spos,epos+1):
        mainmap.putobj(x,y,Wall())

clock=pygame.time.Clock()

mainmap=MapView(30,30)

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

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    key=event.key
                    mainmap.handleKey(key,None,0,0)
        mainmap.handleCycle(None,0,0)
        screen.fill((white))
        mainmap.draw(0,0,300,300)
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
