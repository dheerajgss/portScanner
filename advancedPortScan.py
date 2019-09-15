from socket import *
import optparse
from threading import *

def main():
    parser = optparse.OptionParser('Usage of program: '+'-H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', help='Specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', help='Specify target port seperated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPort = str(options.tgtPort).split(',')
    if(tgtHost == None or tgtPort == None):
        print(parser.usage)
        exit(0)
main()

