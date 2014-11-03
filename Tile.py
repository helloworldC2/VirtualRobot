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
wall = Tile(3,"tiles/wall.png")
wall.setSolid(True)
sand = Tile(4,"tiles/sand.png")
sand.setSpeed(2)
redlight = Tile(5,"tiles/redlight.png")
redlight.setSolid(True)
greenlight = Tile(6,"tiles/greenlight.png")
start1 = Tile(7,"tiles/grass.png")
start2 = Tile(8,"tiles/grass.png")
