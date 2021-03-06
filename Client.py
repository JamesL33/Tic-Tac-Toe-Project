#Module in charge of handling all client related functions. (Inspired by David's code)
import socket, select, sys, time, pickle

class AlreadyConnected(Exception):
    print("You are already connected")

class NotConnected(Exception):
    print("You are not connected")

class Client:
    def __init__(self, host=None, port=12345):
        """Initalizes all the variables used in the rest of the module. (Setting host and port to default values if none are provided)."""
        if host == None:
            host = "127.0.0.1"
        self.__host = host
        self.__port = port
        self.client = None
        self.turn = None
        self.last_message = None        

    def connect(self):
        """Function in charge of connecting the client to the server."""
        if self.connected():
            raise AlreadyConnected()
        self.sendBuffer = []
        self.client = socket.socket()
        self.client.connect((self.__host, self.__port))

    def connected(self):
        """Function that returns wether or not the client is already connected."""    
        return self.client != None

    def shutdown(self):
        """Function that shuts down the client and resets variables used by the client."""
        if not self.connected():
            return
        self.client.close()
        self.client = None

    def send_message(self, msg):
        """Function that receives an input, pickles that input and adds it to a buffer."""
        msgbytes = pickle.dumps(msg)
        self.sendBuffer.append(msgbytes)

    def poll(self):
        """Function that handles receiving and sending messages to and from the client."""
        if not self.connected():
            raise NotConnected()

        read, write, error = select.select( [self.client], [self.client], [self.client], 0 )

        messages = []

        if error != []:
            pass

        try:
            if write != []:
                while len(self.sendBuffer) != 0:
                    msg = self.sendBuffer[0]
                    self.client.send(msg)
                    self.sendBuffer.pop(0)

            if read != []:
                msgbytes = self.client.recv(2048)
                try:
                    msg = pickle.loads(msgbytes)
                except EOFError:
                    print("EOFError")
                    pass
                if msg == True or msg == False:
                    self.turn = msg
                else:
                    print(msg)
                    self.last_message = msg

                if not msgbytes:
                    print("Connection disconnected")

        except ConnectionResetError:
            self.shutdown()

    def RunClient(self):
        """Function in charge of connecting the client, while giving a message confirming it. (Mostly used for debugging)"""
        while True:
            try:
                self.connect()
                break
            except KeyboardInterrupt:
                pass
            finally:
                if self.connected == True:
                    print("Client Connected")