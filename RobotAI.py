import pygame
import Entity
import Tile
import Keyboard
import random
import scoring


class RobotAI(Entity.Entity):



	def __init__(self,level, x, y,destination,speed,health):
		super(RobotAI,self).__init__(level,x,y)
		
		self.destinations = destination
		self.isSwimming = False
		self.isMoving = False
		self.img = pygame.image.load("robots/robot.png")
		self.basicFont = pygame.font.SysFont(None, 32)
		self.path = None
		self.destination = self.getClosestDestination(self.destinations,True)
		self.x = x
		self.y = y
		self.health = health
                self.canPickUpTreasure = True
		self.score = scoring.Score()
		self.speed = speed
		self.goHome = False
		self.inHand = None
		self.blocksPath = False
		self.isSolid = False
		self.currentRoute = list(self.level.paths[self.destination])
	



        def die(self):
                self.level.entities.remove(self)
                self.level.numAI-=1
                self.level.player.gainPoints(self.speed)
                self.level.player.score+=self.speed
                if self.level.numAI<1:
                        self.level.roundOver()
                self.level.shotgunnedDestinations.remove(self.destination)
        """Gets the closest treasure to robot
        @Params:
                d(list): list of destinations
        @Return:
                destination(tulple): closest treasure
        """
        def getClosestDestination(self,d,remove):
                dest = 0
                distance = 1000000
                for i in d:
                        dis = self.level.getDistance((self.x,self.y),i)
                        nextI = False
                        if dis < distance:
                                for a in self.level.shotgunnedDestinations:
                                        if a == i:
                                                nextI =True
                                                break
                                if nextI:continue
                                distance = dis
                                dest = i
                if dest==0:          
                        for i in d:
                                dis = self.level.getDistance((self.x,self.y),i)
                                if dis < distance:
                                        distance = dis
                                        dest = i
                        
                
##		if remove==True:
##                        d.remove(dest)
                
		self.level.shotgunnedDestinations.append(dest)
                return dest

        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		
		xMin = 31
		xMax = 31
		yMin = 59
		yMax = 60


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

		if self.ticks%10==0:
                        if self.level.paths!=True:
                                for node in self.currentRoute:
                                        if node.pos == (xx,yy):
                                                
                                                nextNode = self.currentRoute.index(node)-1
                                                if self.goHome:nextNode+=2
                                                try:
                                                        self.path = self.currentRoute[nextNode]
                                                        
                                                except:
                                                        if self.goHome:
                                                                self.goHome=False
                                                                self.path=None
                                                        else:
                                                                self.goHome=True
                                                                self.path=None
                                                        print "arrived, or just lost (probably lost)"

                                                
                                                #if self.goHome:self.level.paths[self.destination].remove(self.path)
                                                if nextNode == 0:
                                                        self.goHome=True
                                                        for robot in self.level.entities:
                                                                if robot.canPickUpTreasure==True and robot.destination==self.destination:
                                                                        robot.goHome = True
                                                if nextNode == len(self.currentRoute)-1 and self.goHome:
                                                        self.goHome=False
                                                        self.level.treasuresCollected.append(self.inHand)
                                                        try:
                                                                del self.level.paths[self.destination]
                                                                self.destinations.remove(self.destination)
                                                        except:
                                                                pass
                                                       
                                                        self.destination = self.getClosestDestination(self.destinations,True)
                                                        try:
                                                        	self.currentRoute = list(self.level.paths[self.destination])
                                                        except:
                                                                if gui.endLevel == None:
                                                                        gui.endLevel = gui.Level.Level(32,32)
                                                                        gui.endLevel.loadLevelFromFile("levels/sort.txt")
                                                                        gui.endLevel.entities.append(SorterRobot.SorterRobot(gui.endLevel,6<<5,5<<5))
                                                                else:
                                                                        pass
			
                
##		if self.path==True or self.path==None:
##			self.destination = self.getClosestDestination(self.destinations,True)
##			self.path = self.level.findPath((xx,yy),(self.destination[0]>>5,self.destination[1]>>5))
		if self.path != None and self.path!=True:
                        #print self.path.pos,(xx,yy)
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
