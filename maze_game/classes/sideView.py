import pygame
from classes.view import *

lightGray=(220,220,220)

class SideView(View):
    def __init__(self):
        pass
    def draw(self,screen,x,y,width,height):
        pygame.draw.rect(screen,lightGray,(x,y,width,height))
    def handleCycle(self,pview,x,y):
        pass
    def handleKey(self,event,pview,x,y):
        pass
