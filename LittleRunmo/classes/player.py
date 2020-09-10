import pygame,time

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)

class Player:

    def __init__(self,screen):
        self.height=50
        self.width=20
        self.x=250
        self.y=250
        self.screen=screen
        self.xstate=0
        self.ystate=0
        self.grav=5
        self.jumpStrength=30
        self.jumpTime=5

    def draw(self):
        pygame.draw.rect(self.screen,green,(self.y,self.x,self.width,self.height))

    def move(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_w:
                    self.xstate=1

                elif event.key == pygame.K_a:
                    self.ystate = 1

                elif event.key == pygame.K_d:
                    self.ystate=2

            if event.type==pygame.KEYUP:

                if event.key==pygame.K_w:
                    self.xstate=0

                if event.key==pygame.K_a:
                    self.ystate=0

                elif event.key==pygame.K_d:
                    self.ystate=0

        if self.xstate==1:
            self.x=self.x-self.jumpStrength
            self.jumpTime-=1
            if self.jumpTime<=0:
                self.jumptime = 0
                self.jumpStrength-=1
                if self.jumpStrength<=0:
                    self.jumpStrength=0

        if self.ystate==1:
            self.y-=5

        elif self.ystate==2:
            self.y+=5

        self.x=self.x+self.grav
