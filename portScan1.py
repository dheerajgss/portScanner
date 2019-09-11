import socket

hold = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = "192.168.29.238"
port = 21

def portscanner(port):
    if(hold.connect_ex((host,port))):
        print("Port ",port," is closed!")
    else:
        print("Port ",port, " is open!")
portscanner(port)