import time
import random  
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((800,800))
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
        self.image=pygame.Surface([10,15])
        self.image.fill(color)
        self.rect=self.image.get_rect()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([25,25])
        self.image.fill(blue)
        self.rect=self.image.get_rect()
    def update(self):
        pos=pygame.mouse.get_pos()
        self.rect.x=pos[0]
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image=pygame.Surface([10,15])
        self.image.fill(green)
        self.rect=self.image.get_rect()
    def update(self):
        self.rect.y-=5
player_list=pygame.sprite.Group()
block_list=pygame.sprite.Group()
bullet_list=pygame.sprite.Group()
for i in range(100):
    block=Block(blue)
    block.rect.x=random.randrange(790)
    block.rect.y=random.randrange(790)
    block_list.add(block)
    player_list.add(block)
player=Player()
player_list.add(player)
player.rect.y=750
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            bullet=Bullet()
            bullet.rect.x=player.rect.x
            bullet.rect.y=player.rect.y
            player_list.add(bullet)
            bullet_list.add(bullet)
        player_list.update()
        for bullet in bullet_list:
            hit_list=pygame.sprite.spritecollide(bullet,block_list,True)
            for block in hit_list:
                bullet_list.remove(bullet)
                player_list.remove(bullet)
            if bullet.rect.y<=0:
                bullet_list.remove(bullet)
                player_list.remove(bullet)
    screen.fill(red)
    player_list.draw(screen)
    pygame.display.update()
