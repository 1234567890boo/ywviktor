WIDTH=500
HEIGHT=500
import socket
import pygame
from pygame.locals import *
host='0.0.0.0'
port=1234
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))
window=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Cool Python Game")
class Player:
    def __init__(self):
        self.x=WIDTH//2
        self.y=HEIGHT//2
    def moveBy(self,x_distance,y_distance):
        self.x += x_distance
        self.y += y_distance
    def draw(self):
        pygame.draw.rect(window,(255,0,255),(self.x,self.y,20,20))
player1=Player()
while True:
    data=s.recv(8).decode('utf-8')
    data=data.strip()
    print(data)
    player1.x=int(data[0])
    player1.y=int(data[1])
    window.fill((255,255,255))
    player1.draw()
    pygame.display.update()
s.close()
