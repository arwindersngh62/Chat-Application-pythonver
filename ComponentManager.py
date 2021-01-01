import sys
from ConfigManager import ConfigManager
from ChatApplicationServerPropertiesLoader import ChatApplicationServerPropertiesLoader 
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
class ComponentManager():
    def __init__(self):
        self._activeComponents = []
        self._handliingFatalException = False
        self._shuttingDown = False

    def startComponentsList(self,componentNames):
        try:	
            for nextComponent in componentNames:
                com = eval(nextComponent).Instance()
                print("[ChatApplicationServer_ComponentManager]: Starting " + nextComponent )
                com.initialize()
                self._activeComponents.insert(0,com)
        except Exception as e:
            print(' exceptions here '+ str(e))
        return(True)
        
    def startComponent(self,componentName):
        try:
            com = eval(componentName).Instance()
	    
            print( "[ChatApplicationServer_ComponentManager]: Starting " + componentName )
            com.initialize()
            self._activeComponents.insert(0,com)	
        except Exception as e:
            print('add exceptions here'+ str(e))
        return(True)

    def stopComponents(self):
        self._shuttingDown = True
        for com in self._activeComponents:
            print("[ChatApplicationServer_ComponentManger]: Stopping " + type(com).__name__())
            com.shutdown()
        self._activeComponents = []
        sys.exit(1)
        
        
    def fatalException(e):
        if (self._handliingFatalException):
            sys.exit(1)
        self._handliingFatalException = True
        print("-----------------------------------");
        print("[ChatApplicationServer_ComponentManager]: FATAL EXCEPTION...\n" + str(e));
        if (not(self._shuttingDown)):
            self.stopComponents()
        sys.exit(1)

#ComMan_test = ComponentManager.Instance()
#ComMan_configtest.startComponent("ConfigManager.ConfigManager")
#ComMan_test.startComponent("ChatApplicationServerPropertiesLoader")