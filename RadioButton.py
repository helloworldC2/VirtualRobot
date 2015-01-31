import TickBox
import pygame
import Box

class radioButton(TickBox.tickBox,Box.box):
    def __init__(self,screen,(posX,posY)):
        super(radioButton,self).__init__(screen,(posX,posY))
        self.box = pygame.image.load("buttons/box.png")
        self.boxTicked = pygame.image.load("buttons/box2.png")
        
        return

    def check(self):
        self.status = 1
        return

    def unCheck(self):
        self.status = 0
        return
