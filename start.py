import pygame
from pygame.locals import *
import sys

def startgame(canvas) :
    canvas.fill((0,0,0))
    while True :
        for ev in pygame.event.get():
            if ev.type == QUIT :
                pygame.quit()
                sys.exit()
    return
