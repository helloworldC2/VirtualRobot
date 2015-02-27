import pygame
import Entity
import Tile
import Keyboard
import random
import scoring
import Jobs
import BubbleSort
import HeapSort
import BogoSort
import GeneticSort


class SorterRobot(Entity.Entity):



	def __init__(self,level, x, y):
		super(SorterRobot,self).__init__(level,x,y)
		self.isSwimming = False
		self.isMoving = False
		self.img = pygame.image.load("robots/robot.png")
		self.dest = (x>>5,y>>5)
		self.speed = 32
		self.treasures = []
		for i in range(9):
                        self.treasures.append(random.randint(1,100))
		self.inHand = self.treasures[0]
		self.inContainer = self.treasures[1]
		self.currentJob = None
		self.jobs = BogoSort.createJobs(self.treasures,self)
                #self.jobs = HeapSort.heapSort(self.treasures,len(self.treasures))
                #self.jobs = GeneticSort.geneticSort(self.treasures,self)
		self.jobs[0].doJob(self)
		
		

        

        def goTo(self,index):
            x = (index * 2 + 2)
            if x>10:x=x-10
            y = ((index / 5)+1) * 3
            print x,y
            self.dest = (x,y)

            
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
                super(SorterRobot,self).tick()
                self.currentJob.checkHasDone(self)
                if self.currentJob.jobDone==True:
                    self.jobs.remove(self.currentJob)
                    self.jobs[0].doJob(self)
		xa = 0
		ya = 0
		self.centreX= self.x+31
		self.centreY= self.y+59
		xx = self.centreX >>5
		yy = self.centreY >>5

                
                if self.dest!=None:
                    if xx < self.dest[0]:
                        xa=1
                    if yy < self.dest[1]:
                        ya=1
                    if xx > self.dest[0]:
                        xa=-1
                    if yy > self.dest[1]:
                        ya=-1
                    if xx==self.dest[0] and yy==self.dest[1]:
                        self.currentJob.jobDone = True
                        self.dest=None
                
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
