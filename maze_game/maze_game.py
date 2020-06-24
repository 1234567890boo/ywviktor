from classes.enemy import *
from classes.wall import *
from classes.sideView import *
from classes.playerSideView import *
from classes.mapView import *
from classes.context import *

width=520
height=300

red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)


        
clock=pygame.time.Clock()

mainmap=MapView(30,30)


def wallplacey(x,spos,epos):
    for y in range(spos,epos+1):
        mainmap.putobj(x,y,Wall())
def wallplacex(y,spos,epos):
    for x in range(spos,epos+1):
        mainmap.putobj(x,y,Wall())


wallplacex(0,0,29)
wallplacex(29,0,29)
wallplacey(0,0,29)
wallplacey(29,0,29)

wallplacex(6,1,15)
wallplacex(24,5,23) 
wallplacey(11,1,1)

def placeRandom(pview,obj):
    randomx=random.randint(1,28)
    randomy=random.randint(1,28)
    while pview.getobj(randomx,randomy).kind()!="Empty":
        randomx=random.randint(1,28)
        randomy=random.randint(1,28)
    pview.putobj(randomx,randomy,obj)
    
placeRandom(mainmap,PlayerView(green,{pygame.K_w:'up',pygame.K_s:'down',pygame.K_a:'left',pygame.K_d:'right'},100,100))
placeRandom(mainmap,PlayerView(blue,{pygame.K_i:'up',pygame.K_k:'down',pygame.K_j:'left',pygame.K_l:'right'},100,100))

playerDesc=mainmap.get_items("Player")
players=[]
c = 1
for p in playerDesc:
    p[0].setName("Player "+str(c))
    players.append(p[0])
    c+=1
gameContext=Context()

sideView=SideView(players,gameContext)
# testView=PlayerSideView(playerDesc[0][0])

for n in range(1,20):
        placeRandom(mainmap,EnemyView())


screen = pygame.display.set_mode((width, height))

while True:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
                    mainmap.handleKey(event, None,0,0)
        mainmap.handleCycle(None,0,0)
        screen.fill((white))
        mainmap.draw(screen,0,0,300,300)
        sideView.draw(screen,300,0,300,550)
        clock.tick(7)
        pygame.display.flip()
