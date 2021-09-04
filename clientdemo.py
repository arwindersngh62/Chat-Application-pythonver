import socket
import pickle
from threading import Thread
from chatMessages import ChatMessage

class listner(Thread):
    def __init__(self,socket):
        self._socket = socket
        super().__init__()
        
    def run(self):
        while True:
            data = self._socket.recv(1024)
            if data:
                print(data)
                
class abc():
    def __init__(self,type,msg):
        self._type = type
        self._msg= msg
    def get_type(self):
        return self._type
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = clientSocket.connect(('127.0.0.1',19000))
#print(f"client connected :{address}")
data_get = listner(clientSocket)
data_get.start()
#print(clientSocket.getaddrinfo())
#dataFromServer = clientSocket.recv(1024);
#print(dataFromServer.decode());
send_more= True



a = abc('eee','dddd')



    
while send_more:
    data= input("Enter message to be sent")
    #cm = ChatMessage(1,str(data))
    clientSocket.send(pickle.dumps(data));
    #dataFromServer = clientSocket.recv(1024); 
    #print(dataFromServer.decode());    
    ask = input("Send more messages y/n")
    if ask.lower()=='n':
        break
        
        
