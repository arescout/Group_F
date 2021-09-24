# File containing Server classes
# Imports of external packages
import socket
from _thread import *
import threading
import json
import time

print_lock = threading.Lock()

# Imports of internal packages
from Tournament import Tournament


class Server():
    def __init__(self, port):
        # Define what port to use, this should be entered by the host
        self.port = port
        # Dict for storing player's sockets
        self.players = {}
<<<<<<< HEAD
        # Initiate the tournamen
        tournament = Tournament()
=======
        self.connections = []
>>>>>>> 4a1f1a9b7768fcac28c5f4255a908db5cc6c1aae
        # Initiate the Socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Bind the socket to the given port on localhost
        s.bind((socket.gethostname(),port))
        print("socket binded to port", port)
        # Define how many unanswered connections the socket will allow to queue
        s.listen(8)
        print("socket is listening")
        # Start listening to connections
        # For now, this loop will continue until manually terminated
        while True:
            # Accept an incomming connection
            clientSocket, address = s.accept()
            if len(self.players) >= 8:
                print('Game is full')
                continue
            # Print the address for logging purposes
            name = clientSocket.recv(1024)
            name = json.loads(name)
            tournament.addPlayer(name['name'])
            self.players.update({name['name']:clientSocket})
            print_lock.acquire()
            # Send a file
            #self.sendFile(clientSocket, 'testFile.txt')
            clientSocket.send("hejHEJHEJ".encode("ascii"))
            print('Connected to :', address[0], ':', address[1],': player', name['name'])
            connection = Connection(address[1], clientSocket)
            self.connections.append(connection)

            #print_lock.release()
            # Close the socket
        s.close()
        return

    # Function for sending files through the socket
    def sendFile(self, clientSocket, filePath):
        # Define how many bytes to send at a time
        bufferSize = 4096
        # Open the file that is to be transferred
        with open(filePath, 'rb') as f:
            while(True):
                # Make sure all data is read
                while True:
                    # Read the given amount of data from the file
                    bytesRead = f.read(bufferSize)
                    # If no new data is read, all is sent. Break the loop
                    if not bytesRead:
                        break
                    # Send the read data through the socket
                    clientSocket.sendall(bytesRead)
        return True

    def receiveFile(self, clientSocket, filePath, data):
        # Open or create a file at the given address
        with open(filePath, "wb") as f:
            # Receive data from the socket
            #bytesRead = clientSocket.recv(self.bufferSize)
            # Write the data to the file
            f.write(data)
        return True

    

class Connection():
    def __init__(self, port, clientSocket):
        self.sendQueue = []
        self.clientSocket = clientSocket
        self.port = port
        y = threading.Thread(target=self.recvThread)
        y.start()
        x = threading.Thread(target=self.sendThread)
        x.start()
        self.send("Welcome")
        time.sleep(1)
        self.send("Welcome2")

    def recvThread(self):
        while True:
            data = self.clientSocket.recv(1024)
            #self.send(data.decode("utf-8"))
            self.onMsg(data)

    def sendThread(self):
        while True:
            time.sleep(0.01)
            while len(self.sendQueue) != 0:
                self.clientSocket.send(self.sendQueue.pop(0))
                #self.clientSocket.send(f"Hallo {self.port}".encode("utf-8"))
            #print_lock.release()
    def send(self, msg):
        self.sendQueue.append(msg.encode("utf-8"))
    def onMsg(self, msg):
        print(msg.decode("utf-8"))     
        
    


def main():
    print("before initiation")
    server = Server(2232)
    time.sleep(10)
    print("SERVER")
    server.connections[0].send("TESTCONNECTIONS")


if __name__ == '__main__':
    main()
