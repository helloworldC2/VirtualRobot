
import random
import Tile
import string
import math
import RobotAI
import socket
import threading


class Level():

	def __init__(self,w,h):
		self.width  = w
		self.height = h
		self.loadLevelFromFile("levels/Arena.txt")
		#self.generateLevel()
		self.ticks=0
		self.player = None
		self.entities = []
		self.entities.append(RobotAI.RobotAI(self,500,500))
		self.hasAStarWorker = False
		#self.workers = 1	#number of worker
		#self.addr_list = []	#list of client addresses and connections
		#self.HOST = ''
		#self.PORT = 1337
		#self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#self.s.bind((self.HOST, self.PORT))
		#self.sendTilesToAStarWorker()
		#t = threading.Thread(target=self.listenForResult)
		#t.start()


        """Populates the tiles list to hold the level data."""
	def loadLevelFromFile(self,path):
		levelF = open(path,'r')
		data = levelF.read()
		x=-1
		y=0

		data = string.split(data,"@")
		header  = string.split(data[0],",")
		self.width = int(header[0])
		self.height = int(header[1])
		self.tiles = [0]*(self.width*self.height)
		for i in data[1]:
			if i ==';':
				x=-1
				y+=1
				continue
			try:
				self.setTile(x,y,Tile.tiles[int(i)])
			except:
				pass
			x+=1

	"""Generates a random level"""
	def generateLevel(self):
                for x in range(self.width):
                        for y in range(self.height):
                                self.tiles[x+(y*self.width)] = random.randint(1,4)

	"""Updates the tiles and entities"""
	def tick(self):
                self.ticks+=1
                for e in self.entities:
			e.tick()
		for tile in Tile.tiles:
			tile.tick()
		for x in range(self.width):
                        for y in range(self.height):
                                if self.getTile(x,y).id== 5 and self.ticks%random.randint(1,1000)==0:
                                        self.setTile(x,y,Tile.greenlight)
                                if self.getTile(x,y).id== 6 and self.ticks%random.randint(1,1000)==0:
                                        self.setTile(x,y,Tile.redlight)


        """Renders tiles and entities
        @Params:

        """
	def render(self,screen,xoff,yoff):


		for x in range(self.width):
                        for y in range(self.height):
                                self.getTile(x,y).render(screen,(x<<5)-xoff,(y<<5)-yoff)
                for e in self.entities:
                        e.render(screen,xoff,yoff)

        """"""
	def setTile(self,x, y, tile):
                if x < 0 or y < 0 or x >= self.width or y >= self.height:
			return
		self.tiles[x+(y*self.width)] = tile.id

	def getTile(self,x,y):

		if 0 > x or x >= self.width or 0 > y or y >= self.height:
			return Tile.void
		return Tile.tiles[self.tiles[x + y * self.width]]

	def getDistance(self,a,b):
		dx = a[0] - b[0]
		dy = a[1] - b[0]
		return math.sqrt(dx*dx+dy*dy)

	def inList(self,l,i):
		for node in l:
			if node.pos == i:
				return True

		return False



	def findPath(self,start,goal):
		openList = []
		closedList = []
		currentNode = Node(start,None,0,self.getDistance(start,goal))
		openList.append(currentNode)
		while len(openList) >0:
			sorted(openList,key=lambda i: i.totalCost)
			currentNode = openList[0] #only use node with lowest cost
			if currentNode.pos==goal:
				path = []
				while currentNode.parent != None:#goes until reaches the start
					path.append(currentNode)
					currentNode = currentNode.parent
				openList = []
				closedList = []
				return path
			openList.remove(currentNode)
			closedList.append(currentNode)
			for i in range(9):
				if i==0:
					continue#ignore current tile
				x = currentNode.pos[0]
				y  = currentNode.pos[1]
				dx = (i % 3) -1
				dy = (i / 3) -1
				tile = self.getTile(x+dx,y+dy)
				if tile == None or tile == Tile.void:
					continue
				if tile.isSolid:
					#print 'solid'
					continue
				tilePos = (x+dx,y+dy)
				costSoFar = currentNode.costSoFar + self.getDistance(currentNode.pos,tilePos)
				costSoFar*=tile.getSpeed()
				distanceToEnd = self.getDistance(tilePos,goal)
				node = Node(tilePos,currentNode,costSoFar,distanceToEnd)
				if self.inList(closedList,tilePos) and costSoFar >= node.costSoFar: #checks if node has already been used,or if you are going backwards
					continue
				if not self.inList(openList,tilePos) or costSoFar < node.costSoFar:#only add if it's not alredy there
					openList.append(node)




		print "No path :("
		return None

	def sendTilesToAStarWorker(self):
		self.s.listen(self.workers)	#Listens for (n) number of client connections
		print 'Waiting for client...'
		for i in range(self.workers):	#Connects to all clients
			conn, addr = self.s.accept()	#Accepts connection from client
			print 'Connected by', addr
			self.addr_list.append((conn,addr))	#Adds address to address list
		for i in range(self.workers):	#Converts array section into string to be sent
			data = self.tiles
			data.append(self.width)
			data.append(self.height)
			arraystring = repr(data)
			conn.sendto(arraystring , self.addr_list[i][1])	#Sends array string
			print 'Tiles sent to worker'
		self.hasAStarWorker = True

	def requestAStar(self,workerID,start,goal):
		arraystring = repr([start,goal])
		self.addr_list[workerID][0].sendto( arraystring , self.addr_list[workerID][1] )	#Sends array string
		print 'requesting A*!'

	def listenForResult(self):
		while True:
			for i in range(self.workers):	#Receives sorted sections from each client
				arraystring = ''
				print 'Receiving data from clients...'
				while 1:
					data = self.addr_list[i][0].recv(4096)	#Receives data in chunks
					print "Recieved:",data
					data = eval(data)
					self.entities[i].path = [Node((int(data[0]),int(data[1])),None,0,0)]


class Node(object):

	def __init__(self,pos,parent,costSoFar,distanceToEnd):
		self.pos = pos
		self.parent = parent
		self.costSoFar = costSoFar
		self.distanceToEnd = distanceToEnd
		self.totalCost = distanceToEnd +costSoFar
