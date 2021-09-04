import threading
from ConfigManager import ConfigManager
import socket
from components import GenericThreadedComponent
from ServerStatistics import ServerStatistics
from SocketConnectionHandler import SocketConnectionHandler
import socketServerGUI
#from ComponentManager import ComponentManager
import time,sys,datetime
from chatMessages import ChatMessage
from threading import Lock, RLock
import pickle
class Vector():
	def __init__(self):
		self._list=[]
		#print(f'[SSEngine]:: new vector created with id:{id(self)}')
		self._lock = RLock()

	def add(self,data):
		with self._lock:
			#print(f'[SSEngine]::adding the connection handler:{id(data)} to :{id(self)}')
			self._list.append(data)
		
	def copy(self):
		with self._lock:
			#print(f'copying vector {id(self)}')
			vector_new = Vector()
			vector_new._list = self._list.copy()
			return(vector_new)
		
	def __len__(self):
		#swith self._lock:
			#print(f'[SSEngine]::measuring length current elements in {id(self)}')
			#for i in self._list:
				#print(f'[SSEngine]:: vector inside:{id(i)}')
		return int(len(self._list))

	def removeElementAt(self,i):
		with self._lock:
			#print(f'[SSEngine]:: removing element: {id(self._list[i])} from: {id(self)}')
			del self._list[i]
			#print('[SSEngine]:: deleting item , following item left')
			#for value in self._list:
			#	print(f"[SSEngine]:: {id(value)}")
	
	def elementAt(self,i):
		with self._lock:
			a = self._list[i]
		return a

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
		pass


	def printEstablishedSocketInfor(self):
		ocuupance = self._connHandlerOccp.copy()
		if len(ocuupance) == 0:
			socketServerGUI.SocketServerGUI.Instance().appendEvent("[SSEngine]:: There aren't any established client connections to the CA server " )
			return 0
		
		for i in range(len(ocuupance)):
			sch = ocuupance.elementAt(i)
			sch.printSocketInfo()

	def getServer(self):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#print(self._configManager.getValue("Server.Adress"))
		socketServerGUI.SocketServerGUI.Instance().appendEvent("[SSEngine]:: server socket running at "+ str( (self._configManager.getValue("Server.Adress"),self._configManager.getValueInt("Server.PortNumber"))))
		#print((self._configManager.getValue("Server.Adress"),self._configManager.getValueInt("Server.PortNumber")))
		s.bind((self._configManager.getValue("Server.Adress"),self._configManager.getValueInt("Server.PortNumber")))
		#s.bind(('127.0.0.1',19000)) 
		#s.listen(6)
		return(s)
		
	def initialize(self):
		self._isRunning = False 
		self._lock = RLock()
		self._connHandlerOccp = Vector()
		self._connectionHandlingPool = Vector()
		#print("In Initialize")
		self._configManager = ConfigManager.Instance()
		#print(self._configManager.getValue("Server:PortNumber"))
		self._lotusStat = ServerStatistics()

		self._configManager.setDefaultValue( "ConnectionHandlers.Number", '2')
		socketServerGUI.SocketServerGUI.Instance().appendEvent('[SSEngine]:: ConnectionHandling Pool (' + self._configManager.getValue( "ConnectionHandlers.Number" ) + ') fired up (' + self._lotusStat.getCurrentDate() + '));')
		for i in range(self._configManager.getValueInt("ConnectionHandlers.Number")):
			handler = SocketConnectionHandler()
			handler.start()
			#print('[SSEngine]:: starting handlers')
			handler.setHandlerIdentifierName( "CH #" + str(i + 1) )
			self._connectionHandlingPool.add(handler)
		#print(stuff)
		#try:
		self._chatApplication_Server = self.getServer()
		self._chatApplication_Server.listen(5)
		#Client, address = chatApplication_Server.accept()
		#print("connected to server: "+ str(address[0]+":"+str(address[1])))
        #self._socketReader = self._handelConnection.recv(4096)
		self._isRunning = True
		
		#except Exception as e:
		#ComponentManager.Instance().fatalException(e)
		super().initialize()

	def removeConnHandlerOccp(self,sch):
		OccupiedH = None
		for i in range(len(self._connHandlerOccp)):
			occupiedH = self._connHandlerOccp.elementAt(i)
			if (occupiedH.getHandlerIdentifierName() == sch ):
				self._connHandlerOccp.removeElementAt(i)
				break

	
	def getConnectionHandlingPool(self):
		return ( self._connectionHandlingPool)
	
	
	def addConnectionHandlerToPool( self,handlerName):
		handler = SocketConnectionHandler()
		handler.start()
		self._connectionHandlingPool.add(handler)
		handler.setHandlerIdentifierName(handlerName)
		socketServerGUI.SocketServerGUI.Instance().appendEvent(f"[SSEngine]:: {handler} terminated...New reference back in the pool") 
	
	def componentMain(self):
		#try:
	#	print('[SSEngine]::inside component main outside while')
		#print(bool(self._mustShutdown))
		while(not(self._mustShutdown)):
			#print('[SSEngine]::inside component main')
			client,address	= self._chatApplication_Server.accept()
			socketServerGUI.SocketServerGUI.Instance().appendEvent("[SSEngine]::connection recieved")
			data = client.recv(1024)
			user_name = pickle.loads(data)
			reply = {"addr":address[0],"port":address[1]}
			client.sendall(pickle.dumps(reply))
			socketHandler = None
			if len(self._connectionHandlingPool) == 0:
				socketServerGUI.SocketServerGUI.Instance().appendEvent(f'[SSEngine]::No more ConnHandlers available for {address}')
				continue
			else:
				with self._lock:
					socketHandler = self._connectionHandlingPool.elementAt( 0 )
				#with self._lock:
					self._connectionHandlingPool.removeElementAt(0)
					socketHandler.setSocketConnection((client,address,user_name))
					self._connHandlerOccp.add(socketHandler)
				self.printEstablishedSocketInfor()
			

			#print(f'threads tunning: {threading.active_count()}')

		# except:
		# 	print("in except")
		# 	pass
	
	def WriteMsgSpecificClient(PortNo, msg,self):
		occupance = []
		occupance = self._connHandlerOccp
		if len(occupance)== 0:
			return
		
		for i in range(len(occupance)):
			sch = occupance[i]
			if sch.getHandleSocket().getPort() == PortNo:
				sch.WriteMsg(msg)

	def broadcast(self,message):
		timenow = datetime.datetime.now()
		messageLf = f"{timenow}  {message}" 
		socketServerGUI.SocketServerGUI.Instance().appendRoom(messageLf)
		#print("[SSEngine]:: Creating a new vector in braodcast")
		occupance = self._connHandlerOccp.copy()
		if len(occupance) == 0:
			return
		else:
			for i in range(len(occupance)):
				sch = occupance.elementAt(i)
				sch.writeMessage(messageLf)

				
	def run(self):
		self._mustShutdown = False
		#print('inside running')
		self.componentMain()
		#print("Ending the thread")
		#for a in self._connectionHandlingPool:
			#a.stop()
		#sys.exit()
		#print("Still in the fucking thread")
	def getIsRunning(self):
		#
		# print("[SSEngine]:: In running")
		return self._isRunning

	def shutdown(self):
		try:
			self._ChatApplication__Server.close()
			self._isRunning = False
		except:
			pass
		super.shutdown()

if __name__ == '__main__':
	cm = ConfigManager.Instance()
	cm.initialize()
	new = SocketServerEngine.Instance()
	new.initialize()	