import pygame
from pygame import *
import sys

class image:
    def __init__(self,surface,posX,posY,kep):
        self.x = posX
        self.y = posY
        self.canvas = surface
        self.img = pygame.image.load(kep)
        return
    
    def blit(self):
        self.img.convert_alpha()
        self.canvas.blit(self.img,(self.x,self.y))
        return

    def scale(self,hossz,magassag):
        self.img.pygame.transform.scale(sel.img,(hossz,magassag))
        return


