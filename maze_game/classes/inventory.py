import pygame
from classes.gridobj import *

black=(0,0,0)

class Inventory(GridObj):
    def __init__(self,context):
        super(GridObj, self).__init__()
        self.context=context

    def kind(self):
        return "Inventory"

    def getName(self):
        pass

    def action(self):
        pass

    def isInventory(self):
        return True

    def canMoveInto(self, obj):
        return True

class Teleport(Inventory):

    def __init__(self,context):
        Inventory.__init__(self,context)

    def getName(self):
        return 'Teleport'

    def action(self,pview,x,y):
        player=pview.getobj(x,y)
        lastCommand = player.lastcommand
        if player.getEnergy()>10:

            if lastCommand=='up':
                pview.moveobj(x,y,x,y-3)
                player.setEnergy(player.getEnergy()-10)

            if lastCommand=='down':
                pview.moveobj(x,y,x,y+3)
                player.setEnergy(player.getEnergy()-10)

            if lastCommand=='left':
                pview.moveobj(x,y,x-3,y)
                player.setEnergy(player.getEnergy()-10)

            if lastCommand=='right':
                pview.moveobj(x,y,x+3,y)
                player.setEnergy(player.getEnergy()-10)

        return True

    def draw(self,screen,x,y,width,height):
        pass

class EnergyDrink(Inventory):
    def __init__(self,context):
        Inventory.__init__(self, context)
        self.numOfUses=2
    def getName(self):
        return 'Energy Drink-'+str(self.numOfUses)

    def action(self,pview,x,y):
        player = pview.getobj(x, y)
        if player.getActiveInventory().getName():
            player.setEnergy(player.getEnergy()+10)
            self.numOfUses -= 1
        if self.numOfUses <= 0:
            return False

        else:
            return True

    def draw(self,screen,x,y,width,height):
        mapInventory=self.context.getMapFont().render("E", True, black)
        screen.blit(mapInventory,(x,y))

class HealthPotion(Inventory):
    def __init__(self,context):
        Inventory.__init__(self,context)
        self.numOfUses=3

    def getName(self):
        return 'Health Potion-'+str(self.numOfUses)

    def action(self,pview,x,y):

        player = pview.getobj(x, y)
        if player.getActiveInventory().getName():
            player.setHealth(player.getHealth()+15)
            self.numOfUses-=1

        if self.numOfUses<=0:
            return False

        else:
            return True

    def draw(self,screen,x,y,width,height):
        mapInventory=self.context.getMapFont().render("H", True, black)
        screen.blit(mapInventory,(x,y))

class Mine(Inventory):
    def __init__(self,context):
        Inventory.__init__(self, context)
        self.numOfUses = 2

    def getName(self):
        return 'Mine-' + str(self.numOfUses)

    def action(self, pview, x, y):
        player = pview.getobj(x, y)
        lastCommand = player.lastcommand

        if self.numOfUses>=1:

            if lastCommand=='up':
                self.numOfUses -= 1

            if lastCommand=='down':
                self.numOfUses -= 1

            if lastCommand=='left':
                self.numOfUses -= 1

            if lastCommand=='right':
                self.numOfUses -= 1

        if self.numOfUses<=0:
            return False

        else:
            return True

    def activeDraw(self,scree,x,y,width,height):
        pygame.draw.rect()
    def draw(self,screen,x,y,width,height):
        mapInventory=self.context.getMapFont().render("M", True, black)
        screen.blit(mapInventory,(x,y))
