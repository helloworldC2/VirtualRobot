import pygame
import Entity
import Tile
import Keyboard
import random
import scoring


class RobotAI(Entity.Entity):



	def __init__(self,level, x, y,destination):
		super(RobotAI,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.destinations = destination
		self.isSwimming = False
		self.isMoving = False
		self.img = pygame.image.load("robots/robot.png")
		self.basicFont = pygame.font.SysFont(None, 32)
		self.path = None
		self.destination = self.getClosestDestination(self.destinations)
                self.canPickUpTreasure = True
		self.score = scoring.Score()
		self.speed =5

        """Gets the closest treasure to robot
        @Params:
                d(list): list of destinations
        @Return:
                destination(tulple): closest treasure
        """
        def getClosestDestination(self,d):
		print "findind dest"
                dest = 0
                distance = 1000000
                for i in d:
                        dis = self.level.getDistance((self.x,self.y),i)
			print "distance to",i,"=",dis
                        if dis < distance:
                                distance = dis
                                dest = i
		print d
		d.remove(dest)
		print d
		print "Found",dest
                return dest

        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		
		xMin = 31
		xMax = 33
		yMin = 59
		yMax = 61


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


        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
		global x,y
                super(RobotAI,self).tick()
		xa = 0
		ya = 0
		self.centreX= self.x+31
		self.centreY= self.y+59
		xx = self.centreX >>5
		yy = self.centreY >>5

		if self.ticks%30==0:
			if self.level.hasAStarWorker:
				self.level.requestAStar(0,(xx,yy),(self.destination[0]>>5,self.destination[1]>>5))
			else:
				self.path = self.level.findPath((xx,yy),(self.destination[0]>>5,self.destination[1]>>5))

		if self.path==True:
			self.destination = self.getClosestDestination(self.destinations)
			self.path = None
			self.path = self.level.findPath((xx,yy),(self.destination[0]>>5,self.destination[1]>>5))
		if self.path != None and self.path!=True:

                        try:
                                pos = self.path.pos
                                if xx < pos[0]:
                                        xa=1
                                if yy < pos[1]:
                                        ya=1
                                if xx > pos[0]:
                                        xa=-1
                                if yy > pos[1]:
                                        ya=-1
                        except:
                                print "Lost :'("
                                pass

		if xa != 0 or ya != 0:
			self.isMoving = not self.move(xa, ya)
		else:
			self.isMoving = False


		if self.getTileUnder().getId() == Tile.water.getId():
			self.isSwimming = True
		else:
			self.isSwimming = False

                

        """Renders the entity to the screen
        @Params:
                screen(pygame.Surface): suface to draw to
                xoff(int): x offset of screen
                yoff(int): y offset of screen
        @Return:
                None

        """
	def render(self,screen,xoff,yoff):

                if self.isSwimming:
                        source_area = pygame.Rect((0,0), (self.img.get_width(), self.img.get_height()/2))
                        screen.blit(self.img,(self.x-xoff,self.y-yoff+32),source_area)
                else:
                        screen.blit(self.img, (self.x-xoff,self.y-yoff))
