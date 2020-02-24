import pygame,time,random

pygame.init()

width=500
height=500

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Snake OOP")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

class Food:
    def __init__(self,x,y,width,height):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
    def draw(self):
        pygame.draw.rect(screen,green,(self.x,self.y,self.width,self.height))
food=Food(random.randint(30,470),random.randint(30,470),10,10)
food.draw()
