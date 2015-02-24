import socket

UDP_IP = "10.27.15.13" #ip of phone, use ifconfog in terminal
UDP_PORT = 1337

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

def move(x,y):
    data = str(x)+","+str(y)
    try:
        sock.sendto(data, (UDP_IP, UDP_PORT))
    except:
        pass
