import Tile

class Entity(object):

	def __init__(self,level,x,y):
		self.level=level
		self.x=x
		self.y=y
		self.centreX = x
		self.centreY = y
		self.ticks = 0
		self.steps = 0
		self.movingDir = 0
		self.limitedToOneTile = False
		self.canPickUpTreasure = False
		self.speed = 1

        """Updates logic associated with entity
        @Params:
                None
        @Retrun:
                None
        """
	def tick(self):
                self.ticks+=1

        """Moves the entity by xa,ya. As long as the entity will not collide
        with anything by doing so. Can only move along one axis at once.
        @Params:
                xa(int): x movement
                ya(int): y movement
        @Return:
                hasCollided(boolean): true if the entity has collided

        """
	def move(self,xa,ya):
		if xa != 0 and ya != 0:
			self.move(xa, 0)
			self.move(0, ya)

			return True

                xa=xa*self.speed
                ya=ya*self.speed
		if not self.hasCollided(xa, ya):
			if ya < 0:
				self.movingDir = 1
			if ya > 0:
				self.movingDir = 0
			if xa < 0:
				self.movingDir = 2
			if xa > 0:
				self.movingDir = 3

			if self.ticks%self.getTileUnder().getSpeed() ==0:
                                self.x += xa
                                self.y += ya
				self.steps+=1


			return False


		return True

        """Returns the tile under the centre of the entity
        @Params:
                None
        @Return:
                tileUnderEntity(Tile): the tile under the entity
        """
	def getTileUnder(self):
		return self.level.getTile(self.centreX>>5, self.centreY>>5)


        """Determins if the entity has collided
        @Params:
                None
        @Return:
                hasCollided(boolean): if the entity has collided
        """
	def hasCollided(self,xa, ya):
		return False
        """Checks tile at x+xa,y+ya and sees if it's solid. Also calls Tile.bump()
        for tiles collided with.
        @Params:
                xa(int): x movement
                ya(int): y movement
                x(int): x position of entity
                y(int): y position of entity
        @Return:
                ifTileIsNotPassable(bool): true if tile is solid or can't be passed
        """
	def isSolidTile(self,xa, ya, x, y):
		lastTile = self.level.getTile((self.x + x) >>5, (self.y + y) >>5)
		nextTile = self.level.getTile((self.x + x + xa) >>5,(self.y + y + ya) >> 5)

		nextTile.bump(self.level,self,(self.x + x + xa) >>5,(self.y + y + ya) >> 5)
		if self.limitedToOneTile and lastTile != nextTile:#like a duck on water (not a simile)
			return True
		if lastTile != nextTile and nextTile.isSolid:
			return True
		for i in self.level.entitiesOnTiles:
			if i == ((self.x + x + xa) >>5,(self.y + y + ya) >> 5):
				return True

		return False
