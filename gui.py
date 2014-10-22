import time
import client
import threading
import random
import pygame
import Level

def quitGame():
    client.disconnect()
    

def tick():
    global x,y,running,player
    level.tick()
    xx=0
    yy=0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #quitGame()
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                yy=-1
            if event.key == pygame.K_s:
                yy=1
            if event.key == pygame.K_a:
                xx=-1
            if event.key == pygame.K_d:
                xx=1
    if pygame.mouse.get_pressed()[0]:
        if pygame.mouse.get_pos()[0]>x:
            xx=1
        else:
            xx=-1
        if pygame.mouse.get_pos()[1]>y:
            yy=1
        else:
            yy=-1

    if xx!=0 or yy!=0:
        y+=yy
        x+=xx
        move = [x,y]
        client.move(x,y)
        player.move(move)

def render():
    screen.fill((0,0,0))
    xoff = x - (width/2)
    yoff = y - (height/2)
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
        screen.blit(p.player, (p.x-xoff,p.y-yoff))
        text = basicFont.render(p.username, True, (0,0,0))
        textpos = text.get_rect(center=(p.x-xoff+30,p.y-yoff-20))
        screen.blit(text, textpos)

    screen.blit(playerImg, (x-xoff,y-yoff))
    basicFont.render('Hello world!', True, (0,0,0), (0,1,0))
    text = basicFont.render(client.username, True, (0,0,0))
    textpos = text.get_rect(center=(x-xoff+30,y-yoff-20))
    screen.blit(text, textpos)
    pygame.display.flip()
    pygame.display.update()



pygame.init()
pygame.font.init()
basicFont = pygame.font.SysFont(None, 32)
x = random.randint(0,800)
y = random.randint(0,400)
client.login(raw_input("Enter Username: "),x,y)
#client.login("Dave",x,y)

size = width, height = 800, 400
screen = pygame.display.set_mode(size)

level = Level.Level(32,32)

playerImg = pygame.image.load("robot.png")
player = playerImg.get_rect()

pygame.key.set_repeat(1,10)

lastTime = time.time()
lastTimer = time.time()
delta = 0.0
FPS = 60.0
timepertick = 1./FPS
running = True
frames = 0
ticks = 0

while running:

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






        

    
