import time
import random  
import pygame
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("menu")
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
pygame.draw.rect(screen,blue,(200,200,200,40))
pygame.draw.rect(screen,red,(200,400,200,40))
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",35)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
show_text("TicTacToe",210,200,white)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",35)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
show_text("Ping Pong",210,400,white)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",35)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
show_text("Hello Welcome To The Menu!",75,100,white)
def show_text(msg,x,y,color):
    fontobj=pygame.font.SysFont("freesans",15)
    msgobj=fontobj.render(msg,False,color)
    screen.blit(msgobj,(x,y))
show_text("By:Viktor Gonodanov-Meydbray",200,550,white)
pygame.display.update()
while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            print('Mouse pressed the mouse at ',event.pos)
