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
	def render(self,level,screen,x,y,xx,yy):
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




class WaterTile(Tile):

    def __init__(self,iD,char,imagePaths):

        self.images = []
        for i  in imagePaths:
            img = pygame.image.load(i)
            img = pygame.transform.scale(img, (32, 32))
            self.images.append(img)

        super(self.__class__, self).__init__(iD,char,imagePaths[0])

    def render(self,level,screen,x,y,xx,yy):

        if level.getTile(xx,yy-1)!=water and level.getTile(xx+1,yy)!=water and level.getTile(xx,yy+1)!=water and level.getTile(xx-1,yy)!=water:
            screen.blit(self.images[1], (x,y))#surrounded an all sides
            return
        elif level.getTile(xx,yy-1)!=water and level.getTile(xx+1,yy)!=water and level.getTile(xx-1,yy)!=water:
            screen.blit(self.images[5], (x,y))#surrounded top and sides
            return
        elif level.getTile(xx+1,yy)!=water and level.getTile(xx,yy+1)!=water and level.getTile(xx-1,yy)!=water:
            screen.blit(pygame.transform.rotate(self.images[5], 180), (x,y))#surrounded bottom and sides
            return
        elif level.getTile(xx,yy-1)!=water and level.getTile(xx,yy+1)!=water and level.getTile(xx-1,yy)!=water:
            screen.blit(pygame.transform.rotate(self.images[5], 90), (x,y))#surrounded an left top and bottom
            return
        elif level.getTile(xx,yy-1)!=water and level.getTile(xx+1,yy)!=water and level.getTile(xx,yy+1)!=water:
            screen.blit(pygame.transform.rotate(self.images[5], -90), (x,y))#surrounded an right top and bottom
            return
        elif level.getTile(xx,yy-1)!=water and level.getTile(xx,yy+1)!=water:
            screen.blit(pygame.transform.rotate(self.images[4], -90), (x,y))#surrounded top and bottom
            return
        elif level.getTile(xx-1,yy)!=water and level.getTile(xx+1,yy)!=water:
            screen.blit(self.images[4], (x,y))#surrounded left and right
            return
        elif level.getTile(xx,yy-1)!=water and level.getTile(xx-1,yy)!=water:
            screen.blit(self.images[2], (x,y))#top left
            return
        elif level.getTile(xx,yy-1)!=water and level.getTile(xx+1,yy)!=water:
            screen.blit(pygame.transform.rotate(self.images[2], -90), (x,y))#top right
            return
        elif level.getTile(xx,yy+1)!=water and level.getTile(xx+1,yy)!=water:
            screen.blit(pygame.transform.rotate(self.images[2], 180), (x,y))#bottom right
            return
        elif level.getTile(xx,yy+1)!=water and level.getTile(xx-1,yy)!=water:
            screen.blit(pygame.transform.rotate(self.images[2], 90), (x,y))#bottom left
            return
        elif level.getTile(xx,yy+1)!=water:
            screen.blit(pygame.transform.rotate(self.images[3], 90),(x,y))#bottom
            return
        elif level.getTile(xx,yy-1)!=water:
            screen.blit(pygame.transform.rotate(self.images[3], -90), (x,y))#top
            return
        elif level.getTile(xx-1,yy)!=water:
            screen.blit(self.images[3], (x,y))#left
            return
        elif level.getTile(xx+1,yy)!=water:
            screen.blit(pygame.transform.rotate(self.images[3], 180), (x,y))#right
            return
        else:
            screen.blit(self.images[0], (x,y))#no suroundings
            return



"""
Tile creation
"""
void = Tile(0,"v","tiles/void.png")
grass = Tile(1,"g","tiles/grass.png")
water = WaterTile(2,"w",["tiles/water.png","tiles/waterall.png","tiles/watertl.png","tiles/waterside.png","tiles/watert2side.png","tiles/watert3side.png"])
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
Treasure1 = Tile(10,"z","tiles/TreasureChest.png")
Treasure2 = Tile(11,"x","tiles/sandT.png")
Treasure3 = Tile(12,"y","tiles/waterT.png")
landmark1 = Tile(13,"X","tiles/waterLM.png")
landmark2= Tile(14,"Y","tiles/sandLM.png")
landmark3  = Tile(15,"P","tiles/grassLM.png")
grass2  = Tile(16,"P","tiles/grass2.png")
grass.setChild(grass2)
"""gets the tile id from the tiles char.
Used to populate level.tiles[]
@Params:
        char(char): character loaded from level file
@Return:
        id(int): id of tile with char of char
"""
def getID(char):
        for t in tiles:
                if t.char == char:
                    rand=random.randrange(0,10)
                    if rand == 0 and t.hasChildren():
                        return t.getChildren()[0].id
                    return t.id

        return 0
