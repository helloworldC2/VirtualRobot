import pygame
tiles = []

class Tile(object):

	

	def __init__(self,iD,imagePath):
		tiles.append(self)
		self.id = iD
		self.img = pygame.image.load(imagePath)
		self.img = pygame.transform.scale(self.img, (32, 32))
		self.isSolid = False

	def render(self,screen,x,y):
		screen.blit(self.img, (x,y))

	def tick(self):
		pass
		#print self,self.isSolid

	def setSolid(self,solid):
		self.isSolid=solid

	def isSolid(self):
		return self.isSolid

	def getId(self):
		return self.id



void = Tile(0,"tiles/void.png")
grass = Tile(1,"tiles/grass.png")
water = Tile(2,"tiles/water.png")
wall = Tile(3,"tiles/wall.png").setSolid(True)
