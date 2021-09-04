from ComponentManager import ComponentManager
from ConfigManager import ConfigManager
from SocketServerEngine import SocketServerEngine
import sys
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
class chatApplicationServerEngine():
       
        def startUpCAServer(self):
            print("[ChatApplicationServer_Engine]: Booting up...")
            self._cm = ComponentManager.Instance()
            self._ourComponents = []
            self._ourComponents.append('ConfigManager')
            self._ourComponents.append('ChatApplicationServerPropertiesLoader')
            self._ourComponents.append('SocketServerGUI')
            print(self._ourComponents)
            print("[ChatApplicationServer_Engine]: Booting sequence complete")
            #if (not(self._cm.startComponent('ConfigManager'))):
             #   sys.exit()
            if ( not(self._cm.startComponentsList( self._ourComponents) ) ):
                sys.exit()
            #self._configmanager = ConfigManager.Instance()
            #self._server = SocketServerEngine.Instance()
            #self._configmanager.setValue("Server:PortNumber",'5150')
            #self._server.initialize()
            
        def startUpCAClient(self):
            print("[ChatApplicationServer_Engine]: Booting up...")
            cm = ComponentManager.Instance()
            ourComponents = []
            ourComponents.append('ConfigManager')
            ourComponents.append('ChatApplicationServerPropertiesLoader')
            print(ourComponents)
            if ( not(cm.startComponentsList( ourComponents) ) ):
                        sys.exit()
            configmanager = ConfigManager.Instance()
            server = SocketServerEngine.Instance()
            configmanager.setValue("Server:PortNumber",'5000')
            server.initialize()
            print("[ChatApplicationServer_Engine]: Booting sequence complete")
        def shutDownCA(self):
            print("[ChatApplication_Engine]: Shutting down..." )
            ConfigManager.Instance().stopComponents()
            print("[ChatApplication_Engine]: Shut down complete")
            
        def getCommandLineArgsPasswd(self):
            args = sys.argv
            
            for arg in args:
                #print(arg)
                if '=' in arg:
                    mode = arg.split('=')[1].lower()
                    #print(mode)
                else:
                    mode=''
            return mode
            

if __name__ == '__main__':  
    mode =   chatApplicationServerEngine.Instance().getCommandLineArgsPasswd()
    if  mode == "server":
        print("[Chat Application Server Engine]Starting Server")
        chatApplicationServerEngine.Instance().startUpCAServer()
    elif mode == 'client':
        print("[Chat Application Server Engine]starting Client")
    else:
        print("No correct mode given - either 'Mode=Server' or 'Mode=Client'")
#chatApplicationServerEngine.Instance().shutDownCA()    
    #print("Shuting Down server")
    sys.exit()
