import cursor
from cursor import *
import pygame
from pygame.locals import *
import sys
import gui
import Game
import LeaderboardClient


def leaderboardMenu(display):
    bg = pygame.image.load("menu/wallpaper.jpg").convert_alpha()
    back = pygame.image.load("buttons/back.png").convert_alpha()
    font = pygame.font.Font(None, 30)
    stringsToRender = []
    names = []
    scores = []

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
        display.blit(bg,(0,0))
        #draw scores

        for s in range(len(stringsToRender)):
            # newSurf = pygame.Surface((300,100))
            # newSurf.blit(stringsToRender[s],(0,0))
            # newSurf.set_alpha(255)
            # display.blit(newSurf, (200,50+(s*30)))
            display.blit(stringsToRender[s],(300,30+(s*30)))

        display.blit(back,(bX,bY))

        pygame.display.update()
        if len(names)<=0:
            scores = LeaderboardClient.getHighScores();
            names = scores[0]
            scores = scores[1]
            for i in range(len(names)):
                stringsToRender.append(font.render(str(i+1)+": "+str(names[i])+" - "+str(scores[i]),0,(0,0,0)))
    return
