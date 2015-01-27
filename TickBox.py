import pygame
from pygame import *
import sys
import Image
import Button

class tickBox(Button.button):
    def __init__(self,screen,posX,posY,question):
        self.canv = screen
        self.x = posX
        self.y = posY
        self.ask = question
        self.box = pygame.image.load("buttons/box.png")
        self.boxTicked = pygame.image.load("buttons/box1.png")
        self.status = 0
        
        return
        
    
    def collide(self,pos) :
        rect = self.box.get_rect()
        print rect
        if pos[0] >= self.x and pos[0] <= self.x + rect.width and pos[1] >= self.y and pos[1] <= self.y + rect.height :
            return 1
        else :
            return 0

    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.collide(pos) == 1:
                if self.status == 0:
                    self.status = 1
                    print self.status
                    self.blit()
                    return
                elif self.status == 1:
                    self.status = 0
                    print self.status
                    self.blit()
                    return

        return
    
    def getStatus(self):
        return self.status

    def blit(self):
        self.box.convert_alpha()
        self.boxTicked.convert_alpha()
        if self.status == 0:
            self.canv.blit(self.box,(self.x,self.y))                    
        elif self.status == 1:
            self.canv.blit(self.boxTicked,(self.x,self.y))
        pygame.display.update()
        return
