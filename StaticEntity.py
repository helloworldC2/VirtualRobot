import Entity
import pygame
import Tile
import Keyboard
import random
import Client
import gui


class StaticEntity(Entity.Entity):


	def __init__(self,level, x, y):
		super(StaticEntity,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.id = len(level.entities)
		self.basicFont = pygame.font.SysFont(None, 32)
		self.blocksPath = False
		

        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		return False


        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
		global x,y
                super(StaticEntity,self).tick()
                if self.entityCollidedWith!=None:
                    print "Bang"
                    self.entityCollidedWith = None
		

        """Renders the entity to the screen
        @Params:
                screen(pygame.Surface): suface to draw to
                xoff(int): x offset of screen
                yoff(int): y offset of screen
        @Return:
                None

        """
	def render(self,screen,xoff,yoff):
            screen.blit(self.img, (self.x-xoff+16,self.y-yoff+16))
