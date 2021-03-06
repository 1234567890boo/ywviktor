from classes.player import *
from classes.inventory import *

lightGray=(220,220,220)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

class PlayerSideView(View):
    n=0
    def __init__(self,player,context):
        self.player=player
        self.context=context

    def draw(self,screen,x,y,width,height):
        health=self.player.getHealth()
        energy=self.player.getEnergy()
        color=self.player.getColor()
        maxWidth=width-20
        hRatio=health/140
        realHealthWidth=hRatio*maxWidth

        eRatio=energy/140
        realEnergyWidth=eRatio*maxWidth

        playerName=self.context.getPlayerFont().render(self.player.getName(), True, black)
        screen.blit(playerName,(x+5,y-5))

        pHealth = self.context.getBarFont().render("Health"+str(HealthPotion(self.context).numOfUses), True, black)
        pEnergy = self.context.getBarFont().render("Energy" +str(HealthPotion(self.context).numOfUses), True, black)

        activeInventory = self.player.getActiveInventory()
        activeInventoryName = self.context.getBigFont().render(activeInventory.getName(), True, black)

        pygame.draw.rect(screen,color,(x+5,y+10,realHealthWidth,10))
        pygame.draw.rect(screen, color, (x+5,y+25,realEnergyWidth,10))

        screen.blit(pHealth,(x+5,y+10))
        screen.blit(pEnergy,(x+5,y+25))
        screen.blit(activeInventoryName,(x+5,y+40))

