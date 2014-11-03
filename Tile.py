import pygame

tiles = []

class Tile(object):

	

	def __init__(self,iD,imagePath):
		self.id = iD
		self.img = pygame.image.load(imagePath)
		self.img = pygame.transform.scale(self.img, (32, 32))
		self.isSolid = False
		self.speed = 1.0
		tiles.append(self)

	def render(self,screen,x,y):
		screen.blit(self.img, (x,y))

	def tick(self):
		pass
		#print self,self.isSolid
	def setSpeed(self,speed):
                self.speed = speed

        def getSpeed(self):
                return self.speed

	def setSolid(self,solid):
		self.isSolid=solid

	def isSolid(self):
		return self.isSolid

	def getId(self):
		return self.id

void = Tile(0,"tiles/void.png")
grass = Tile(1,"tiles/grass.png")
water = Tile(2,"tiles/water.png")
water.setSpeed(3)
wall = Tile(3,"tiles/wall.png").setSolid(True)
sand = Tile(4,"tiles/sand.png").setSpeed(2)
redlight = Tile(5,"tiles/redlight.png").setSolid(True)
greenlight = Tile(6,"tiles/greenlight.png")
