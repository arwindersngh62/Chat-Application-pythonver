from socket import socket
from ConfigManager import ConfigManager
from threading import Thread,RLock
import pickle
class ListenFromServer(Thread):
    def __init__(self,socket):
        self._socket = socket
        self._close = False
        super().__init__()

    def stop(self):
        print("Inside stop")
        self._close = True

    def run(self):
        while not(self._close):
            data = self._socket.recv(1024)
            if data:
                print(pickle.loads(data))

        print("In listen ffrom server ending")
