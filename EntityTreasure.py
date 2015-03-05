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

        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		
		xMin = -1
		xMax = 33
		yMin = -1
		yMax = 33

                if self.isSolidTile(xa, ya, xMin, yMin):
			return True
                if self.isSolidTile(xa, ya, xMin+2, yMin):
			return True
                if self.isSolidTile(xa, ya, xMin+2, yMin+2):
			return True
			
                if self.isSolidTile(xa, ya, xMax, yMin):
			return True
                if self.isSolidTile(xa, ya, xMax-2, yMin):
			return True
                if self.isSolidTile(xa, ya, xMax-2, yMin+2):
                        return True
                        
                if self.isSolidTile(xa, ya, xMax, yMax):
			return True
                if self.isSolidTile(xa, ya, xMax-2, yMax):
			return True
                if self.isSolidTile(xa, ya, xMax-2, yMax-2):
                        return True

                if self.isSolidTile(xa, ya, xMin, yMax):
			return True
                if self.isSolidTile(xa, ya, xMin+2, yMax):
			return True
                if self.isSolidTile(xa, ya, xMin+2, yMax-2):
                        return True

		
		return False
	
        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
                super(EntityTreasure,self).tick()
                self.hasCollided(0,0)
               
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
            
                    
