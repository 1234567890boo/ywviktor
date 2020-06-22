from classes.player import *

lightGray=(220,220,220)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

class PlayerSideView(View):

    def __init__(self,player,context):
        self.player=player
        self.context=context
    def draw(self,screen,x,y,width,height):
        health=self.player.getHealth()
        color=self.player.getColor()
        maxWidth=width-20
        hRatio=health/140
        realWidth=hRatio*maxWidth
        img=self.context.getFont().render("Player {}:{}", True, blue)
        screen.blit(img,(5,5))
        pygame.draw.rect(screen,color,(x+5,y+10,realWidth,10))