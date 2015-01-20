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

	def tick(self):
                self.ticks+=1

	def move(self,xa,ya):
		if xa != 0 and ya != 0:
			self.move(xa, 0)
			self.move(0, ya)

			return True

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


	def getTileUnder(self):
		return self.level.getTile(self.centreX>>5, self.centreY>>5)


	def hasCollided(self,xa, ya):
		return False

	def isSolidTile(self,xa, ya, x, y):
		lastTile = self.level.getTile((self.x + x) >>5, (self.y + y) >>5)
		nextTile = self.level.getTile((self.x + x + xa) >>5,(self.y + y + ya) >> 5)
		nextTile.bump(self.level,(self.x + x + xa) >>5,(self.y + y + ya) >> 5)
		if self.limitedToOneTile and lastTile != nextTile:#like a duck on water
			return True
		if lastTile != nextTile and nextTile.isSolid:
			return True
		for i in self.level.entitiesOnTiles:
			if i == ((self.x + x + xa) >>5,(self.y + y + ya) >> 5):
				return True

		return False
