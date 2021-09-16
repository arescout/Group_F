# File containing client classes
# Imports
import socket

class Client():
    def __init__(self,serverAddress, serverPort):
        s = socket.socket()
        s.connect((socket.gethostname(),serverPort))

        return


    def initiateSocket(serverAddress, serverPort):
        socket = socket.socket()
        socket.connect((serverAddress,serverPort))
        return(socket)


def main():
    client = Client('127.0.0.1', 1234)


if __name__ == '__main__':
    main()
