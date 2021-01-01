from threading import Thread
from ConfigManager import ConfigManager
from ServerStatistics import ServerStatistics
import pickle
class SocketConnectionHandler(Thread):
        def __init__(self):
                self._configManager = ConfigManager.Instance()
                self._connectionstat = ServerStatistics()
                self._mustShutdown = False
                self._isSocketOpen = False
                self._handlerName = None
                self._handelConnection = None
                self._socketWriter = None
                self._socketReader = None
                Thread.__init__(self)
	
        def printSocketInfo(self):
                if (not(self._handelConnection == None)):
                        if (not(handleConnection._closed)):
                                print('some info about the socket added to the GUI')
                                        
				
        def setSocketConnection(self,insocket):
                self._handelConnection = insocket
                self._isSocketOpen = True

        def setSocketStreamReaderWriter(self):
                self._socketReader = self._handelConnection.recv(4096)
                self._username = picle.loads(self._sockerReader)
                return True
        def setHandlerIdentifierName(self,name):
                self._handlerName = name

        def getHandlerIdentifierName(self):
                return(self._handlerName)

        def getUserName(self):
                return (self._username)

        def getHandleSocket(self):
                return(self._handleConnection)
        def socketConnectionHandlerRelease(self):
                self._handleConnection = None
                self._isSocketOpen = False
                #print stuff on gui and add it back to connection pool
        def stop(self):
                self._mustshutdown = True
                self._isSocketOpen = False
                
        def recieveContent(self):
                self._socketReader = connection.recv(4096)
                msg = pickle.loads(self._socketReader)
                #do stuff based on message type
                
        def writeMessage(self,msg):
                self._handleConnection.sendall(str.encode(msg))
                
                
                
        def run(self):
                while (not(self._mustShutdown)):
                        if (self._handleConnection == None):
                                self.wait()
                        if (not(self._handleConnection == None)):
                                self.recieveContent()
                                self.socketConnectionHandlerRelease()
                                #tell serverengine to remove socket from this connection handler
	
abc= SocketConnectionHandler()
abc.start()
		
