import pygame
from pygame import *
import sys
import TickBox
import textfield
from pygame.locals import *
import Image
import Button

class barItem( Button.button):
    def __init__(self,surface,(posX,posY),kep):
        self.tf1 = textfield.textField(surface,(30,50),(730,30),'',20)
        self.tf2 = textfield.textField(surface,(250,105),(50,30),'',20)
        self.x = posX
        self.y = posY
        self.canvas = surface
        self.im = kep
        self.img = pygame.image.load(kep)
        self.dragging = 0
        self.placed = False
        self.selected = False
        self.edit = False
        self.b = TickBox.tickBox(surface,(400,152))
        return
    #return if the item is selected or not
    def isSelected(self):
        return self.selected
    #if the item was clicked on the bar
    def select(self):
        self.selected = not self.selected
    #place item 
    def place(self):
        self.placed = True 
        return
    #if the item was placed
    def ifPlaced(self):
        return self.placed
    #dragging item
    def setOne(self):
        self.dragging = 1
    #not dragging
    def setZero(self):
        self.dragging = 0
        
    #changing coordinates
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
    #if the item is being dragged or not
    def getStatus(self):
        return self.dragging
