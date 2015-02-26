import Entity
import pygame
import Tile
import Keyboard
import random
import Client
import gui
import copy


class EntityTreasure(Entity.Entity):


	def __init__(self,level, x, y,value):
		super(EntityTreasure,self).__init__(level,x,y)
		self.value = value
                self.basicFont = pygame.font.SysFont(None, 32)

       


        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
                super(EntityTreasure,self).tick()
                
		

        """Renders the entity to the screen
        @Params:
                screen(pygame.Surface): suface to draw to
                xoff(int): x offset of screen
                yoff(int): y offset of screen
        @Return:
                None

        """
	def render(self,screen,xoff,yoff):
            text = self.basicFont.render(str(self.value), True, (0,0,0))
   	    textpos = text.get_rect(center=(self.x-xoff,self.y-yoff))
            screen.blit(text, textpos)

