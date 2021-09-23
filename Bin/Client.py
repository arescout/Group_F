# File containing client classes
# Imports of external packages
import socket
import json

# Class for handling everyting on the client side
class Client():
    def __init__(self,serverAddress, serverPort, pname):
        # Set how many bytes to accept from a socket
        self.bufferSize = 4096
        # Set playername in game
        self.pname = pname
        # Inititate a Socket
        self.s = socket.socket()
        # Connect to a socket with a given address and port
        # For now it's localhost per default
        self.s.connect((socket.gethostname(),serverPort))
        # Receive a file that is sent instantly from the server
        #self.receiveFile(self.s,'testReceive.txt')
        self.s.send(str.encode(json.dumps({'name': self.pname})))
        while True:
            data = self.s.recv(1024)
            print("Recieved from server", str(data.decode('ascii')))
            ans = input("Do you want to send a message?")
            if ans == 'y':
                msg = input("Insert Message:")
                self.s.send(msg.encode('ascii'))
                continue
            else:
                break
        self.s.close()

    # Function for receiving a file from a socket
    # This function assumes that all data is sent in one transmission, ie the file isn't bigger than bufferSize
    def receiveFile(self, socket, filePath):
        # Open or create a file at the given address
        with open(filePath, "wb") as f:
            # Receive data from the socket
            bytesRead = socket.recv(self.bufferSize)
            # Write the data to the file
            f.write(bytesRead)
        return True

def main():
    #addr = str(input('Enter server address: '))
    #port = int(input('Enter server port: '))
    #pname = str(input('Enter player name (without blankspaces): '))
    addr='127.0.0.1'
    port=2232
    pname='p'
    client = Client(addr, port, pname)


if __name__ == '__main__':
    main()
