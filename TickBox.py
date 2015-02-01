import pygame
from pygame import *
import sys
import Image
import Button
import Box

class tickBox(Box.box):
    def __init__(self,screen,(posX,posY)):
        super(tickBox,self).__init__(screen,(posX,posY))
        self.box = pygame.image.load("buttons/box.png")
        self.boxTicked = pygame.image.load("buttons/box1.png")
        self.box.convert_alpha()
        self.boxTicked.convert_alpha()
        return

    #returns True if user clicks the box
    def clicked(self):
        pos = pygame.mouse.get_pos()
        if self.collide(pos) == 1:
                if self.status == 0:
                    self.status = 1
                    print self.status
                    self.blit()
                    return 1
                elif self.status == 1:
                    self.status = 0
                    print self.status
                    self.blit()
                    return 1
        else:
            return 0

    #prints the tick box on the screen    
    def blit(self):
        if self.status == 0:
            self.canv.blit(self.box,(self.x,self.y))                    
        elif self.status == 1:
            self.canv.blit(self.boxTicked,(self.x,self.y))
        pygame.display.update()
        return
