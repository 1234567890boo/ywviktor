import pygame,random,time
from pygame.locals import*

pygame.init()

width=100
height=100

screen=pygame.display.set_mode((width,height))

pygame.display.set_caption("Maze Game")

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

clock=pygame.time.Clock()

class Player:
    def __init__(self):
        self.x=10
        self.y=10
        self.width=10
        self.hegiht=10
        self.vel=1
    def draw(self):
        pygame.draw.rect(screen,green,(self.x,self.y,self.height.self.height))

wall=[[1,1,1,1,1,1,1,1,1,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,0,0,0,0,0,0,0,0,1],
      [1,1,1,1,1,1,1,1,1,1]]
screen.fill(white)
for x in range(0,10,1):
        for y in range(0,10,1):
            if wall[x][y]==1:
                pygame.draw.rect(screen,black,(x*10,y*10,10,10))
player=Player()
while True:
    player.draw()
    clock.tick(10)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_SPACE:
              for x in range(0,10,1):
                for y in range(0,10,1):
                    if wall[x][y]==1:
                        pygame.draw.rect(screen,black,(x*10,y*10,10,10))
    pygame.display.update()
