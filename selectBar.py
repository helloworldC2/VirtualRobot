import pygame
from pygame import *
import sys

class barItem:
    def __init__(self,surface,(posX,posY),kep):
        self.x = posX
        self.y = posY
        self.canvas = surface
        self.img = pygame.image.load(kep)
        self.dragging = 0
        self.placed = False
        
        return

    def place(self):
        self.placed = True 
        return

    def ifPlaced(self):
        return self.placed

    def setOne(self):
        self.dragging = 1

    def setZero(self):
        self.dragging = 0
        

    def setCoord(self,posX,posY):
        self.x = posX
        self.y = posY
        

    def copy(self,image):
        self.x = image.x
        self.y = image.y
        self.canvas = image.canvas
        self.img = image.img
        self.dragging = 0
        return

    def getStatus(self):
        return self.dragging
    
    def blit(self):
        self.img.convert_alpha()
        self.canvas.blit(self.img,(self.x,self.y))
        return

    def scale(self,hossz,magassag):
        self.img = pygame.transform.scale(self.img,(hossz,magassag))
        return

    def collide(self,pos) :
        rect = self.img.get_rect()
        if pos[0] >= self.x and pos[0] <=self.x + rect.width and pos[1] >= self.y and pos[1] <= self.y + rect.height :
            return 1
        else :
            return 0

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.collide(pos) == 1:
            
            return 1
        else:
            return 0
