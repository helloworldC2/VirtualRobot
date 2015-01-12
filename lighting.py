class Vector2f(object):

    def __init__(x,y):
        self.x=x
        self.y=y





class Block(object):

	def __init__(x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height




	def getVertices() :

		a = Vector2f(self.x, self.y)
		b = new Vector2f(self.x+self.width, self.y)
		c = new Vector2f(self.x+self.width, self.y+self.height)
		d = new Vector2f(self.x, self.y+self.height)
		return [a,b,c,d]


class Intersect(object):


	def __init__(pos, d, a):
		self.pos = pos
		self.angle = a
		self.distance = d


class Light(object):

	def __init__(location, radius, red, green, blue):
		self.location = location
		self.prevLocation =  None
		self.radius= radius
		self.red = red
		self.green = green
		self.blue = blue
        self.points =[]
        self.walls = []
        self.angles = []
        self.interactions = []


	def hasMoved():
		if prevLocation==null):
			this.prevLocation = new Vector2f(location.x,location.y)
			return True

		if prevLocation.x!=location.x||prevLocation.y!=location.y):
			walls.clear()
			points.clear()
			angles.clear()
			intersects.clear()
			this.prevLocation.set(self.location.x, self.location.y)
			return True

		walls.clear()
		points.clear()
		angles.clear()
		return false
	}
	public void clear(){
		walls.clear()
		points.clear()
		angles.clear()
		intersects.clear()
	}
}
