import pygame
import random

"""
Global list of tile objects
"""
tiles = []

"""
Class to hold the attributes of tiles
"""
class Tile(object):


        """Constructor for tile class
        @Params:
                iD(int): id of tile
                char(char): lookup char of tile
                imagePath(string): path to tile texture
        @Return:
                Tile(object)
        """
	def __init__(self,iD,char,imagePath):
		self.id = iD
		self.char =char
		self.img = pygame.image.load(imagePath)
		self.img = pygame.transform.scale(self.img, (32, 32))
		self.isSolid = False
		self.speed = 1.0
		self.children = []
		tiles.append(self)


        """render tiles to screeen
        @Params:
                screen(pygame.surface): pygame surface
                x(int): x co-ordinate of tile
                y(int): y co-ordinate of tile
        @Return:
                None
        """
	def render(self,screen,x,y):
		screen.blit(self.img, (x,y))

        """update tile properties
        @Params:
                None
        @Return:
                None
        """
	def tick(self):
		pass
		#print self,self.isSolid

	"""set the movement cost of the tile
        @Params:
                speed(float): movement cost of tile
        @Return:
                None
        """
	def setSpeed(self,speed):
                self.speed = speed

        """gets the movement cost of the tile
        @Params:
                None
        @Return:
                speed(float): movement cost of tile
        """
        def getSpeed(self):
                return self.speed

        """sets the solidity of the tile
        @Params:
                solid(boolean): solidity of tile
        @Return:
                None
        """
	def setSolid(self,solid):
		self.isSolid=solid

        """gets the solidity of the tile
        @Params:
                None
        @Return:
                solid(boolean): solidity of tile
        """
	def isSolid(self):
		return self.isSolid

        """gets the id of the tile
        @Params:
                None
        @Return:
                id(int): solidity of tile
        """
	def getId(self):
		return self.id


        """gets the tiles children
        @Params:
                        None
        @Return:
                        children(list)
        """
	def getChildren(self):
                return self.children

        """adds child to tiles children
        @Params:
                        child(tile): the tile to add to tiles children
        @Return:
                        None

        """
        def setChild(self,child):
                self.children.append(child)

        """tests whether tile has children
        @Params:
                        None:
        @Return:
                        hasChildren(boolean): true if tile has child
        """
        def hasChildren(self):
                if len(self.children)==0:
                        return False
                return True


"""
Tile creation
"""
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
Treasure3 = Tile(12,"y","tiles/start.png")
Treasure4 = Tile(13,"p","tiles/start.png")
grass.setChild(sand)

"""gets the tile id from the tiles char.
Used to populate level.tiles[]
@Params:
        char(char): character loaded from level file
@Return:
        id(int): id of tile with char of char
"""
def getID(char):
        for t in tiles:
                rand=random.randrange(0,100)
                if rand == 0 and t.hasChildren():
                         return t.getChildren()[0].id
                elif t.char == char:
                        return t.id

        return 0
