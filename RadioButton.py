import TickBox
import pygame

class radioButton(TickBox.tickBox):
    def __init__(self,screen,(posX,posY),question):
        self.canv = screen
        self.x = posX
        self.y = posY
        self.ask = question
        self.box = pygame.image.load("buttons/box.png")
        self.boxTicked = pygame.image.load("buttons/box2.png")
        self.status = 0
        return

    def check(self):
        self.status = 1
        return

    def unCheck(self):
        self.status = 0
        return
