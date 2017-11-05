import time
import random  
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((900,900))
pygame.display.set_caption("Shooting Game")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
screen.fill(red)
class Block(pygame.sprite.Sprite):
    def __init__(self,color):
        super().__init__()
        self.image==pygame.Surface([10,15])
        self.image.fill(color)
        self.rect==self.image.get_rect()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image==pygame.Surface([10,15])
        self.image.fill(color)
        self.rect==self.image.get_rect()
    def update(self):
        pos=pygame.oude.get_pos()
        self.rect.x=pos[0]
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image==pygame.Surface([10,15])
        self.image.fill(color)
        self.rect==self.image.get_rect()
    def update(self):
        self.rect.y-=5
player_list=pygame.sprite.Group()
pygame.display.update()
