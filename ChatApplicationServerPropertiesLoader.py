from components import IComponent
from properties_loader import property_loader
from ConfigManager import ConfigManager
from exception import PropertyLoadException,ComponentInitException

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
class ChatApplicationServerPropertiesLoader(IComponent):
    def checkPropertyValue(self,configValue,loadedProp,configManager):
        if (not(loadedProp == "null") and not(loadedProp == "")):
            configManager.setValue( configValue, loadedProp )
            return True
        else:
            return False
    def initialize(self):
        configManager = ConfigManager.Instance()
        configManager.initialize()
        configManager.setDefaultValue("PropertiesFile.Folder","chatapplication.properties")
        CSProps = property_loader(configManager.getValue("PropertiesFile.Folder"))
        try:
            CSProps.load()
            try:
                ( (self.checkPropertyValue( "ConnectionHandlers.Number", CSProps.getProperty( "ConnectionHandlers" ),configManager ) ))
            except:
                raise PropertyLoadException( "ConnectionHandlers.Number", "[ChatApplicationServer.PropertiesLoader]: Exception while loading property " )
            try:
                self.checkPropertyValue( "Server.PortNumber", CSProps.getProperty( "ServerPort" ),configManager ) 
            except:
                configManager.setValue( "Server.PortNumber", "1500" )  
            try:
                self.checkPropertyValue( "Server.Address", CSProps.getProperty( "ServerAddress" ) )
            except:
                configManager.setValue( "Server.Adress", "localhost" )
            try:
                self.checkPropertyValue( "Client.Username", CSProps.getProperty( "ClientUsername" ) )
            except:
                configManager.setValue( "Client.Username", "Anonymous" )   
        except:
            raise ComponentInitException( "[ChatApplicationServer.PropertiesLoader]: IOException ")

    def componentMain(self):
        pass
    def shutdown(self):
        pass


	
	