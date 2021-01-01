from ComponentManager import ComponentManager
from ConfigManager import ConfigManager
from SocketServerEngine import SocketServerEngine
import sys
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
