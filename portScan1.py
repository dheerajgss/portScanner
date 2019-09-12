import socket

hold = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = input("Enter host IP address to scan: ")
port = int(input("Enter port number: "))

def portscanner(port):
    if(hold.connect_ex((host,port))):
        print("Port ",port," is closed!")
    else:
        print("Port ",port, " is open!")
portscanner(port)
