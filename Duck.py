import Animal
import pygame
import Tile
import random


class Duck(Animal.Animal):


    def __init__(self,level, x, y):
        super(Animal.Animal,self).__init__(level,x,y)
        self.x = x
        self.y = y
        self.isSwimming = False
        self.isMoving = False
        self.img = [pygame.image.load("animals/duckfront.png"),pygame.transform.flip(pygame.image.load("animals/duckfront.png"),False,True),pygame.transform.rotate(pygame.image.load("animals/duckfront.png"),-90),pygame.transform.rotate(pygame.image.load("animals/duckfront.png"),90)]
        self.basicFont = pygame.font.SysFont(None, 32)
        self.xa =0
        self.ya =0
        self.limitedToOneTile = True

    """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
    def hasCollided(self,xa, ya):
        xMin = 0
        xMax = 32
        yMin = 16
        yMax = 32


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
        super(Animal.Animal,self).tick()
        self.centreX= self.x+16
        self.centreY= self.y+16
        xx = self.centreX >>5
        yy = self.centreY >>5

        if self.ticks%random.randint(1,500)==0:
            self.xa = random.randint(-1,1)
            self.ya = random.randint(-1,1)


        if self.xa != 0 or self.ya != 0:
            self.isMoving = not self.move(self.xa,self.ya)
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
        image = self.img[self.movingDir]

        screen.blit(image, (self.x-xoff,self.y-yoff))
