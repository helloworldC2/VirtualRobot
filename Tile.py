import pygame

tiles = []

class Tile(object):



	def __init__(self,iD,char,imagePath):
		self.id = iD
		self.char =char
		self.img = pygame.image.load(imagePath)
		self.img = pygame.transform.scale(self.img, (32, 32))
		self.isSolid = False
		self.speed = 1.0
		self.children = []
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
	def getChildren(self):
                return self.children
        def setChild(self,child):
                self.children.append(child)
        def hasChildren(self):
                if len(self.children)==0:
                        return False
                return True

void = Tile(0,"v","tiles/void.png")
grass = Tile(1,"g","tiles/grass.png")
water = Tile(2,"w","tiles/water.png")
water.setSpeed(3)
wall = Tile(3,"a","tiles/wall.png")
wall.setSolid(True)
sand = Tile(4,"s","tiles/sand.png")
sand.setSpeed(2)
redlight = Tile(5,"r","tiles/redlight.png")
redlight.setSolid(True)
greenlight = Tile(6,"l","tiles/greenlight.png")
start1 = Tile(7,"S","tiles/start.png")
start2 = Tile(8,"R","tiles/start.png")
amberlight = Tile(9,"m","tiles/amberlight.png")
amberlight.setSolid(True)
Treasure0 = Tile(10,"z","tiles/start.png")
Treasure2 = Tile(11,"x","tiles/start.png")
Treasure3 = Tile(11,"y","tiles/start.png")
Treasure4 = Tile(12,"p","tiles/start.png")
grass.setChild(sand)


def getID(char):
        for t in tiles:
                rand=random.randrange(0,100)
                if rand == 0 and t.hasChildren():
                         return t.getChildren()[0].id
                else:
                         if t.char == char:
                                 return t.id

        return 0
