import Animal
import pygame
import Tile
import random
import Client
import gui



def color_surface(surface, red, green, blue):
    pxarray = pygame.PixelArray(surface)
    pxarray.replace((255,255,255), (red,green,blue))
    

class Duck(Animal.Animal):


    def __init__(self,level, x, y,r,g,b):
        super(Animal.Animal,self).__init__(level,x,y)
        self.x = x
        self.y = y
        self.id = len(level.entities)
        self.isSwimming = False
        self.isMoving = False
        self.img = [pygame.image.load("animals/duckfront.png"),pygame.transform.flip(pygame.image.load("animals/duckfront.png"),False,True),pygame.transform.rotate(pygame.image.load("animals/duckfront.png"),-90),pygame.transform.rotate(pygame.image.load("animals/duckfront.png"),90)]
        self.xa =0
        self.ya =0
        self.red = r
        self.green = g
        self.blue = b
        self.breedCoolDown = random.randint(500,5000)
        self.deathTimer = random.randint(2000,20000)
        self.limitedToOneTile = True
        if Client.isHost == True:
            Client.sendEntity("Duck",x,y)


    def canPlace(self):
        if self.level.getTile(self.x>>5,self.y>>5)!=Tile.water:
            return False
        for e in self.level.entitiesOnTiles:
            if e[0] == self.x>>5 and e[1] == self.y>>5:
                return False
        return True
        
    def placeInLevel(self):
        if self.canPlace():
            self.level.entities.append(Duck(self.level,self.x,self.y,self.red,self.green,self.blue))
            print "Placed Duck"
            return True
        return False
        
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

    def mate(self, level, duck):
        if self.breedCoolDown >0 and duck.breedCoolDown >0:return
        for i in range(9):
            if i==4:
                continue#ignore current tile
            x = self.x>>5
            y  = self.y>>5
            dx = (i % 3) -1
            dy = (i / 3) -1
            tile = level.getTile(x+dx,y+dy)
            if tile == Tile.water:
                    duckling = Duck(level,(x+dx)<<5,(y+dy)<<5,(self.red+duck.red)/2,(self.green+duck.green)/2,(self.blue+duck.blue)/2)
                    level.entities.append(duckling)
                    self.breedCoolDown = random.randint(500,5000)
                    duck.breedCoolDown = random.randint(500,5000)
                    print "ducks have bred",self,duck,"born at",duckling.x>>5,duckling.y>>5
                    return
        print "Nowhere for babby to be born :("
           
        

    def die(self):
        print "Duck dies RIP"
        self.level.entities.remove(self)
        
    """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
    def tick(self):
        global x,y
        super(Animal.Animal,self).tick()
        self.breedCoolDown -=1
        self.deathTimer -=1
        if self.deathTimer <0:self.die()
        self.centreX= self.x+16
        self.centreY= self.y+16
        xx = self.centreX >>5
        yy = self.centreY >>5

        
        if self.entityCollidedWith != None:
            try:self.mate(self.level,self.entityCollidedWith)
            except:print "That can't mate with a duck!"
            #print self,self.entityCollidedWith
            self.entityCollidedWith = None
        
        if self.ticks%random.randint(1,500)==0:
            self.xa = random.randint(-1,1)
            self.ya = random.randint(-1,1)


        if self.xa != 0 or self.ya != 0:
            self.isMoving = not self.move(self.xa,self.ya)
            if Client.isHost == True and gui.isMultiplayer == True:
                Client.moveEntity(self.id,self.x,self.y,self.movingDir,self.isSwimming)
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
        
        image.convert_alpha()
        color_surface(image, self.red, self.green, self.blue)
        screen.blit(image, (self.x-xoff,self.y-yoff))
