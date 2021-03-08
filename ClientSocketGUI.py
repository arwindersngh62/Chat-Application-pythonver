from ConfigManager import ConfigManager 
from Tkinter import *
#from ClientEngine import ClientEngine


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
class ClientSocketGUI(IComponent):
	def __init__(self):
		self._configManager = ConfigManager.Instance()
		#self._client = ClientEngine.Instance()
	
	
	def createWindow(self):
		self._root = Tk()
		self._root.mainloop()
	
	def initialize(self):
		createWindow()

    def append(self,somemsg):
        pass
        
    def appendPrivateChat(self,msg):
        pass
        
    def actionPerformed(action)
        pass
        
    def loginFailed():
        pass
        
    def getPublicMessagemsgToBeSent():
        pass
        
    def componentMain():
        pass
        
        
    def windowClosing(action):
        pass
        
    def shutdown():
        pass
	
	
		