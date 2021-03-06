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
import SorterRobot
import Animal
import Duck
import GuiHUD
import Sounds
import Config
import camera



defeat = False
gameOver = False
scorePosted = False
treasureLocations = []#master list that holds the locations of all the treasures
#holds them in the format (x,y)  !!!!Make sure to update when treasure is found or placed!!!!


def removeTreasure(loc):
    for t in treasureLocations:
        if t == loc:
            treasureLocations.remove(t)
    if len(treasureLocations)==0:
        gameOver = True
    
        
"""Called when the game closes to remove level.player from server"""
def quitGame():
    print "Exiting!"
    Config.saveConfig()
    if isMultiplayer==True:
        Client.disconnect()

"""Called 60 times a second. Updates the games logic"""
def tick():
    global x,y,running,gameOver,scorePosted,isMultiplayer
    Keyboard.update(level)
    if timer == 30:
        soundFXs = Sounds.Audio(False) 
        soundFXs.Plysound(False,False,False,False,True)

    if gameOver == True and scorePosted==False:
        level.player.score.happyDucks(level.player.username)
        scorePosted = True
        
    if Client.isHost == True and isMultiplayer == True:
        level.tick()
        endLevel.tick()
    if isMultiplayer == False and gameOver==False:
        level.tick()
        if endLevel!=None:endLevel.tick()
    if gameOver==False and level.player!=None:
        level.player.tick()
    
    if level.player == None:
        level.cam.tick()
    
    hud.tick(timer,xoff,yoff,level)



"""Called as many times as possible in the main loop.
Draws all the games graphics"""
def render():
    screen.fill((0,0,0))
    global xoff,yoff
    xoff = level.cam.x
    yoff = level.cam.y
    
    if level.player!=None:
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
    if endLevel!=None:endLevel.render(screen,-level.player.x+(6<<5)+xoff,-level.player.y+(10<<5)+yoff)
    if level.player!=None:
        level.player.render(screen,xoff,yoff)
    
    hud.render(screen,level,basicFont,xoff,yoff)
    pygame.display.flip()


def populateLevel():
    for i in range(0):
        dx = 0
        dy = 0
        while level.getTile(dx,dy)!=Tile.water:
            dx = random.randint(0,level.width)
            dy = random.randint(0,level.height)
        level.entities.append(Duck.Duck(level,dx<<5,dy<<5,random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    dx = 0
    dy = 0
    for i in range(2):
        while level.getTile(dx,dy)!=Tile.water:
            dx = random.randint(0,level.width)
            dy = random.randint(0,level.height)
        treasureLocations.append((dx<<5,dy<<5))
        level.setTile(dx,dy,Tile.Treasure1)
        dx = 0
        dy = 0
        while level.getTile(dx,dy)!=Tile.sand:
            dx = random.randint(0,level.width)
            dy = random.randint(0,level.height)
        treasureLocations.append((dx<<5,dy<<5))
        level.setTile(dx,dy,Tile.Treasure2)
        dx = 0
        dy = 0
        while level.getTile(dx,dy)!=Tile.grass:
            dx = random.randint(0,level.width)
            dy = random.randint(0,level.height)
        treasureLocations.append((dx<<5,dy<<5))
        level.setTile(dx,dy,Tile.Treasure3)

   
    #for i in range(1):
        #level.entities.append(RobotAI.RobotAI(level,32,32,treasureLocations,difficulty))

def startServer(players,console):
    if console==True:
        subprocess.call(['java', '-jar', 'server.jar', players])#with console
    else:
        subprocess.call(['javaw', '-jar', 'server.jar', players])#for no console

def start(canvas,multiplayer=False,runServer=False,AI=False,nAI=1,diff=4) :
    global screen, player, height, width, size, level,hud,basicFont,isMultiplayer,hasAI,numAI,difficulty,timer,endLevel
    screen = canvas
    pygame.init()
    pygame.font.init()
    if runServer:#true if you want to run a server localy
        t = threading.Thread(target=startServer,args=('3',False))
        t.start()
        time.sleep(1)#bad, but oh well
        print "Server starting"
    basicFont = pygame.font.SysFont(None, 32)
    x = 32*16
    y = 32*16
    hud = GuiHUD.GuiHUD(screen)
    level = Level.Level(32,32)
    
    endLevel = None
    #endLevel = Level.Level(32,32)
    username = Config.config["name"]
    player = Player.Player(level,username,x,y)
    #level.player = player
    isMultiplayer = multiplayer
    hasAI = AI
    numAI = nAI
    difficulty = diff
    if isMultiplayer == True:
        Client.login(username,x,y)



    size = width, height = 800, 600




    while Client.isWaiting == True and isMultiplayer == True:#wait for Client to sync
        pass



    level.loadLevelFromFile("levels/Arena.txt")
    #endLevel.loadLevelFromFile("levels/sort.txt")
    #endLevel.entities.append(SorterRobot.SorterRobot(endLevel,6<<5,5<<5))
    #if isMultiplayer == False:
        #populateLevel()

   # if Client.isHost == True and isMultiplayer == True:
      #  populateLevel()


    lastTime = time.time()
    lastTimer = time.time()
    delta = 0.0
    FPS = 60.0
    timepertick = 1./FPS
    frames = 0
    ticks = 0
    timer = 0
    clock  = pygame.time.Clock()
    while Keyboard.running:
        #doesn't work on pi, but better on pc
         now = time.time()
         delta += (now - lastTime) / timepertick
         lastTime = now

         while delta >= 1:
             ticks+=1
             timer+=1
             tick()
             delta -= 1

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
