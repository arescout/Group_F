# File containing Server classes
# Imports of external packages
import socket

# Imports of internal packages
from Tournament import Tournament

# Class for handling everything on the server side
class Server():
    def __init__(self, port):
        # Define what port to use, this should be entered by the host
        self.port = port
        # Initiate the Socket
        s = socket.socket()
        # Bind the socket to the given port on localhost
        s.bind((socket.gethostname(),port))
        # Define how many unanswered connections the socket will allow to queue
        s.listen(8)
        # Start listening to connections
        # For now, this loop will continue until manually terminated
        while True:
            # Accept an incomming connection
            clientSocket, address = s.accept()
            # Print the address for logging purposes
            print(address)
            # Send a file
            self.sendFile(clientSocket, 'testFile.txt')
        # Close the socket
        s.close()
        return

    # Function for sending files through the socket
    def sendFile(self, clientSocket, filePath):
        # Define how many bytes to send at a time
        bufferSize = 4096
        # Open the file that is to be transferred
        with open(filePath, 'rb') as f:
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

def main():
    server = Server(1234)


if __name__ == '__main__':
    main()
