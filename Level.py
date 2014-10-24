
import random
import Tile
import string



class Level():

	def __init__(self,w,h):
		self.width  = w
		self.height = h
		self.tiles = [0]*(w*h)
		self.loadLevelFromFile("levels/lvl1.txt")
		#self.generateLevel()


	def loadLevelFromFile(self,path):
		levelF = open(path,'r')
		data = levelF.read()
		x=0
		y=0
		
		data = string.split(data,"@")
		header  = string.split(data[0],",")
		self.width = int(header[0])
		self.height = int(header[1])
		for i in data[1]:
			if i ==';':
				x=-1
				y+=1
				continue
			if i =='$' or i =='':
				break
			try:
				self.setTile(x,y,Tile.tiles[int(i)])
			except:
				pass
			x+=1
	def generateLevel(self):
                for x in range(self.width):
                        for y in range(self.height):
                                self.tiles[x+(y*self.width)] = random.randint(0,3)
		
	def tick(self):
		for tile in Tile.tiles:
			tile.tick()

	def render(self,screen,xoff,yoff):
		

		for x in range(self.width):
                        for y in range(self.height):
                                self.getTile(x,y).render(screen,(x<<5)-xoff,(y<<5)-yoff)


	def setTile(self,x, y, tile):
                if x < 0 or y < 0 or x >= self.width or y >= self.height:
			return
		self.tiles[x + y * self.width] = tile.getId();

	def getTile(self,x,y):

		if 0 > x or x >= self.width or 0 > y or y >= self.height:
			return Tile.void
		return Tile.tiles[self.tiles[x + y * self.width]]
