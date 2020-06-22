from classes.playerSideView import *


lightGray=(220,220,220)

sHeight=100

class SideView(View):
    def __init__(self,players,context):
        self.playerViews=[]
        for player in players:
            playerView=PlayerSideView(player,context)
            self.playerViews.append(playerView)
        self.context=context

    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,lightGray,(x,y,width,height))
        shift=10
        for playerView in self.playerViews:
            playerView.draw(screen,x+10,shift,width-20,sHeight)
            shift+=sHeight+10


    def handleCycle(self,pview,x,y):
        pass

    def handleKey(self,event,pview,x,y):
        pass

    def getHealth(self):
        pass
