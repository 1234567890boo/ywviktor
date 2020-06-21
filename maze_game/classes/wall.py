import pygame
from classes.view import *
black=(0,0,0)
class Wall(View):
    def kind(self):
        return "Wall"
    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,black,(x,y,width,height))
    def handleKey(self,key,pview,x,y):
        pass
