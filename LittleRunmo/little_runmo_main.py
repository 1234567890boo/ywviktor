import pygame
from classes.player import *

pygame.init()

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

width,height = 500,500
screen=pygame.display.set_mode((width, height))
clock=pygame.time.Clock()

p1=Player(screen)

while True:
    clock.tick(100)
    screen.fill(white)

    p1.draw()
    p1.move()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()

    pygame.display.update()
