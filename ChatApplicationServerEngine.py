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
       
        def startUpCAServer():
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
        def startUpCAClient():
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
        def shutDownCA():
            print("[ChatApplication_Engine]: Shutting down..." )
            ConfigManager.Instance().stopComponents()
            print("[ChatApplication_Engine]: Shut down complete")
            
        def getCommandLineArgsPasswd(self):
            agrs = sys.argv
            for arg in args:
                if '=' in arg:
                    mode = arg.split('=')[0].lower()
                else:
                    continue
            return mode
            
if __name__ == "__main__":
    server = chatApplicationServerEngine.Instance()
    if server.getCommandLineArgsPasswd() == "server":
        print("Starting Server")
    elif server.getCommandLineArgsPasswd == 'client':
        print("starting Client")
    else:
        print("No correct mode given - either 'Mode=Server' or 'Mode=Client'")
        
    print("Shuting Down server")
