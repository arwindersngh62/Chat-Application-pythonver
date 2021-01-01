from ConfigManager import ConfigManager
import socket
from components import GenericThreadedComponent
from ServerStatistics import ServerStatistics
from SocketConnectionHandler import SocketConnectionHandler
class Singleton:
	def __init__(self,cls):
		self.cls = cls
	
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

@Singleton
class SocketServerEngine(GenericThreadedComponent):
	def __init__(self):
		self._isRunning = False
	
	def printEstablishedSocketInfor(self):
		ocuupance = []
		ocuupance = self._connHandlerOccp
		if len(ocuupance) == 0:
			print('no established connections')
			return 0
		
		for i in range(len(ocuupance)):
			sch = ocuupance[i]
			sch.printSocketInfo()
	def getServer(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#s.bind() add data aquired from config manager here
		
	def initialize(self):
		self._configManager = ConfigManager.Instance()
		self._lotusStat = ServerStatistics()
		self._connHandlerOccp = []
		connectionHandlingPool = []
		self._configManager.setDefaultValue( "ConnectionHandlers.Number", '6')
		#print('[SSEngine]:: ConnectionHandling Pool (" + configManager.getValue( "ConnectionHandlers.Number" ) + ") fired up (" + lotusStat.getCurrentDate() + ")\n" );')
		for i in range(self._configManager.getValueInt("ConnectionHandlers.Number")):
			handler = SocketConnectionHandler();
			handler.start()
			handler.setHandlerIdentifierName( "CH #" + str(i + 1) )
			connectionHandlingPool.append(handler)
		#print(stuff)
		try:
			chatApplication_Server = getServer()
			isRunning = True
		
		except:
			ComponentManager.Instance().fatalException()
		super.initialize()

	def removeConnHandlerOccp(self,sch):
		OccupiedH = None
		for i in range(len(self._connHandlerOccp)):
			occupiedH = self._connHandlerOccp(i)
			if (occupiedH.getHandlerIdentifierName() == sch ):
				del self._connHandlerOccp[i]
				break

	def getConnectionHandlingPool():
		return ( self._connectionHandlingPool())
	
	def addConnectionHandlerToPool( handlerName):
		handler = SocketConnectionHandler()
		handler.start()
		connectionHandlingPool.addElement(handler)
	def componentMain(self):
		try:
			while(not(mustShutdown)):
				s= self._ChatApplication_Server.accept()
				socketHandler = None
				if len(self._connectionHandlingPool) == 0:
					continue
				socketHandler = connectionHandlingPool[0]
				del connectionHandlingPool[0]
				socketHandler.setSocketConnection(s)
				self._connHandlerOccp.add(socketHandler)

		except:
			pass
	
	def WriteMsgSpecificClient(PortNo, msg,self):
		occupance = []
		occupance = self._connHandlerOccp
		if len(occupance)== 0:
			return
		
		for i in range(len(ocuupance)):
			sch = occupance[i]
			if sch.getHandleSocket().getPort() == PortNo:
				sch.WriteMsg(msg)

	def broadcast(message):
		timenow = datetime.datetime.now()
		messageLf = timenow + " " + message 
		print(messageLf)
		occupance = []
		occupance = connHandlerOccp
		if len(occupance) == 0:
			return
		for i in range(len(occupance)):
			sch = occupance.get[i]
			sch.writeMsg(messageLf)
	def run(self):
		pass
	def getIsRunning(self):
		return self._isRunning

	def shutdown(self):
		try:
			self._ChatApplication__Server.close()
			self._isRunning = False
		except:
			pass
		super.shutdown()



		


			
		
	