import time
import threading
import random
import pygame
import Level
import Keyboard
import namepicker
import Player
import Tile
import RobotAI

"""Called when the game closes to remove level.player from server"""
def quitGame():
    client.disconnect()
    
"""Called 60 times a second. Updates the games logic"""
def tick():
    global x,y,running
    Keyboard.update(level)
    level.tick()
    level.player.tick()
    

    
"""Called as many times as possible in the main loop.
Draws all the games graphics"""
def render():
    screen.fill((0,0,0))
    xoff = level.player.x - (width/2)
    yoff = level.player.y - (height/2)
    if xoff < 0:
        xoff = 0
    if xoff > ((level.width << 5) - screen.get_width()):
        xoff = ((level.width << 5) - screen.get_width())
    if yoff < 0:
        yoff = 0
    if yoff > ((level.height << 5) - screen.get_height()):
        yoff = ((level.height << 5) - screen.get_height())

    level.render(screen,xoff,yoff)
    

    level.player.render(screen,xoff,yoff)
    pygame.display.flip()
    


def start(canvas) :
    global screen, height, width, size, level
    screen = canvas
    pygame.init()
    pygame.font.init()
    basicFont = pygame.font.SysFont(None, 32)
    x = random.randint(0,800)
    y = random.randint(0,600)
    


    size = width, height = 800, 600
    #screen = pygame.display.set_mode(size)
    level = Level.Level(32,32)
    for w in range(level.width):
        for h in range(level.height):
            if level.getTile(w,h).getId() == Tile.start1.getId(): 
                startX = h<<5
                startY = w<<5
            if level.getTile(w,h).getId() == Tile.start2.getId(): 
                endX = h<<5
                endY = w<<5
                
    level.entities.append(RobotAI.RobotAI(level,startX,startY,(endX,endY)))
    level.entities.append(RobotAI.RobotAI(level,endX,endY,(startX,startY)))

    username = namepicker.getRandomName()
    level.player = Player.Player(level,username,x,y)


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

