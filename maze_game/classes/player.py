import pygame
from classes.view import *
class PlayerView(View): #Extends View
    def kind(self):
        return "Player"
    def __init__(self,color,keys):
        self.color=color
        self.keys=keys
        self.activeCommand = ""
    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,self.color,(x,y,width,height))
    def handleKey(self,event,pview,x,y):
        command=self.keys.get(event.key,'')
        if event.type == pygame.KEYDOWN and command!="":
            self.activeCommand=command
        if event.type==pygame.KEYUP and command!="":
            self.activeCommand=""
    def handleCycle(self,pview,x,y):
        if self.activeCommand == 'up':
            pview.moveobj(x, y, x, y - 1)
        if self.activeCommand == 'down':
            pview.moveobj(x, y, x, y + 1)
        if self.activeCommand == 'left':
            pview.moveobj(x, y, x - 1, y)
        if self.activeCommand == 'right':
            pview.moveobj(x, y, x + 1, y)

