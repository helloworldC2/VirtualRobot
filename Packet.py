import time,string

class Packet(object):

	packetID =-1

	def __init__(self,iD):
		self.packetID==iD

	def getID(self, data):
		return data[:2]

	def readData(self, data):
		return data[2:len(data)]


	def writeData(self,server):
		server.sendDataToAllClients(self.getData())

	def writeDataToServer(self,client):
		client.sendDataToServer(self.getData())



class Packet00Login(Packet):

	def __init__(self,username="",x=0,y=0):
		super(Packet00Login,self).__init__(00)
		self.username = username
		self.x = x
		self.y = y
	def receivePacket(self,data):
		stuff = string.split(data,",")
		self.username = stuff[0][2:]
		self.x = stuff[1]
		self.y = stuff[2]


   	def getData(self):
   		return "00" + self.username+','+str(self.x)+','+str(self.y)

   	def getUsername(self):
   		return self.username


class Packet01Disconnect(Packet):

	def __init__(self,username=""):
		super(Packet01Disconnect,self).__init__(01)
		self.username = username

	def receivePacket(self,data):
		stuff = string.split(data,",")
		self.username = stuff[0][2:]


   	def getData(self):
   		return "01" + self.username

   	def getUsername(self):
   		return self.username

class Packet02Move(Packet):

	def __init__(self,username="",x=0,y=0,movingDir=0,isSwimming=False,):
		super(Packet02Move,self).__init__(02)
		self.username = username
		self.x=x
		self.y=y
		self.isSwimming = isSwimming
		self.movingDir = movingDir

	def receivePacket(self,data):
		stuff = string.split(data,",")
		self.username = stuff[0][2:]
		self.x=stuff[1]
		self.y=stuff[2]
		self.movingDir = stuff[3]
		self.isSwimming = stuff[4]


   	def getData(self):
   		return "02" + self.username +','+str(int(self.x))+','+str(int(self.y))+','+str(self.movingDir)+','+str(self.isSwimming)

   	def getUsername(self):
   		return self.username

class Packet03AddEntity(Packet):

	def __init__(self,idd=0,t="",x=0,y=0,otherData="no"):
		super(Packet03AddEntity,self).__init__(03)
		self.id = idd
		self.type = t
		self.x=x
		self.y=y
		self.otherData = otherData

	def receivePacket(self,data):
                print data
		stuff = string.split(data,",")
		self.id = stuff[0][2:]
		self.type=stuff[1]
		self.x=stuff[2]
		self.y=stuff[3]
		self.otherData = stuff[4]
		if self.otherData==None or self.otherData=="":
                        self.otherData = "no"


	def getData(self):
                print self.otherData
		return "03" + str(self.id) +','+self.type+','+str(int(self.x))+','+str(int(self.y))+','+str(self.otherData)

class Packet04MoveEntity(Packet):

	def __init__(self,id=0,x=0,y=0,movingDir=0,isSwimming = False):
		super(Packet04MoveEntity,self).__init__(04)
		self.id = id
		self.x=x
		self.y=y
		self.movingDir = movingDir
		self.isSwimming = isSwimming

	def receivePacket(self,data):
		stuff = string.split(data,",")
		self.id = stuff[0][2:]
		self.x=stuff[1]
		self.y=stuff[2]
		self.movingDir=stuff[3]
		self.isSwimming = stuff[4]

	def getData(self):
		return "04" + str(self.id) +','+str(int(self.x))+','+str(int(self.y))+','+str(self.movingDir)+','+str(self.isSwimming)


class Packet05SendTiles(Packet):

	def __init__(self,tiles=0):
		super(Packet05SendTiles,self).__init__(05)
		self.tiles = tiles

	def receivePacket(self,data):
		self.tiles = data[2:]


	def getData(self):
		return "05" + self.getTilesString()


	def getTilesString(self):
		t = ""
		for s in self.tiles:
			t+=str(s)
			t+=','

		return t


class Packet06UpdateTile(Packet):

	def __init__(self,tile=0,x=0,y=0):
		super(Packet06UpdateTile,self).__init__(06)
		self.tile = tile
		self.x = x
		self.y = y

	def receivePacket(self,data):
		stuff = string.split(data,",")
		self.tile = stuff[0][2:]
		self.x=stuff[1]
		self.y=stuff[2]


	def getData(self):
		return "06" +str(self.tile) + ',' + str(self.x) + ',' + str(self.y)
