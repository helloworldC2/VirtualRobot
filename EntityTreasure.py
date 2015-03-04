import Entity
import pygame
import Tile
import Keyboard
import random
import Client
import gui
import copy


class EntityTreasure(Entity.Entity):


	def __init__(self,level, x, y,value,image=None):
		super(EntityTreasure,self).__init__(level,x,y)
		self.value = value
		self.decrition = "Some treasure"
                self.basicFont = pygame.font.SysFont(None, 32)
                self.image = image
                self.blocksPath = False
                try:
                        self.image = pygame.transform.scale(self.image, (32, 32))
                except:
                        print "nope!",self.image
                print self.x,self.y
       


        def setDescription(self,desc):
                self.description = description

        def setValue(self,value):
                self.value = value
        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
                super(EntityTreasure,self).tick()
                if self.entityCollidedWith!=None:
                        if self.entityCollidedWith.canPickUpTreasure==True:
                            self.entityCollidedWith.inHand = self
                            self.level.entities.remove(self)
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
                if self.image!=None:
                        screen.blit(self.image, (self.x-xoff,self.y-yoff))
                else:    
                        text = self.basicFont.render(str(self.value), True, (0,0,0))
                        textpos = text.get_rect(center=(self.x-xoff,self.y-yoff))
                        screen.blit(text, textpos)
            
                    
