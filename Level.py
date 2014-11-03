
import random
import Tile
import string



class Level():

	def __init__(self,w,h):
		self.width  = w
		self.height = h
		self.loadLevelFromFile("levels/Arena.txt")
		#self.generateLevel()
		self.ticks=0

        """Populates the tiles list to hold the level data."""
	def loadLevelFromFile(self,path):
		levelF = open(path,'r')
		data = levelF.read()
		x=-1
		y=0
		
		data = string.split(data,"@")
		header  = string.split(data[0],",")
		self.width = int(header[0])
		self.height = int(header[1])
		self.tiles = [0]*(self.width*self.height)
		for i in data[1]:
			if i ==';':
				x=-1
				y+=1
				continue
			try:
				self.setTile(x,y,Tile.tiles[int(i)])
			except:
				pass
			x+=1

	"""Generates a random level"""
	def generateLevel(self):
                for x in range(self.width):
                        for y in range(self.height):
                                self.tiles[x+(y*self.width)] = random.randint(1,4)

	"""Updates the tiles and entities"""
	def tick(self):
                self.ticks+=1
		for tile in Tile.tiles:
			tile.tick()
		for x in range(self.width):
                        for y in range(self.height):
                                if self.getTile(x,y).id== 5 and self.ticks%random.randint(1,1000)==0:
                                        self.setTile(x,y,Tile.greenlight)
                                if self.getTile(x,y).id== 6 and self.ticks%random.randint(1,1000)==0:
                                        self.setTile(x,y,Tile.redlight)

                                
        """Renders tiles and entities
        @Params:
        
        """
	def render(self,screen,xoff,yoff):
		

		for x in range(self.width):
                        for y in range(self.height):
                                self.getTile(x,y).render(screen,(x<<5)-xoff,(y<<5)-yoff)

        """"""
	def setTile(self,x, y, tile):
                if x < 0 or y < 0 or x >= self.width or y >= self.height:
			return
		self.tiles[x+(y*self.width)] = tile.id

	def getTile(self,x,y):

		if 0 > x or x >= self.width or 0 > y or y >= self.height:
			return Tile.void
		return Tile.tiles[self.tiles[x + y * self.width]]

