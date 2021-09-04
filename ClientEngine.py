from ListenFromServer import ListenFromServer
from components import GenericThreadedComponent
from ConfigManager import ConfigManager
import ClientSocketGUI 
import socket
#from ClientSocketGUI import ClientSocketGUI
import pickle
from ChatMessage import ChatMessage
import time
import threading
class Singleton:
    def __init__(self,cls):
        if Singleton.__instance == None:
            self.cls = cls

        else:
            return Singleton.__instance

    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self.cls()
            return self._instance

    def __call__(self):
        raise   TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._cls)



class ClientEngine(GenericThreadedComponent):
        _instance = None
        _lock = threading.Lock()
        def __init__(self):
                self.timestamp = str(time.time())
                # Cannot hide ctor, so raise an error from 2nd instantiation
                if (ClientEngine._instance != None):
                        raise('This is a Singleton! use Singleton.GetInstance method')
                # Simulate ctor delay
                #time.sleep(2)
                ClientEngine._instance = self
                print(f'singleton class created {threading.current_thread()}')
                #PrintFlushed(‘Singleton was created by thread ID ‘ +  str(threading.current_thread().ident))
        @staticmethod
        def Instance():
                if (ClientEngine._instance == None):
                        ClientEngine._lock.acquire()
                        if (ClientEngine._instance == None):
                                ClientEngine._instance = ClientEngine()
                ClientEngine._lock.release()
                return ClientEngine._instance
        @staticmethod
        def Reset():
                ClientEngine._instance = None


        def initialize(self):
                self._isRunning = False
                self._mustShutdown = False
                self._configManager = ConfigManager.Instance()
                #self._clientgui = ClientSocketGUI.ClientSocketGUI.Instance()
                #self._configManager.initialize()
                #set values to removed later
                #self._configManager.setValue( "Server.Address" , '127.0.0.1')
                #self._configManager.setValue( "Server.PortNumber" , '19000')
                #self._configManager.setValue( "Client.Username" , 'Arwinder')
                #ServerStatistics lotusStat;
                #try:
                self._socket = socket.socket()
                print("Connecting to the server")
                self._socket.connect((self._configManager.getValue("Server.Address"),int(self._configManager.getValue("Server.PortNumber"))))
                print("connection completed")
                self._socket.sendall(pickle.dumps(self._configManager.getValue("Client.Username")))
                socket_data = self._socket.recv(1024)
                socket_data = pickle.loads(socket_data)
                print(socket_data)
                #except:
                #        print("Error connecting to the server:")
                        #ClientSocketGUI.Instance().loginFailed()
                        #return None
                #print( f"Connection accepted: {socket_data['addr']}:{socket_data['port']}" )
                #serveraddr = 
                #print(serveraddr)
                
                self._lfs = ListenFromServer(self._socket)
                self._lfs.start()
                super().initialize()
        def display(self,msg):
                ClientSocketGUI.ClientSocketGUI.Instance().append(msg)

        
        def sendMessage(self,msg):
                msg = pickle.dumps(msg)
                self._socket.sendall(msg)


        def shutdown(self):
                self._isRunning = False
                self._mustShutdown = True
                #self._socket.sendall(str.encode("Ending this cllient"))
                
        def componentMain(self):
                while not(self._mustShutdown):
                        #print("Please choose message type")
                        #user_input = int(input("1:Logout,2:WHOISIN,3:Privete message,4:message"))
                        #print(f"user input:{user_input}")
                        #if user_input == 1:
                        #        self._lfs.stop()
                        #        msg = ChatMessage('LOGOUT','')
                        #        self.sendMessage(msg)
                        #        break
                        #elif user_input == 2:
                        #        print("inside who is in")
                        #        msg = ChatMessage('WHOISIN','')
                        #        self.sendMessage(msg)
                        #elif user_input == 3:
                        #        print("inside private message")
                        #        msg = ChatMessage('PRIVATEMESSAGE','hello')
                        #        self.sendMessage(msg)
                        #else:
                        #        print("inside message type")
                        #        msg = ChatMessage('MESSAGE','hello non private')
                        #        self.sendMessage(msg)
                        clientgui = ClientSocketGUI.ClientSocketGUI.Instance()
                        print(clientgui)
                        msg = clientgui.getPublicMsgToBeSent()
                        if msg.strip() == "":
                                time.sleep(100)
                        
                        else:
                                msg = ChatMessage('MESSAGE',msg)
                                self.sendMessage(msg)
                        

                        #print(msg._type)
                self.shutdown()
        def run(self):
                self.componentMain()
        
        def getStreamReader(self):
                return self._socket
        

#ser = socket.create_server(('localhost',9080))

#a = ClientEngine.Instance()
#a.initialize()
