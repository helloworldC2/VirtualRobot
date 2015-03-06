import math
import Entity
import pygame
import Tile
import Keyboard
import Robot_Skin_selector
import VRClient
import scoring
import Client
import gui
import Sounds
import Duck
import StaticEntity

class Player(Entity.Entity):


	def __init__(self,level,username, x, y):
		super(Player,self).__init__(level,x,y)
		self.x = x
		self.y = y
		self.username =username
		self.isSwimming = False
		self.isMoving = False
		self.foundTreasure = False
		SkinTP = Robot_Skin_selector.selskin()
		self.img = [pygame.image.load("robots/GFront.png"),pygame.image.load("robots/GBack.png"),pygame.image.load("robots/GSide.png"),pygame.transform.flip(pygame.image.load("robots/GSide.png"),True,False)]
		self.basicFont = pygame.font.SysFont(None, 32)
		self.xa =0
		self.ya =0
		self.score = scoring.Score()
		self.health = 110
		#self.inHand = Duck.Duck(level,0,0,255,255,255)
		self.inHand = StaticEntity.StaticEntity(level,0,0)
		self.selectedTile = [0,0]
		self.placeCooldown = 0
		self.points = 0
		

        def gainPoints(self,points):
                self.points+=points
                if self.points>1000:self.points=1000
        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		xMin = 14
		xMax = 43
		yMin = 48
		yMax = 62


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
                super(Player,self).tick()
                self.placeCooldown -=1
		self.xa = 0
		self.ya = 0
		self.centreX= self.x+32
		self.centreY= self.y+62                        
		xx = self.centreX >>5
		yy = self.centreY >>5
		soundFXs = Sounds.Audio(False) 

		if Keyboard.keys['w']:
			self.ya=-1
		if Keyboard.keys['s']:
			self.ya=1
		if Keyboard.keys['a']:
			self.xa=-1
		if Keyboard.keys['d']:
			self.xa=1

		if self.xa != 0 or self.ya != 0:
			self.isMoving = not self.move(self.xa, self.ya)
			VRClient.move(self.x,self.y)
			if gui.isMultiplayer == True:
                                Client.move(self.x,self.y,self.movingDir,self.isSwimming)
                    
                        #soundFXs.Plysound(True,False,False,False,False)
		else:
			self.isMoving = False
			soundFXs.Plysound(False,False,False,False,False)

		if self.getTileUnder().getId() == Tile.water.getId()or self.getTileUnder().getId() == Tile.larva.getId() or self.getTileUnder().getId() == Tile.quicksand.getId():
			self.isSwimming = True
		else:
			self.isSwimming = False
		if self.getTileUnder().getId() == Tile.larva.getId()or self.getTileUnder().getId() == Tile.quicksand.getId():
                        if self.health < 0:
                                self.health = 0
                        self.health =  self.health - 1
                        
                if self.health <= 0:
                        gui.gameOver = True
                        gui.defeat = True 

                if self.movingDir == 0:self.selectedTile=[xx,yy+1]#up
                if self.movingDir == 1:self.selectedTile=[xx,yy-3]#down
                if self.movingDir == 2:self.selectedTile=[xx-1,yy-1]#left
                if self.movingDir == 3:self.selectedTile=[xx+1,yy-1]#right
                if self.selectedTile[0]<<5 != self.inHand.x or self.selectedTile[1]<<5!=self.inHand.y:
                        self.inHand.x = self.selectedTile[0]<<5
                        self.inHand.y = self.selectedTile[1]<<5
                        self.inHand.setCanPlace()
                else:
                        self.inHand.x = self.selectedTile[0]<<5
                        self.inHand.y = self.selectedTile[1]<<5
                if Keyboard.keys['e'] and self.placeCooldown <0:
                        if self.inHand.placeInLevel():self.placeCooldown = 20
                        


        """Renders the entity to the screen
        @Params:
                screen(pygame.Surface): suface to draw to
                xoff(int): x offset of screen
                yoff(int): y offset of screen
        @Return:
                None

        """
	def render(self,screen,xoff,yoff):
		image = self.img[self.movingDir]
                if self.isSwimming:
                        source_area = pygame.Rect((0,0), (image.get_width(), image.get_height()/2))
                        screen.blit(image,(self.x-xoff,self.y-yoff+32),source_area)
                else:
                        screen.blit(image, (self.x-xoff,self.y-yoff))
                         
   	 	text = self.basicFont.render(self.username, True, (0,0,0))
   		textpos = text.get_rect(center=(self.x-xoff+30,self.y-yoff-20))
                screen.blit(text, textpos)
                self.inHand.render(screen,xoff,yoff)
                s = pygame.Surface((32,32), pygame.SRCALPHA)   
                                         
                
                if not self.inHand.canPlace:
                        s.fill((255,0,0,128))
                        screen.blit(s, (self.inHand.x-xoff,self.inHand.y-yoff))
                else:
                        s.fill((0,255,0,128))
                        screen.blit(s, (self.inHand.x-xoff,self.inHand.y-yoff))
                
