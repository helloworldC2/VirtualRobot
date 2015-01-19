import cursor
from cursor import *
import pygame
from pygame.locals import *
import sys
import Game
import gui

def playMenu(display) :
    bg = pygame.image.load("menu/wallpaper.jpg")
    #bg = pygame.transform.scale(bg,(1107,700))
    bgpart = pygame.image.load("menu/bgpart.jpg")
    
    robot = pygame.image.load("robots/robot.png").convert_alpha()
    robot = pygame.transform.scale(robot,(150,150))
    ai = pygame.image.load("buttons/AI.png").convert_alpha()
    single = pygame.image.load("buttons/Single.png").convert_alpha()
    multi = pygame.image.load("buttons/Multiplayer.png").convert_alpha()

    sound = pygame.image.load("buttons/soundoff.png").convert_alpha()
    soundOn = pygame.image.load("buttons/soundon.png").convert_alpha()
    sound = pygame.transform.scale(sound,(35,50))
    soundOn = pygame.transform.scale(soundOn,(60,50))

    sX = 720
    sY = 540
    
    rX = 50
    rY = 50


    aiWidth = ai.get_width()
    singleWidth = single.get_width()
    multiWidth = multi.get_width()
    
    aiX = 400 - aiWidth/2
    singleX = 400 - singleWidth/2
    multiX = 400 - multiWidth/2

    aiY = 250
    singleY = 350
    multiY = 450

    left = 0

    

    display.blit(bg,(0,0))
    display.blit(robot,(rX,rY))
    display.blit(ai,(aiX,aiY))
    display.blit(single,(singleX,singleY))
    display.blit(multi,(multiX,multiY))
    display.blit(sound,(sX,sY))

    s = 0
    
    while True :
        pos = pygame.mouse.get_pos()
        
        if collide(aiX,aiY,ai,pos) or collide(singleX,singleY,single,pos) or collide(multiX,multiY,multi,pos) or collide(sX,sY,sound,pos) :
            pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
        else :
            pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
        
        if left == 0 and rX <= 500 :
            rX += 1
            if rX == 500 :
                left = 1
        elif left == 1 and rX > 50 :
            rX -= 1
            if rX == 50 :
                left = 0
        
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN and ev.button == 1 :
                if s == 0 and collide(sX,sY,sound,pos) :
                    s = 1
                    display.blit(bg,(0,0))
                    display.blit(robot,(rX,rY))
                    display.blit(ai,(aiX,aiY))
                    display.blit(single,(singleX,singleY))
                    display.blit(multi,(multiX,multiY))
                    display.blit(sound,(sX,sY))
                    display.blit(soundOn,(sX,sY))
                    break
                if s == 1 and collide(sX,sY,sound,pos) :
                    s = 0
                    display.blit(bg,(0,0))
                    display.blit(robot,(rX,rY))
                    display.blit(ai,(aiX,aiY))
                    display.blit(single,(singleX,singleY))
                    display.blit(multi,(multiX,multiY))
                    display.blit(sound,(sX,sY))
                    break
                    
        display.blit(bgpart,(0,0))
        display.blit(robot,(rX,rY)) 

        pygame.display.update()
    


    return
