import random,pygame
from classes.utils import *
from classes.view import *
red=(255,0,0)
class EnemyView(View):
    def kind(self):
        return "Enemy"
    def __init__(self):
        pass
    def draw(self,screen, x,y,width,height):
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
            closestDist=len(get_line(ecoord,closestVisibleCoords))
            for player in playersVisible:
                pcoords=(player[1],player[2])
                dist=len(get_line(ecoord,pcoords))
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
