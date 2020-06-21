from classes.player import *

lightGray=(220,220,220)
green=(0,255,0)
blue=(0,0,255)

class PlayerSideView(View):

    def __init__(self,player):
        self.player=player

    def draw(self,screen,x,y,width,height):
        health=self.player.getHealth()
        color=self.player.getColor()
        maxWidth=width-20
        hRatio=health/100
        realWidth=hRatio*maxWidth
        pygame.draw.rect(screen,color,(x+5,y+10,realWidth,10))