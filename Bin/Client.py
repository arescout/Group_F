# File containing client classes
# Imports of external packages
import socket
from _thread import *
import threading
import json
import time


print_lock = threading.Lock()

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
        #print("innan start new thread")
        #start_new_thread(self.threaded, (self.s, ))
        
        x = threading.Thread(target=self.listeningThread)
        x.start()
        
        return
            

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
    def sendFile(self, msg):
        self.s.send(msg.encode("utf-8"))

    def listeningThread(self):
        while True:
            #print("I WHILE")
            # data received from client
            data = self.s.recv(1024)
            #print("efter data")
            if not data:
                print('Bye')
                break
                # lock released on exit
            self.s.send("FRÅN CLIENT TILL SERVER".encode("utf-8"))
            time.sleep(1)
            print("Recieved from server", str(data.decode('utf-8')))
            #print_lock.release()
            
        self.s.close()

    def closeClient(self):
        self.s.close()
        print_lock.release()

def main():
    #addr = str(input('Enter server address: '))
    #port = int(input('Enter server port: '))
    #pname = str(input('Enter player name (without blankspaces): '))
    addr='127.0.0.1'
    port=2232
    pname='p'
    client = Client(addr, port, pname)    
    #print("förbi client")
    client.s.send("TEST SKICK".encode("ascii"))
    #time.sleep(10)
    #print("efter sleep i clienten")


if __name__ == '__main__':
    main()
