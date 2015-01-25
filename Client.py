import atexit
import socket
import Packet
import time
import sys
import threading
import pygame
import Player
import Duck
import Animal
import gui
import string



UDP_IP = "178.62.91.20"
#UDP_IP = "127.0.0.1"
UDP_PORT = 1331

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

isHost = False
isWaiting = True
isServerReady = False

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP


username = "username_default"
players = []
numOfEntities = 0



def sendDataToServer(data):
	global timeLast
	#print "Sending:",data
	sock.sendto(data, (UDP_IP, UDP_PORT))

def getPacket(data):
	iD = data[:2]
	return iD

def parsePacket(data,addr):
	global timeLast,username,isWaiting,isHost,isServerReady

        if data=="You Are Host":
                isHost=True
                return
	packetType = getPacket(data)

	if packetType=='00':
                isWaiting = False
		loginP = Packet.Packet00Login()
		loginP.receivePacket(data)
		if loginP.username != username:

                        for p in players:
                            if p.username == loginP.username:
                                return
                        addPlayer(loginP.username,int(loginP.x),int(loginP.y))

                else:
                    if len(players)==0:
                        isHost = True
                        print "YOU ARE HOST!"
                        print loginP.username,"connected to the server!"
	elif packetType=='01':
		print "disconnect"
                dis  = Packet.Packet01Disconnect()
                dis.receivePacket(data)
                for p in players:
                        if p.username == dis.username:
                                players.remove(p)

	elif packetType=='02':
        	move = Packet.Packet02Move()
		move.receivePacket(data)
		for pl in players:
                        if move.username == pl.username:
                                pl.x = int(move.x)
                                pl.y = int(move.y)
                                pl.movingDir = int(move.movingDir)
                                pl.isSwimming = move.isSwimming =="true"
                                return
                if move.username!=username:
                        addPlayer(move.username,int(move.x),int(move.y))
        elif packetType == '03':
                ent = Packet.Packet03AddEntity()
                ent.receivePacket(data)
                addEntity(ent.type,ent.x,ent.y)
        elif packetType == '04':
                move = Packet.Packet04MoveEntity()
                move.receivePacket(data)
                gui.level.entities[int(move.id)].x = int(move.x)
                gui.level.entities[int(move.id)].y = int(move.y)
                gui.level.entities[int(move.id)].movingDir = int(move.movingDir)
                gui.level.entities[int(move.id)].isSwimming = move.isSwimming =="true"
        elif packetType == '05':
                tiles = Packet.Packet05SendTiles()
                tiles.receivePacket(data)
                setTiles(tiles.tiles)
                print "Got tiles"
        elif packetType == '06' and isHost==False:
                tile = Packet.Packet06UpdateTile()
                tile.receivePacket(data)
                gui.level.tiles[int(tile.x)+(gui.level.width*int(tile.y))] = int(tile.tile)
                gui.level.hasChanged = True

def setTile(tile,x,y):
    send = Packet.Packet06UpdateTile(tile,x,y)
    sendDataToServer(send.getData())


def setTiles(tiles):
    tiles = string.split(tiles,",")
    for t in tiles:
        try:
            gui.level.tiles.append(int(t))
        except ValueError:
            pass

def sendTiles(tiles):
    send = Packet.Packet05SendTiles(tiles)
    sendDataToServer(send.getData())

def addPlayer(usename,x,y):
    pl = PlayerMP(usename,x,y)
    players.append(pl)


def addEntity(e,x,y):
    print e
    if e == "Duck":
        d = Duck.Duck(gui.level,int(x),int(y))
    elif e == "Crab":
        d = Animal.Animal(gui.level,int(x),int(y))

    gui.level.entities.append(d)

def sendEntity(e,x,y):
    global numOfEntities
    ent = Packet.Packet03AddEntity(numOfEntities,e,x,y)
    numOfEntities+=1
    sendDataToServer(ent.getData())

def moveEntity(id,x,y,movingDir,isSwimming):
    move = Packet.Packet04MoveEntity(id,x,y,movingDir,isSwimming)
    sendDataToServer(move.getData())


def waitForPacket():
	while True:
    		data, addr = sock.recvfrom(4096)
    		parsePacket(data, addr)


def move(x,y,direction,isSwimming):
        global username
        move = Packet.Packet02Move(username,x,y,direction,isSwimming)
        sendDataToServer(move.getData())

def login(user,x,y):
	global username,isServerReady
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
