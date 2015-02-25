import pygame
import random
import Tile
import string
import math
import RobotAI
import socket
import threading
import Client
import gui
import Queue


class Level():

	def __init__(self,w,h):
		self.width  = w
		self.height = h
		self.tiles = []
		#self.generateLevel()
		self.ticks=0
		self.player = None
		self.entities = []
		self.hasAStarWorker = False
		self.entitiesOnTiles = []
		self.hasChanged = True
		self.tileImage = 0
		self.paths = {}#used for testing if traps can be placed

##		self.workers = 1	#number of worker
##		self.addr_list = []	#list of client addresses and connections
##		self.HOST = ''
##		self.PORT = 1337
##		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##		self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
##		self.s.bind((self.HOST, self.PORT))
##		self.sendTilesToAStarWorker()
##		t = threading.Thread(target=self.listenForResult)
##		t.start()


        """Populates the tiles list to hold the level data.
        @Params:
                path(string): path to level file
        @Return:
                None
        """
        def loadLevelFromFile(self,path):

			if Client.isHost == True and gui.isMultiplayer==True:
				self.addTiles(path)
				Client.sendTiles(self.tiles)
			elif gui.isMultiplayer==True:
				while len(self.tiles)<2:#wait for tiles from host
					#print "Waiting for tiles.."
					pass
			else:
				self.addTiles(path)

        """Called by loadLevelFromFile depending on who is host and such
        """
        def addTiles(self,path):
                levelF = open(path,'r')
                data = levelF.read()
                x=0
                y=0

                data = string.split(data,"@")
                header  = string.split(data[0],",")
                self.width = int(header[0])
                self.height = int(header[1])
                self.tiles = [0]*(self.width*self.height)
                for i in data[1]:

			if i =='\n':
				continue

                        if i ==';':
                                x=0
                                y+=1
                                continue
                        try:
                                #self.setTile(x,y,Tile.tiles[Tile.getID(i)])
                                self.tiles[x+(y*self.width)]=Tile.tiles[Tile.getID(i)].id
                        except:
                                print "Fail at",x,y
                        x+=1


	"""Generates a random level
        @Params:
                None
        @Return:
                None
        """
	def generateLevel(self):
                for x in range(self.width):
                        for y in range(self.height):
                                self.tiles[x+(y*self.width)] = random.randint(1,4)

	"""Updates the tiles and entities
        @Params:
                None
        @Return:
                None
        """
	def tick(self):
		self.entitiesOnTiles  = []
                self.ticks+=1
                for e in self.entities:
                        self.entitiesOnTiles.append((e.centreX>>5,e.centreY>>5))
                        e.tick()

		for tile in Tile.tiles:
			tile.tick()

		for x in range(self.width):
                        for y in range(self.height):
                                if self.getTile(x,y).id== 5 and self.ticks%random.randint(1,10000)==0:
                                        self.setTile(x,y,Tile.amberlight)
                                        self.souroundingTiles(x,y,Tile.redlight,Tile.amberlight)
                                        #self.sendChangeToWorker(x,y,Tile.greenlight)
                                if self.getTile(x,y).id== 9 and self.ticks%random.randint(1,10000)==0:
                                        self.setTile(x,y,Tile.greenlight)
                                        self.souroundingTiles(x,y,Tile.amberlight,Tile.greenlight)
                                if self.getTile(x,y).id== 6 and self.ticks%random.randint(1,10000)==0:
                                        self.setTile(x,y,Tile.redlight)
                                        self.souroundingTiles(x,y,Tile.greenlight,Tile.redlight)
                                        #self.sendChangeToWorker(x,y,Tile.redlight)

        """recursively sets all identical surrounding tiles
        to a new tile
        @Params:
                x(int): x co-ordinate of starting tile
                y(int): y co-ordinate of starting tile
                get(tile): tile to be changed
                set(tile): tile to set
        """
        def souroundingTiles(self,x,y, get,set):
                for i in range(9):
                        dx = (i % 3) -1
                        dy = (i / 3) -1
                        if self.getTile(x+dx,y+dy).id== get.id:
                                self.setTile(x, y, set)
                                self.souroundingTiles(x+dx,y+dy,get,set)


        """Renders tiles and entities
        @Params:
                screen(pygame.surface): pygame surface to draw on to
                xoff(int): x offset of the objects to render
                yoff(int): y offset of the objects to render
        @Return:
                None
        """
	def render(self,screen,xoff,yoff):
		if self.tileImage==0 or self.hasChanged==True:
                        self.hasChanged = False
			self.tileImage = pygame.Surface((self.width<<5,self.height<<5))
			for x in range(self.width):
		                for y in range(self.height):
	                                self.getTile(x,y).render(self,self.tileImage,(x<<5),(y<<5),x,y)
		screen.blit(self.tileImage,(-xoff,-yoff))

		for e in self.entities:
			e.render(screen,xoff,yoff)
		for p in self.paths:
                        if self.paths[p]==False:continue
                        for node in range(len(self.paths[p])-1):
                                pygame.draw.line(screen, (0, 0, 255), ((self.paths[p][node].pos[0]<<5)+16-xoff,((self.paths[p][node].pos[1]<<5)+16-yoff)), ((self.paths[p][node+1].pos[0]<<5)+16-xoff,(self.paths[p][node+1].pos[1]<<5)+16-yoff))
		

        """changes to tile in level.tiles at index x+(y*level.width) to
           tile.id
        @Params:
                x(int): x position of tile
                y(int): y position of tile
                tile(Tile): tile to set
        @Return:
                None
        """
	def setTile(self,x, y, tile):
                if x < 0 or y < 0 or x > self.width or y > self.height:
			return
		self.tiles[x+(y*self.width)] = tile.id
		if gui.isMultiplayer:
			Client.setTile(tile.id,x,y)
		self.hasChanged = True

        """gets the tile  form level.tiles
        @Params:
                x(int): x position of tile
                y(int): y position of tile
        @Return:
                tile(Tile)
        """
	def getTile(self,x,y):

		if x < 0 or y < 0 or x > self.width or y > self.height:
			return Tile.void
		try:
			return Tile.tiles[self.tiles[x + y * self.width]]
		except IndexError:
			return Tile.void


	def canPassTile(self,t,x,y,entity):
		if t.isSolid:
			return False
		for i in self.entities:
			if i.x>>5 == x and i.y>>5 ==y:
				return False
		return True


        """gets distance between two points
        @Params:
                a(vec2): first point
                b(vec2): second point
        @Return:
                distance(double): distance between a and b
        """
	def getDistance(self,a,b):
		dx = a[0] - b[0]
		dy = a[1] - b[1]
		return math.sqrt(dx*dx+dy*dy)
	"""returns true if i is in list l
        @Params:
                l(list): list to check
                i(object): object to look for
        @Return:
                inList(boolean): true if i is in l
        """
	def isInList(self,l,i):
		for node in l:
			if node == i:
				return True

		return False

	"""returns true if i is in list l
        @Params:
                l(list): list to check
                i(object): object to look for
        @Return:
                inList(boolean): true if i is in l
        """
	def inList(self,l,i):
		for node in l:
			if node.pos == i:
				return True

		return False
        """gets the best option from list l
        @Params:
                l(list): list of nodes
        @Return:
                bestNode(Node): node with lowest cost fo far
        """
	def lookForFastest(self,l):
                currentSmallest =0
                bestNode = None
                if len(l)==1:
                        return l[0]
                for i in l:
                        if i.costSoFar<currentSmallest or currentSmallest==0:
                                currentSmallest =i.costSoFar
                                bestNode = i
                return bestNode

        """finds the fastest path between two points
        @Params:
                start(vec2): starting point
                goal(vec2): end point
        @Return:
                path(Node[]): next node to move to
        """
	def findPathAStar(self,start,goal):
		openList = []
		closedList = []
		currentNode = Node(start,None,0,self.getDistance(start,goal))
		del start
		openList.append(currentNode)
		while len(openList) >0:
			currentNode = self.lookForFastest(openList) #only use node with lowest cost
			if currentNode.pos == goal:
			#if len(closedList)>=20 or currentNode.pos == goal:
				path = []
				while currentNode.parent != None:#goes until reaches the start
					path.append(currentNode)
					currentNode = currentNode.parent
				del openList
				del closedList
				return path
			openList.remove(currentNode)
			closedList.append(currentNode)
			for i in range(9):
				if i==4 or i==0 or i==2 or i==6 or i==8:
					continue#ignore current tile
				x = currentNode.pos[0]
				y  = currentNode.pos[1]
				dx = (i % 3) -1
				dy = (i / 3) -1
				tile = self.getTile(x+dx,y+dy)
				if tile == None or tile == Tile.void:
					continue
				if not self.canPassTile(tile,x+dx,y+dy,None) and not tile.id == 9:
					#print 'solid'
					continue
				tilePos = (x+dx,y+dy)
				costSoFar = currentNode.costSoFar + (self.getDistance(currentNode.pos,tilePos)+tile.getSpeed())
				distanceToEnd = self.getDistance(tilePos,goal)
				node = Node(tilePos,currentNode,costSoFar,distanceToEnd)
				if self.inList(closedList,tilePos) and costSoFar >= node.costSoFar: #checks if node has already been used,or if you are going backwards
					continue
				if not self.inList(openList,tilePos) or costSoFar < node.costSoFar:#only add if it's not alredy there
					openList.append(node)




		print "No path :("
		return False

	"""finds the fastest path between two points
        @Params:
                start(vec2): starting point
                goal(vec2): end point
        @Return:
                path(Node[]): list of nodes in path
        """
        #http://www.redblobgames.com/pathfinding/a-star/implementation.html#sec-1-1#used that for reference
	def findPathBF(self,start,goal):
		frontier = Queue.Queue()
                frontier.put(start)
                came_from = {}
                came_from[start] = None
		while not frontier.empty():
                        current = frontier.get()

                        if current == goal:
                                print "end reached"
                                break
                        for i in range(9):
				if i==4 or i==0 or i==2 or i==6 or i==8:
					continue#ignore current tile
				x = current[0]
				y  = current[1]
				dx = (i % 3) -1
				dy = (i / 3) -1
				tile = self.getTile(x+dx,y+dy)
				if tile == None or tile == Tile.void:
					continue
				if not self.canPassTile(tile,x+dx,y+dx,None) and not tile.id == 9:
					#print 'solid'
					continue
				tilePos = (x+dx,y+dy)
				if tilePos not in came_from:
                                     frontier.put(tilePos)
                                     #print "Added node",tilePos
                                     came_from[tilePos] = current
                n = current
                path = []
                while True:
                        b = came_from[n]
                        if b==None or b==start:
                                break
                        n=b
                        path.append(Node(n,None,0,0))

                return path


	"""finds the fastest path between two points
        @Params:
                start(vec2): starting point
                goal(vec2): end point
        @Return:
                path(Node): next node to move to
        """

	def findPath(self,start,goal):
		openList = []
		closedList = []
		currentNode = Node(start,None,0,self.getDistance(start,goal))
		del start
		openList.append(currentNode)
		while len(openList) >0:
			currentNode = self.lookForFastest(openList) #only use node with lowest cost
			if currentNode.pos == goal:
			#if len(closedList)>=20 or currentNode.pos == goal:
				path = []
				while currentNode.parent != None:#goes until reaches the start
					path.append(currentNode)
					currentNode = currentNode.parent
				del openList
				del closedList
				if len(path) >0:
                                        return path[len(path)-1]
                                return True
			openList.remove(currentNode)
			closedList.append(currentNode)
			for i in range(9):
				if i==4 or i==0 or i==2 or i==6 or i==8:
					continue#ignore current tile
				x = currentNode.pos[0]
				y  = currentNode.pos[1]
				dx = (i % 3) -1
				dy = (i / 3) -1
				tile = self.getTile(x+dx,y+dy)
				if tile == None or tile == Tile.void:
					continue
				if not self.canPassTile(tile,x+dx,y+dx,None) and not tile.id == 9:
					#print 'solid'
					continue
				tilePos = (x+dx,y+dy)
				costSoFar = currentNode.costSoFar + (self.getDistance(currentNode.pos,tilePos)+tile.getSpeed())
				distanceToEnd = self.getDistance(tilePos,goal)
				node = Node(tilePos,currentNode,costSoFar,distanceToEnd)
				if self.inList(closedList,tilePos) and costSoFar >= node.costSoFar: #checks if node has already been used,or if you are going backwards
					continue
				if not self.inList(openList,tilePos) or costSoFar < node.costSoFar:#only add if it's not alredy there
					openList.append(node)




		print "No path :("
		return False


        def willBlockTreasure(self,e,x,y,updatePath):
                spawnLocation = (1,1)
                if self.paths=={}:
                        for t in gui.treasureLocations:
                                self.paths[t] = self.findPathAStar(spawnLocation,(t[0]>>5,t[1]>>5))
                                if self.paths[t]==False:
                                        print "treasure at",t,"was blocked from the off, implement something to stop this!"
                for t in self.paths:
                        index = 0
                        if self.paths[t] ==False:continue
                        for node in self.paths[t]:
                                index+=1
                                if node.pos == (x,y):
                                        self.entities.append(e)
                                        if updatePath == True:
                                                path = self.findPathAStar(spawnLocation,(t[0]>>5,t[1]>>5))#probably don't need to check the whole path unless updating
                                        else:
                                                prevNode = self.paths[t][index+1]
                                                path = self.findPathAStar((prevNode.pos[0],prevNode.pos[1]),(t[0]>>5,t[1]>>5))#quickly checks if there could be a new path
                                               
                                        self.entities.remove(e)
                                        if  path == False:
                                                return True
                                        if updatePath:
                                                self.paths[t] = path
                
                return False


        """sends tiles to A* worker
        @Params:
                None
        @Params:
                None
        """
	def sendTilesToAStarWorker(self):
		self.s.listen(self.workers)	#Listens for (n) number of client connections
		print 'Waiting for client...'
		for i in range(self.workers):	#Connects to all clients
			conn, addr = self.s.accept()	#Accepts connection from client
			print 'Connected by', addr
			self.addr_list.append((conn,addr))	#Adds address to address list
			print "connected!",conn,addr
		for i in range(self.workers):	#Converts array section into string to be sent
			data = self.tiles
			data.append(self.width)
			data.append(self.height)
			arraystring = repr(data)
			conn.sendto(arraystring , self.addr_list[i][1])	#Sends array string
			print 'Tiles sent to worker'
		self.hasAStarWorker = True

	"""sends updates to A* workers
        @Params:
                x(int): x pos of tile
                y(int): y pos of tile
                tile(Tile): tile that has changed
        @Return:
                None
        """
        def sendChangeToWorker(self,x,y,tile):
                for i in range(self.workers):	#Converts array section into string to be sent
			data = ["c"]
			data.append(x)
			data.append(y)
			data.append(tile.id)
			arraystring = repr(data)
			self.addr_list[i][0].sendto(arraystring , self.addr_list[i][1])

	"""requests an update from the A* worker
        @Params:
                workerID(int): id of the worker
                start(vec2): start of path
                goal(vec2): end of path
        @Return:
                None
        """
	def requestAStar(self,workerID,start,goal):
		arraystring = repr([start,goal])
		worker_add = self.addr_list[workerID][0]
		worker_add .sendto( arraystring , self.addr_list[workerID][1] )	#Sends array string
		print 'requesting A*!'

        """Listens to result from A* worker
        @Params:
                None
        @Return:
                None
        """
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
