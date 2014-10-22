#client
import atexit
import socket
import Packet
import time
import sys
import threading
import pygame
import Player



UDP_IP = "54.76.38.104"
UDP_IP = "127.0.0.1"
UDP_PORT = 1331

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


username = "username_default"
players = []



def sendDataToServer(data):
	global timeLast
	#print "Sending:",data
	sock.sendto(data, (UDP_IP, UDP_PORT))

def getPacket(data):
	iD = data[:2]
	return iD

def parsePacket(data,addr):
	global timeLast,username
	packetType = getPacket(data)

	if packetType=='00':
		loginP = Packet.Packet00Login()
		loginP.receivePacket(data)
		if loginP.username != username:
                        addPlayer(loginP.username,int(loginP.x),int(loginP.y))
		
		print loginP.username,"connected to the server!"
	elif packetType=='01':
		print "disconnect"
		sys.exit("bye bye")
	elif packetType=='02':
        	move = Packet.Packet02Move()
		move.receivePacket(data)
		print data
		for pl in players:
                        print move.username,"moved"
                        if move.username == pl.username:
                                print move.username,pl.x,pl.y
                                pl.x = int(move.x)
                                pl.y = int(move.y)
                                return
                if move.username!=username:
                        addPlayer(move.username,int(move.x),int(move.y))
		
def addPlayer(usename,x,y):
    pl = PlayerMP(usename,x,y)
    players.append(pl)
   




def waitForPacket():
	while True:
    		data, addr = sock.recvfrom(128) 
    		print "received message:", data, addr
    		parsePacket(data, addr)


def move(x,y):
        global username
        move = Packet.Packet02Move(username,x,y,0,0,0)
        sendDataToServer(move.getData())

def login(user,x,y):
	global username
        username  = user
        login = Packet.Packet00Login(user,x,y)
        sendDataToServer(login.getData())
        t = threading.Thread(target=waitForPacket)
        t.start()

def disconnect():
	disconnect = Packet.Packet01Disconnect(username)
	sendDataToServer(disconnect.getData())
	print "Disconnected from server!"


class PlayerMP(Player.Player):

    def __init__(self,username,x,y):
        super(PlayerMP,self).__init__(None,username,x,y)
    



    

