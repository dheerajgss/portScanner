from socket import *
import optparse
from threading import *

def connectScan(tgtHost, tgtPort):
    try:
        hold = socket(AF_INET, SOCKET_STREAM)
        hold.connect((tgtHost, tgtPort))
        print("%d/tcp open" % (tgtPort) )
    except:
        print("%d/tcp closed" % (tgtPort))
    finally:
        hold.close()
        
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("Unknown host")
    try:
        tgtName = gethostbyaddr(tgtIP)
        print("Scan results for: "+ tgtName[0])
    except:
        print("Scan results for: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connectScan, args = (tgtHost, int(tgtPort)))
        t.start();

def main():
    parser = optparse.OptionParser('Usage of program: '+'-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target port seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if(tgtHost == None or tgtPorts == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)

if __name__ == '__main__':
    main()

