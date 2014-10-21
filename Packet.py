import time,string

class Packet(object):

	packetID =-1

	def getID(self, data):
		return data[:2]

	def readData(self, data):
		return data[2:len(data)]

	def __init__(self,iD):
		self.packetID==iD

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

	def writeData(self,server):
		server.sendDataToAllClients(self.getData())

	def writeDataToServer(self,client):
		client.sendDataToServer(self.getData())


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

	def writeData(self,server):
		server.sendDataToAllClients(self.getData())

	def writeDataToServer(self,client):
		client.sendDataToServer(self.getData())

class Packet02Move(Packet):

	def __init__(self,username="",x=0,y=0,numSteps=0,isMoving=False,movingDir=0):
		super(Packet02Move,self).__init__(02)
		self.username = username
		self.x=x
		self.y=y
		self.numSteps=numSteps
		self.isMoving = isMoving
		self.movingDir = movingDir

	def receivePacket(self,data):
		stuff = string.split(data,",")
		self.username = stuff[0][2:]
		self.x=stuff[1]
		self.y=stuff[2]
		self.numSteps=stuff[3]
		self.isMoving = stuff[4]
		self.movingDir = stuff[5]


   	def getData(self):
   		return "02" + self.username +','+str(int(self.x))+','+str(int(self.y))+','+str(self.numSteps)+','+str(self.isMoving)+','+str(self.movingDir)

   	def getUsername(self):
   		return self.username

	def writeData(self,server):
		server.sendDataToAllClients(self.getData())

	def writeDataToServer(self,client):
		client.sendDataToServer(self.getData())
