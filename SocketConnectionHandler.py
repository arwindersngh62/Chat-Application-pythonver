
#from pythonver.SocketServerEngine import SocketServerEngine
from threading import Thread,RLock
from ConfigManager import ConfigManager
from ServerStatistics import ServerStatistics
import pickle
from chatMessages import ChatMessage
import socketServerGUI
class abc():
    def __init__(self,type,msg):
        self._type = type
        self._msg= msg
    def get_type(self):
        return self._type
class SocketConnectionHandler(Thread):
        
        def __init__(self):
                self._configManager = ConfigManager.Instance()
                self._connectionstat = ServerStatistics()
                self._mustShutdown = False
                self._isSocketOpen = False
                self._handlerName = None
                self._handleConnection = None
                self._socketWriter = None
                self._socketReader = None
                self._lock = RLock()
                self._username = None
                self._address = None
                Thread.__init__(self)
	
        def printSocketInfo(self):
                if (not(self._handleConnection == None)):
                        if (not(self._handleConnection._closed)):
                                socketServerGUI.SocketServerGUI.Instance().appendEvent(f"----------[{self._handlerName}]:: Configuration properties of assigned socket connection----------")
                                socketServerGUI.SocketServerGUI.Instance().appendEvent(f"Remote Address:=  {self._address[0]}" )
                                socketServerGUI.SocketServerGUI.Instance().appendEvent(f"Remote Port:=  {self._address[1]}")
                                socketServerGUI.SocketServerGUI.Instance().appendEvent(f"Client UserName:= {self._username}")
                                #TODO DIffernce between local and INternet address
                                socketServerGUI.SocketServerGUI.Instance().appendEvent(f"Local Address:= {self._address[0]}")                                        
				
        def setSocketConnection(self,socket_tuple):
                self._lock.acquire()
                self._handleConnection = socket_tuple[0]
                self._address = socket_tuple[1]
                self._username = socket_tuple[2]
                self._isSocketOpen = True
                #print(self._address)
                socketServerGUI.SocketServerGUI.Instance().appendEvent(f"[SSEngine]:: {self._handlerName}  assigned to socket {self._address }") 
                self._lock.release()
                #self.setSocketStreamReaderWriter()
                print(self._username)
        #TODO
        def setSocketStreamReaderWriter(self):
                self._lock.acquire()
                #print("setting sockket stream readerwriter")
                self._socketReader = self._handleConnection.recv(4096)
                self._username = pickle.loads(self._socketReader)
                self._lock.release()
                return True
                



        def setHandlerIdentifierName(self,name):
                self._handlerName = name

        def getHandlerIdentifierName(self):
                return(self._handlerName)

        def getUserName(self):
                return (self._username)

        def getHandleSocket(self):
                return(self._handleConnection)
        def socketConnectionHandlerRelease(self,pool):
                self._lock.acquire()
                self._handleConnection = None
                self._address = None
                self._isSocketOpen = False
                
                pool.add(self)
                self._lock.release()
                #print stuff on gui and add it back to connection pool
        def stop(self):
                self._lock.acquire()
                self._mustShutdown = True
                self._isSocketOpen = False
                self._lock.release()
                
        def recieveContent(self):
                from SocketServerEngine import SocketServerEngine
                self._lock.acquire()
                #print("lock acquired in recive content")
                self._socketReader = self._handleConnection.recv(4096)
                self._lock.release()
                #print("lock released in recive content")
                #print(self._socketReader)
                if self._socketReader:
                        cm = pickle.loads(self._socketReader)
                        #print(cm.getType())
                        if cm.getType() == cm.message_type["WHOISIN"]:
                                #print('Whoisin mesgae recieved')
                                SocketServerEngine.Instance().printEstablishedSocketInfor()
                        if cm.getType() == cm.message_type["MESSAGE"]:
                                print("Sending data into socket server engine for braodcast")
                                SocketServerEngine.Instance().broadcast(f"{self._username}  {cm.getMessage()}")
                                print(f'recieved message is at {self.getHandlerIdentifierName()}:: {cm.getMessage()}')
                        if cm.getType() == cm.message_type["LOGOUT"]:
                                #print("Logout message recieved")
                                print(f"{self._username}  disconnected with a LOGOUT message.")
                                self._handleConnection.sendall(pickle.dumps("Exit the connection"))
                                connHandlerPool = SocketServerEngine.Instance().getConnectionHandlingPool()
                                self.socketConnectionHandlerRelease(connHandlerPool)
                                SocketServerEngine.Instance().removeConnHandlerOccp( self._handlerName )
                                self._isSocketOpen = False
                        if cm.getType() == cm.message_type["PRIVATEMESSAGE"]:
                                print(f"prvivte message recieved {cm.getMessage()}")
                        #msg = pickle.loads(self._socketReader)
                        #pass
                        #print(self._socketReader)
                
                #do stuff based on message type
                
        def writeMessage(self,msg):
                #print(f"locking for write message ::{self._username}")
                #self._lock.acquire()
                #print(f"Message sent to client {self._username}")
                #self._lock.release()
                #print(f"released locked for write message{self._username}")
                #with self._lock:
                self._handleConnection.sendall(pickle.dumps(msg))
                #self._lock.release()
                
                
                
        def run(self):
                while (not(self._mustShutdown)):
                        #print("running connection handler")
                        if (self._handleConnection == None):
                                #print("Waiting for connection")
                                pass
                        if (not(self._handleConnection == None)):
                                #print('socket added loop')
                                self.recieveContent()
                                #self.socketConnectionHandlerRelease()
                                #tell serverengine to remove socket from this connection handler
                print('exiting run loop!!')
                #print("stopping handler")
	