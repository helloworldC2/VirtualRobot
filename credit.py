import cursor
from cursor import *
import pygame
from pygame.locals import *
import sys
import gui
import Game


def creditMenu(display):
    bg = pygame.image.load("menu/wallpaper.jpg")
    rollingCredit = pygame.image.load("menu/rolling.png").convert_alpha()
    back = pygame.image.load("buttons/back.png").convert_alpha()
    
    bX = 10
    bY = 560
    rX = 200
    rY = 700
    while True :
        pos = pygame.mouse.get_pos()

        if collide(bX,bY,back,pos) :
            pygame.mouse.set_cursor(*cursor.HAND_CURSOR)
        else :
            pygame.mouse.set_cursor(*cursor.ARROW_CURSOR)
        
        for event in pygame.event.get():
            
            if event.type == MOUSEBUTTONDOWN and event.button == 1 :
                if collide(bX,bY,back,pos) :
                    Game.menu1(display)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    pygame.quit()
                    sys.exit()
             if rY<-1200:Game.menu1(display)
        display.blit(bg,(0,0))
        display.blit(rollingCredit,(rX,rY))
        display.blit(back,(bX,bY))
        rY -= 1

        pygame.display.update()

    return    
