import pygame
from classes.empty import *
from classes.player import *

class inventory(player):
    def teleport(self,x,y,pview):
        if self.activeCommand == 'teleport':
            if self.lastcommand == 'up':
                pview.moveobj(x, y, x, y - 3)

            if self.lastcommand == 'down':
                pview.moveobj(x, y, x, y + 3)

            if self.lastcommand == 'right':
                pview.moveobj(x, y, x + 3, y)

            if self.lastcommand == 'left':
                pview.moveobj(x, y, x - 3, y)
            self.energy -= 10


if self.activeCommand != "":
    self.energy -= 0.5