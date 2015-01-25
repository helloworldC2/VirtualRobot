import Entity
import pygame
import Tile
import Keyboard
import random
import Client
import gui


class Animal(Entity.Entity):


	def __init__(self,level, x, y):
		super(Animal,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.id = len(level.entities)
		self.isSwimming = False
		self.isMoving = False
		self.img = pygame.image.load("animals/crab.png")
		self.basicFont = pygame.font.SysFont(None, 32)
		if Client.isHost == True:
			Client.sendEntity("Crab",x,y)

        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		xMin = 32
		xMax = 38
		yMin = 48
		yMax = 60


		for x in range(xMin,xMax):
			if self.isSolidTile(xa, ya, x, yMin):
				return True

		for x in range(xMin,xMax):
			if self.isSolidTile(xa, ya, x, yMax):
				return True

		for y in range(yMin,yMax):
			if self.isSolidTile(xa, ya, xMin, y):
				return True

		for y in range(yMin,yMax):
			if self.isSolidTile(xa, ya, xMax, y):
				return True
		return False


        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
		global x,y
                super(Animal,self).tick()
		xa = 0
		ya = 0
		self.centreX= self.x+31
		self.centreY= self.y+63
		xx = self.centreX >>5
		yy = self.centreY >>5

                if self.ticks%random.randint(1,100)==0:
                        xa = random.randint(-4,4)

                else:
                        xa = 0

		if xa != 0 or ya != 0:
			self.isMoving = not self.move(xa, ya)
			if Client.isHost == True and gui.isMultiplayer==True:
				Client.moveEntity(self.id,self.x,self.y,self.movingDir,self.isSwimming)
		else:
			self.isMoving = False


		if self.getTileUnder().getId() == Tile.water.getId():
			self.isSwimming = True
		else:
			self.isSwimming = False


        """Renders the entity to the screen
        @Params:
                screen(pygame.Surface): suface to draw to
                xoff(int): x offset of screen
                yoff(int): y offset of screen
        @Return:
                None

        """
	def render(self,screen,xoff,yoff):

                if self.isSwimming:
                        source_area = pygame.Rect((0,0), (self.img.get_width(), self.img.get_height()/2))
                        screen.blit(self.img,(self.x-xoff+16,self.y-yoff+48),source_area)
                else:
                        screen.blit(self.img, (self.x-xoff+16,self.y-yoff+16))
