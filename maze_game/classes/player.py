import pygame
from classes.view import *
class PlayerView(View): #Extends View
    def kind(self):
        return "Player"
    def __init__(self,color,keys):
        self.color=color
        self.keys=keys
    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,self.color,(x,y,width,height))
    def handleKey(self,key,pview,x,y):
         command=self.keys.get(key,'')
         if command=='up':
             pview.moveobj(x,y,x,y-1)
         if command=='down':
             pview.moveobj(x,y,x,y+1)
         if command=='left':
             pview.moveobj(x,y,x-1,y)
         if command=='right':
             pview.moveobj(x,y,x+1,y)
         if command!='':
             return True
         return False

