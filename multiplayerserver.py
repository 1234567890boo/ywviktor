WIDTH=500
HEIGHT=500
import pygame
from pygame.locals import *
pygame.init()
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cool Python Game")
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",1234))
s.listen(10)
client, client_address = s.accept()
print("Client has connected with address: {}".format(client_address))
class Player:
    def __init__(self):
        self.x=WIDTH//2
        self.y=HEIGHT//2
    def moveBy(self,x_distance,y_distance):
        self.x += x_distance
        self.y += y_distance
    def draw(self):
        pygame.draw.rect(window,(255,0,0),(self.x,self.y,20,20))
player1=Player()
x=y=0
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==K_UP:
                y=-1
                x=0
            elif event.key==K_DOWN:
                y=1
                x=0
            elif event.key==K_LEFT:
                x=-1
                y=0
            elif event.key==K_RIGHT:
                x=1
                y=0
        if event.type==KEYUP:
            x=y=0
    window.fill((255,255,255))
    player1.draw()
    player1.moveBy(x,y)
    client.sendall(bytes("{} {}\n".format(player1.x,player1.y),"utf-8"))
    pygame.display.update() 
    
