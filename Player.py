import math
import Entity
import pygame
import Tile
import Keyboard
import Robot_Skin_selector
import VRClient
import scoring


class Player(Entity.Entity):


	def __init__(self,level,username, x, y):
		super(Player,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.username =username
		self.isSwimming = False
		self.isMoving = False
		self.foundTreasure = False
		SkinTP = Robot_Skin_selector.selskin()
		self.img = [pygame.image.load("robots/GFront.png"),pygame.image.load("robots/GBack.png"),pygame.image.load("robots/GSide.png"),pygame.transform.flip(pygame.image.load("robots/GSide.png"),True,False)]
		self.basicFont = pygame.font.SysFont(None, 32)
		self.xa =0
		self.ya =0
		self.score = scoring.Score()



	def hasCollided(self,xa, ya):
		xMin = 14
		xMax = 43
		yMin = 48
		yMax = 62


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


	def tick(self):
                super(Player,self).tick()
		self.xa = 0
		self.ya = 0
		self.centreX= self.x+32
		self.centreY= self.y+62
		xx = self.centreX >>5
		yy = self.centreY >>5

		if Keyboard.keys['w']:
			self.ya=-1
		if Keyboard.keys['s']:
			self.ya=1
		if Keyboard.keys['a']:
			self.xa=-1
		if Keyboard.keys['d']:
			self.xa=1

		if self.xa != 0 or self.ya != 0:
			self.isMoving = not self.move(self.xa, self.ya)
			VRClient.move(self.x,self.y)
		else:
			self.isMoving = False

		if self.getTileUnder().getId() == Tile.water.getId():
			self.isSwimming = True
		else:
			self.isSwimming = False
	       #if self.getTileUnder().getId() == Tile.landmark1.getId()or Tile.landmark2.getId()or Tile.landmark3.getId():
			#self.Treasure = True
               #else:
			#self.Treasure = False
               #if self.Treasure == True:
                      #  pass




	def render(self,screen,xoff,yoff):
		image = self.img[self.movingDir]
                if self.isSwimming:
                        source_area = pygame.Rect((0,0), (image.get_width(), image.get_height()/2))
                        screen.blit(image,(self.x-xoff,self.y-yoff+32),source_area)
                else:
                        screen.blit(image, (self.x-xoff,self.y-yoff))
   	 	text = self.basicFont.render(self.username, True, (0,0,0))
   		textpos = text.get_rect(center=(self.x-xoff+30,self.y-yoff-20))
                screen.blit(text, textpos)
