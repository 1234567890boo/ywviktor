import pygame
from classes.inventory import *
from classes.empty import *



class PlayerView(View): #Extends View
    def kind(self):
        return "Player"

    def __init__(self,color,keys,health,energy):
        self.color=color
        self.keys=keys
        self.activeCommand = ""
        self.health=health
        self.energy=energy
        self.lastcommand=''
        self.inventory = [Teleport(),EnergyDrink()]
        self.inventoryNum=0

    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,self.color,(x,y,width,height))

    def handleKey(self,event,pview,x,y):

        command=self.keys.get(event.key,'')
        if command!="":
            if event.type == pygame.KEYDOWN:
                self.activeCommand=command
            if event.type==pygame.KEYUP:
                self.activeCommand=""

    def handleCycle(self,pview,x,y):
        if self.energy>0:
            if self.activeCommand == 'up':
                pview.moveobj(x, y, x, y - 1)
                self.energy-=0.5
                self.lastcommand='up'

            elif self.activeCommand == 'down':
                pview.moveobj(x, y, x, y + 1)
                self.energy -= 0.5
                self.lastcommand = 'down'

            elif self.activeCommand == 'left':
                pview.moveobj(x, y, x - 1, y)
                self.energy -= 0.5
                self.lastcommand = 'left'

            elif self.activeCommand == 'right':
                pview.moveobj(x, y, x + 1, y)
                self.energy -= 0.5
                self.lastcommand = 'right'

            if self.activeCommand == 'shift':
                self.inventoryNum += 1
            if self.inventoryNum>=len(self.inventory):
                self.inventoryNum=0

            if self.activeCommand=='activate':
                self.getActiveInventory().action(pview,x,y)

        for xshift in range(-1,2,1):
            for yshift in range(-1,2,1):
                if pview.getobj(x+xshift,y+yshift).kind() == "Enemy":
                    self.health -= 0.50

        if self.activeCommand=="":
            self.health += 0.25
            self.energy += 1

        if self.health>=100:
            self.health=100

        if self.energy>=100:
            self.energy=100

        if self.health<0:
            pview.putobj(x,y,Empty())
            self.health=0
            self.energy=0

        if self.energy<0:
            self.energy=0


    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def getColor(self):
        return self.color

    def getHealth(self):
        return self.health

    def getEnergy(self):
        return self.energy

    def setEnergy(self,energy):
        self.energy=energy

    def getActiveInventory(self):
        return self.inventory[self.inventoryNum]