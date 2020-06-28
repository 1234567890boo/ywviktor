import pygame
from classes.player import *

class Inventory:
    def getName(self):
        pass
    def action(self):
        pass

class Teleport(Inventory):

    def getName(self):
        return 'Teleport'

    def action(self,pview,x,y):
        player=pview.getobj(x,y)
        lastCommand=player.lastcommand
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

class EnergyDrink(Inventory):
    def __init__(self):
        self.numOfUses=1
    def getName(self):
        return 'Energy Drink'

    def action(self,pview,x,y):
        player = pview.getobj(x, y)
        if player.getActiveInventory().getName():
            player.setEnergy(player.getEnergy()+10)
            self.numOfUses-=1
        if self.numOfUses==0:
            player.inventory[player.inventoryNum].pop()