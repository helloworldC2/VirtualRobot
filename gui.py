import time
import subprocess
import threading
import random
import Client
import pygame
import Level
import Keyboard
import namepicker
import Player
import Tile
import RobotAI
import Animal
import Duck
import GuiHUD





"""Called when the game closes to remove level.player from server"""
def quitGame():
    print "Exiting!"
    if isMultiplayer==True:
        Client.disconnect()

"""Called 60 times a second. Updates the games logic"""
def tick():
    global x,y,running
    Keyboard.update(level)
    if Client.isHost == True and isMultiplayer == True:
        level.tick()
    if isMultiplayer == False:
        level.tick()
    level.player.tick()
    hud.tick()



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
    for p in Client.players:
        p.render(screen,xoff,yoff)

    level.player.render(screen,xoff,yoff)
    hud.render(screen,level,basicFont)
    pygame.display.flip()


def populateLevel():
    for w in range(level.width):
        for h in range(level.height):
            if level.getTile(w,h).getId() == Tile.start1.getId():
                startX = h<<5
                startY = w<<5
            if level.getTile(w,h).getId() == Tile.start2.getId():
                endX = h<<5
                endY = w<<5
    #level.entities.append(RobotAI.RobotAI(level,endX,endY,(startX,startY)))
    level.entities.append(Animal.Animal(level,random.randint(0,20),random.randint(0,20)))
    destinations = []
    for i in range(10):
        dx = 0
        dy = 0
        while level.getTile(dx,dy)!=Tile.water:
            dx = random.randint(0,level.width)
            dy = random.randint(0,level.height)
        level.entities.append(Duck.Duck(level,dx<<5,dy<<5))
    dx = 0
    dy = 0
    while level.getTile(dx,dy)!=Tile.water:
        dx = random.randint(0,level.width)
        dy = random.randint(0,level.height)
    destinations.append((dx<<5,dy<<5))
    level.setTile(dx,dy,Tile.landmark1)
    dx = 0
    dy = 0
    while level.getTile(dx,dy)!=Tile.sand:
        dx = random.randint(0,level.width)
        dy = random.randint(0,level.height)
    destinations.append((dx<<5,dy<<5))
    level.setTile(dx,dy,Tile.landmark2)
    dx = 0
    dy = 0
    while level.getTile(dx,dy)!=Tile.grass:
        dx = random.randint(0,level.width)
        dy = random.randint(0,level.height)
    destinations.append((dx<<5,dy<<5))
    level.setTile(dx,dy,Tile.landmark3)

    #level.entities.append(RobotAI.RobotAI(level,startX,startY,destinations))

def startServer(players,console):
    if console==True:
        subprocess.call(['java', '-jar', 'server.jar', players])#with console
    else:
        subprocess.call(['javaw', '-jar', 'server.jar', players])#for no console

def start(canvas) :
    global screen, height, width, size, level,hud,basicFont,isMultiplayer
    screen = canvas
    pygame.init()
    pygame.font.init()
    if False:#true if you want to run a server localy
        t = threading.Thread(target=startServer,args=('3',False))
        t.start()
        time.sleep(1)#bad, but oh well
        print "Server starting"
    basicFont = pygame.font.SysFont(None, 32)
    x = random.randint(0,800)
    y = random.randint(0,600)
    hud = GuiHUD.GuiHUD()
    level = Level.Level(32,32)
    username = namepicker.getRandomName()
    level.player = Player.Player(level,username,x,y)
    isMultiplayer = False #set to true if you want to enanble multiplayer
    if isMultiplayer == True:
        Client.login(username,x,y)



    size = width, height = 800, 600




    while Client.isWaiting == True and isMultiplayer == True:#wait for Client to sync
        pass



    level.loadLevelFromFile("levels/Arena.txt")

    if isMultiplayer == False:
        populateLevel()

    if Client.isHost == True and isMultiplayer == True:
        populateLevel()


    lastTime = time.time()
    lastTimer = time.time()
    delta = 0.0
    FPS = 60.0
    timepertick = 1./FPS
    frames = 0
    ticks = 0
    clock  = pygame.time.Clock()
    while Keyboard.running:
        #doesn't work on pi, but better on pc
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
             #print frames
             pygame.display.set_caption("Frames:"+ str(frames) +" ticks:"+str(ticks))
             frames=0
             ticks=0

##        tick()
##        render()
##        pygame.display.set_caption("FPS:"+str(clock.get_fps()))
##        clock.tick(60)

    quitGame()
    pygame.quit()
