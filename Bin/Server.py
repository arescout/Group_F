# File containing Server classes
# Imports
import socket
from Tournament import Tournament

class Server():
    def __init__(self, port):
        self.port = port

        s = socket.socket()
        s.bind((socket.gethostname(),port))
        s.listen(8)

        while True:
            clientSocket, address = s.accept()

            print(address)

            clientSocket.close()

        s.close()

        return

    def initiateSocket(port):
        s = socket.socket()
        s.bind('',1234)
        s.listen(8)
        return(s)

def main():
    server = Server(1234)


if __name__ == '__main__':
    main()
