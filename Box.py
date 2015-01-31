import pygame
from pygame import *
import sys
import Image
import Button

class box(object):
    def __init__(self,screen,(posX,posY)):
        self.canv = screen
        self.x = posX
        self.y = posY
        #self.box = pygame.image.load("buttons/box.png")
        #self.boxTicked = pygame.image.load("buttons/box1.png")
        self.status = 0
        
        return
        
    
    def collide(self,pos) :
        rect = self.box.get_rect()
        print rect
        if pos[0] >= self.x and pos[0] <= self.x + rect.width and pos[1] >= self.y and pos[1] <= self.y + rect.height :
            return 1
        else :
            return 0
        
    
    def getStatus(self):
        return self.status


