# File containing Server classes
# Imports of external packages
import socket
from _thread import *
import threading

print_lock = threading.Lock()

# Imports of internal packages
from Tournament import Tournament


class Server():
    def __init__(self, port):
        # Define what port to use, this should be entered by the host
        self.port = port
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
            # Print the address for logging purposes
            print(address)
            print_lock.acquire()
            # Send a file
            #self.sendFile(clientSocket, 'testFile.txt')
            print('Connected to :', address[0], ':', address[1])
            start_new_thread(self.threaded, (clientSocket, ))
            print_lock.release()
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
                # Read the given amount of data from the file
                bytesRead = f.read(bufferSize)
                # If no new data is read, all is sent. Break the loop
                if not bytesRead:
                    break
                # Send the read data through the socket
                clientSocket.sendall(bytesRead)
        return True
    
    def receiveGameFile(self, clientSocket, filePath, data):
        # Open or create a file at the given address
        bufferSize = 4096
        with open(filePath, "wb") as f:
            f.write(data)
            while True:
            # Receive data from the socket
                bytesread =  clientSocket.recv(4096) 
                # If no new data is read, all is sent. Break the loop
                if not data:
                    break           
                # Write the data to the file
                f.write(bytesread)
        return True

    def receiveTournamentFile(self, clientSocket, filePath, data):
        # Open or create a file at the given address
        bufferSize = 4096
        with open(filePath, "wb") as f:
            f.write(data)
            while True:
            # Receive data from the socket
                bytesread =  clientSocket.recv(4096) 
                
                if not data:
                    break           
                # Write the data to the file
                f.write(bytesread)
        return True
    
    def threaded(self, c):
        while True:
            # data received from client
            data = c.recv(1024) 
            if not data:
                print('Bye')
              
                # lock released on exit
                print_lock.release()
                break
            
            if(str(data.decode('ascii'))[0]=='G'):
                self.receiveGameFile(c, 'testGameFile.txt', data)
                ### Todo: Make change in the gamefile to be sent?
                self.sendFile('testGameFile.txt')  ## only send to client 

            elif(str(data.decode('ascii'))[0]=='T'):
                self.receiveFile(c, 'testTournamentFile.txt', data)
                #### Todo: Make change in the tournamentfile to be sent?
                self.sendFile(c, 'testTournamentFile.txt')  ### send to all

            # reverse the given string from client ???
            #data = data[::-1]
  
            # send back reversed string to client
            #c.send(data)
            #self.receiveFile(c, "sampleRec.txt", data)
            #print(str(data.decode('ascii'))[0])
   
        # connection closed
        c.close()


def main():
    server = Server(1234)


if __name__ == '__main__':
    main()
