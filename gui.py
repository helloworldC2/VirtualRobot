import time
import client
import threading
import random
import Tile
import pygame


pygame.init()
x = random.randint(0,800)
y = random.randint(0,400)
client.login(raw_input("Enter Username: "),x,y)
size = width, height = 800, 400
screen = pygame.display.set_mode(size)
keys = {}
tiles = [0]*(80*40)
def createLevel():
    for x in range(80):
        for y in range(40):
            tiles[x+(y*80)] = 0

def quitGame():
    client.disconnect()
    

def tick():
    global x,y,running,player
    xx=0
    yy=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quitGame()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yy=-1
                print 'w'
            if event.key == pygame.K_s:
                yy=1
                print 's'
            if event.key == pygame.K_a:
                xx=-1
                print 'a'
            if event.key == pygame.K_d:
                xx=1
                print 'd'
    if xx!=0 or yy!=0:
        y+=yy
        x+=xx
        move = [x,y]
        client.move(x,y)
        player.move(move)

def render():
##    for x in range(80):
##        for y in range(40):
##            Tile.tiles[tiles[x+(y*80)]].render()
##            x*=10
##            y*=10
##            client.canvas.coords(tile,x,y,x+10,y+10)
##            client.canvas.update()
    screen.fill((0,0,0))
    
    for p in client.players:
        screen.blit(p.player, (p.x,p.y))

    
    screen.blit(playerImg, (x,y))
    pygame.display.flip()
    pygame.display.update()

#createLevel()
playerImg = pygame.image.load("smashing.jpg")
player = playerImg.get_rect()
pygame.key.set_repeat(1,20)
lastTime = time.time()
lastTimer = time.time()
delta = 0.0
FPS = 60.0
timepertick = 1./FPS
running = True

while running:
    now = time.time()
    delta += (now - lastTime) / timepertick
    lastTime = now

    while delta >= 1:
        tick();
        delta -= 1;
    render()
    
pygame.quit()






        

    
