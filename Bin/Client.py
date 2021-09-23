# File containing client classes
# Imports of external packages
import socket

# Class for handling everyting on the client side
class Client():
    def __init__(self,serverAddress, serverPort):
        # Set how many bytes to accept from a socket
        self.bufferSize = 4096
        # Inititate a Socket
        self.s = socket.socket()
        # Connect to a socket with a given address and port
        # For now it's localhost per default
        self.s.connect((socket.gethostname(),serverPort))
        # Receive a file that is sent instantly from the server
        #self.receiveFile(self.s,'testReceive.txt')
        #self.s.send(f"Hello".encode('ascii'))
        while True:
            data = self.s.recv(1024)
            self.receiveFile(self.s,'testReceive.txt', data)
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
    # This function assumes that all data is sent in one transmission, ie the file isn't bigger than bufferSize. 
    # - Not anymore I think?
    def receiveFile(self, socket, filePath, data):
        # Open or create a file at the given address
        with open(filePath, "wb") as f:
            f.write(data)
            while True:
                # Receive data from the socket
                bytesRead = socket.recv(self.bufferSize)
                # If no new data is read, all is sent. Break the loop
                if not bytesRead:
                    break
                # Write the data to the file
                f.write(bytesRead)
        return True

def main():
    client = Client('127.0.0.1', 1234)


if __name__ == '__main__':
    main()
