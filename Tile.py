#import RobotAI
import pygame
import random
import scoring
import Config
import EmailClient
import threading
import gui
import Sounds


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
        """returns true if the tile is the same as tile at x,y or
        tile at x,y is solid
        @Params:
                level(level): the level object
                x(int) x pos of tile
                y(int): y pos of tile
        @Return:
                bool: solid or self
        """
        def thisOrSolid(self,level,x,y):
            t = level.getTile(x,y)
            if t.isSolid:
                return True
            if t == self:
                return True
            return False

        def bump(self,level,entity,x,y):
                if entity.canPickUpTreasure==True:
                        if self == landmark1:
                                level.setTile(x,y,Treasure3)
                                gui.removeTreasure((x<<5,y<<5))
                                entity.score.incrementScore()
                                if entity == level.player:
                                        t = threading.Thread(target=EmailClient.sendRandomEmail,args=(Config.config['email'],))
                                        t.start()
                                self.updateAI(level,x,y)
                        if self == landmark2:
                                level.setTile(x,y,Treasure2)
                                gui.removeTreasure((x<<5,y<<5))
                                entity.score.incrementScore()
                                if entity == level.player:
                                        t = threading.Thread(target=EmailClient.sendRandomEmail,args=(Config.config['email'],))
                                        t.start()
                                self.updateAI(level,x,y)
                        if self == landmark3:
                                level.setTile(x,y,Treasure1)
                                gui.removeTreasure((x<<5,y<<5))
                                entity.score.incrementScore()
                                if entity == level.player:
                                        t = threading.Thread(target=EmailClient.sendRandomEmail,args=(Config.config['email'],))
                                        t.start()
                                self.updateAI(level,x,y)
                        if self == cactus and entity == level.player:
                                sounFXs = Sounds.Audio(False) 
                                sounFXs.Plysound(False,True,False,False,False)
                                entity.b -= 1 
                                print "Ouch!"
                                if entity.xa>0:
                                        entity.x-=4
                                if entity.xa<0:
                                        entity.x+=4
                                if entity.ya>0:
                                        entity.y-=4
                                if entity.ya<0:
                                        entity.y+=4
        def updateAI(self,level,x,y):
                for e in level.entities:
                        if e.canPickUpTreasure:     
                                for d in e.destinations:
                                        print d[0],x<<5, d[1],y<<5
                                        if d[0]==x<<5 and d[1]==y<<5:
                                                e.destinations.remove(d)
                                                print "Removed",d
                                if len(e.destinations) >0:
                                        e.destination = e.getClosestDestination(e.destinations,False)
                                        print "Changed destination!"
                                else:
                                        gui.gameOver=True

class WaterTile(Tile):

    def __init__(self,iD,char,imagePaths):

        self.images = []
        for i  in imagePaths:
            img = pygame.image.load(i)
            img = pygame.transform.scale(img, (32, 32))
            self.images.append(img)

        super(self.__class__, self).__init__(iD,char,imagePaths[0])

    def render(self,level,screen,x,y,xx,yy):

        if not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx+1,yy) and not self.thisOrSolid(level,xx,yy+1) and not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(self.images[1], (x,y))#surrounded an all sides
            return
        elif not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx+1,yy) and not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(self.images[5], (x,y))#surrounded top and sides
            return
        elif not self.thisOrSolid(level,xx+1,yy) and not self.thisOrSolid(level,xx,yy+1) and not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx-1,yy).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[5], 180), (x,y))#surrounded bottom and sides
            return
        elif not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx,yy+1) and not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx-1,yy).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[5], 90), (x,y))#surrounded an left top and bottom
            return
        elif not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx+1,yy) and not self.thisOrSolid(level,xx,yy+1):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[5], -90), (x,y))#surrounded an right top and bottom
            return
        elif not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx,yy+1):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[4], -90), (x,y))#surrounded top and bottom
            return
        elif not self.thisOrSolid(level,xx-1,yy) and not self.thisOrSolid(level,xx+1,yy):
            screen.blit(level.getTile(xx-1,yy).img, (x,y))
            screen.blit(self.images[4], (x,y))#surrounded left and right
            return
        elif not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(self.images[2], (x,y))
            return
        elif not self.thisOrSolid(level,xx,yy-1) and not self.thisOrSolid(level,xx+1,yy):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[2], -90), (x,y))#top right
            return
        elif not self.thisOrSolid(level,xx,yy+1) and not self.thisOrSolid(level,xx+1,yy):
            screen.blit(level.getTile(xx+1,yy).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[2], 180), (x,y))#bottom right
            return
        elif not self.thisOrSolid(level,xx,yy+1) and not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx-1,yy).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[2], 90), (x,y))#bottom left
            return
        elif not self.thisOrSolid(level,xx,yy+1):
            screen.blit(level.getTile(xx,yy+1).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[3], 90),(x,y))#bottom
            return
        elif not self.thisOrSolid(level,xx,yy-1):
            screen.blit(level.getTile(xx,yy-1).img, (x,y))
            screen.blit(pygame.transform.rotate(self.images[3], -90), (x,y))#top
            return
        elif not self.thisOrSolid(level,xx-1,yy):
            screen.blit(level.getTile(xx-1,yy).img, (x,y))
            screen.blit(self.images[3], (x,y))#left
            return
        elif not self.thisOrSolid(level,xx+1,yy):
            screen.blit(level.getTile(xx+1,yy).img, (x,y))
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
grass3 = Tile(17,"-","tiles/grass3.png")
cactus = Tile(18,"-","tiles/cactus.png")
sandbush = Tile(19,"-","tiles/sandbush.png")
larva = WaterTile(20,"L",["tiles/larva.png","tiles/waterall.png","tiles/larval.png","tiles/larvaside.png","tiles/larva2side.png","tiles/larva3side.png"])
larva.setSpeed(2)
cactus.setSolid(True)
grass.setChild(grass2)
grass.setChild(grass3)
sand.setChild(cactus)
sand.setChild(sandbush)
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
                    rand=random.randrange(0,20)
                    if rand == 0 and t.hasChildren():
                        return t.getChildren()[random.randint(0,len(t.getChildren())-1)].id
                    return t.id

        return 0
