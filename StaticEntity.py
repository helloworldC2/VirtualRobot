import Entity
import pygame
import Tile
import Keyboard
import random
import Client
import gui
import copy


class StaticEntity(Entity.Entity):


	def __init__(self,level, x, y):
		super(StaticEntity,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.id = len(level.entities)
		self.basicFont = pygame.font.SysFont(None, 32)
		self.blocksPath = True
		self.img = pygame.image.load("tiles/cactus.png")
		self.img = pygame.transform.scale(self.img, (32, 32))
		self.canPlace = True
		


        def CanPlace(self):
                for e in self.level.entities:
                    if e.x == self.x and e.y == self.y:
                        self.canPlace = False
                        return
                if self.blocksPath == True:
                        if self.level.willBlockTreasure(self,self.x>>5,self.y>>5,False):
                                self.canPlace = False
                                return
                self.canPlace = True
                       
        
        def placeInLevel(self):
                if self.canPlace:
                        self.level.entities.append(copy.copy(self))
                        print "Placed Entity"
                        self.CanPlace()
                        print self.x>>5,self.y>>5
                        self.level.willBlockTreasure(self,self.x>>5,self.y>>5,True)#update paths
                        return True
                return False

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
            screen.blit(self.img, (self.x-xoff,self.y-yoff))
