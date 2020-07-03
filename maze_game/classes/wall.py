import pygame
from classes.gridobj import *
black=(0,0,0)
class Wall(GridObj):
    def kind(self):
        return "Wall"
    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,black,(x,y,width,height))
    def handleKey(self,key,pview,x,y):
        pass
