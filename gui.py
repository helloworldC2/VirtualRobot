import time
import threading
import random
import pygame
import Level
import Keyboard
import client
import Player

def quitGame():
    client.disconnect()
    

def tick():
    global x,y,running,player
    Keyboard.update()
    level.tick()
    player.tick()
    

    

def render():
    screen.fill((0,0,0))
    xoff = player.x - (width/2)
    yoff = player.y - (height/2)
    if xoff < 0:
        xoff = 0
    if xoff > ((level.width << 5) - screen.get_width()):
        xoff = ((level.width << 5) - screen.get_width())
    if yoff < 0:
        yoff = 0
    if yoff > ((level.height << 5) - screen.get_height()):
        yoff = ((level.height << 5) - screen.get_height())

    level.render(screen,xoff,yoff)
    
    for p in client.players:
<<<<<<< HEAD
        p.render(screen,xoff,yoff)

    player.render(screen,xoff,yoff)
=======
        screen.blit(p.player, (p.x-xoff,p.y-yoff))
        text = basicFont.render(p.username, True, (0,0,0))
        textpos = text.get_rect(center=(p.x-xoff+30,p.y-yoff-20))
        screen.blit(text, textpos)

    screen.blit(playerImg, (x-xoff,y-yoff))
    basicFont.render('Hello world!', True, (0,0,0), (0,1,0))
    text = basicFont.render(client.username, True, (0,0,0))
    textpos = text.get_rect(center=(x-xoff+30,y-yoff-20))
    screen.blit(text, textpos)
>>>>>>> origin/master
    pygame.display.flip()
    pygame.display.update()



pygame.init()
pygame.font.init()
basicFont = pygame.font.SysFont(None, 32)
x = random.randint(0,800)
y = random.randint(0,400)
#client.login(raw_input("Enter Username: "),x,y)
client.login("Dave",x,y)

size = width, height = 800, 400
screen = pygame.display.set_mode(size)

level = Level.Level(32,32)
player = Player.Player(level,client.username,x,y)


lastTime = time.time()
lastTimer = time.time()
delta = 0.0
FPS = 60.0
timepertick = 1./FPS
frames = 0
ticks = 0

while Keyboard.running:

    now = time.time()
    delta += (now - lastTime) / timepertick
    lastTime = now

    while delta >= 1:
        ticks+=1
        tick();
        delta -= 1;

    frames+=1
    render()

    if time.time() - lastTimer >= 0:
        lastTimer+=1
        pygame.display.set_caption("Frames:"+ str(frames) +" ticks:"+str(ticks))
        frames=0
        ticks=0

    
pygame.quit()
