import socket
import Tile
import math
import time
from Node import *



def getTile(x,y):
    global width,height,tiles
    if 0 > x or x >= width or 0 > y or y >= height:
        return Tile.void
    return Tile.tiles[tiles[x + y * width]]

def getDistance(a,b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return math.sqrt(dx*dx+dy*dy)

def inList(l,i):
    for node in l:
        if node.pos == i:
            return True

    return False



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


def findPath(self,start,goal):
	openList = []
	closedList = []
	currentNode = Node(start,None,0,self.getDistance(start,goal))
	openList.append(currentNode)
	while len(openList) >0:

		#sorted(openList,key=lambda i: i.totalCost)
		currentNode = self.lookForFastest(openList) #only use node with lowest cost
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
			if i==4:
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
			costSoFar = currentNode.costSoFar + (self.getDistance(currentNode.pos,tilePos)+tile.getSpeed())
			distanceToEnd = self.getDistance(tilePos,goal)
			node = Node(tilePos,currentNode,costSoFar,distanceToEnd)
			if self.inList(closedList,tilePos) and costSoFar >= node.costSoFar: #checks if node has already been used,or if you are going backwards
				continue
			if not self.inList(openList,tilePos) or costSoFar < node.costSoFar:#only add if it's not alredy there
				openList.append(node)




	print "No path :("
	return None
print "Starting!"
HOST = '127.0.0.1'
PORT = 1337
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "TCP socket up!"


arraystring = ''
tiles = None
print 'Waiting for tiles...'

data = s.recv(4096)
print data
data = eval(data)
print len(data)
width = data[len(data)-2:len(data)-1][0]
height = data[len(data)-1:len(data)][0]
tiles =  data[:len(data)-2]
print width,height
print tiles


print 'Tiles recieved!'

while 1:
    data = s.recv(4096)
    request = eval(data)
    print request
    firstNode = findPath(request[0],request[1])
    if firstNode == None or len(firstNode)==0:
        continue
    firstNode = firstNode[len(firstNode)-1]
    toSend = [str(firstNode.pos[0]),str(firstNode.pos[1])]
    toSend = repr(toSend)
    s.sendall(toSend)
s.close()
