import Entity
import pygame
import Tile
import client
import Keyboard


class Player(Entity.Entity):

	
	def __init__(self,level,username, x, y):
		super(Player,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.username =username
		self.isSwimming = False
		self.isMoving = False
		self.img = pygame.image.load("robot.png")
		self.basicFont = pygame.font.SysFont(None, 32)


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
		xa = 0
		ya = 0
		centreX= self.x+32
		centreY= self.y+32
		xx = centreX >>5
		yy = centreY >>5
		
		if Keyboard.keys['w']:
			ya=-1
		if Keyboard.keys['s']:
			ya=1
		if Keyboard.keys['a']:
			xa=-1
		if Keyboard.keys['d']:
			xa=1

		if xa != 0 or ya != 0:
			self.isMoving = not self.move(xa, ya)



		else:
			self.isMoving = False
		
		if self.isMoving:
			client.move(self.x,self.y)

		if self.getTileUnder().getId() == Tile.water.getId():
			self.isSwimming = True
		else:
			self.isSwimming = False

	

	def render(self,screen,xoff,yoff):
		screen.blit(self.img, (self.x-xoff,self.y-yoff))
   	 	text = self.basicFont.render(self.username, True, (0,0,0))
   		textpos = text.get_rect(center=(self.x-xoff+30,self.y-yoff-20))
                screen.blit(text, textpos)


