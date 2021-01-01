import abc
from threading import Thread
#abstract method and interface for components class
class IComponent(metaclass=abc.ABCMeta):
	@classmethod
	def __subclasshook__(cls, subclass):
		return(hasattr(subclass,'initialize') and callabel(subclass.initialize) and hasattr(subclass, 'shutdown')and callable(subclass.shutdown) and hasattr(subclass, 'componentMain')and callable(subclass.componentMain) or NotImplemented)
	

	@abc.abstractmethod
	def initialize(self):
		raise NotImplementedError

	@abc.abstractmethod
	def shutdown(self):
		raise NotImplementedError

	@abc.abstractmethod
	def componentMain(self):
		raise NotImplementedError


class GenericThreadedComponent(IComponent,Thread,metaclass=abc.ABCMeta):
	def __init__(self):
		self._mustShutdown = False
		Thread.__init__(self)
	
	@abc.abstractmethod
	def initialize(self):
		self._mustshutdown = False
		self.start()
		

	@abc.abstractmethod
	def shutdown(self):
		self._mustshutdown = True 
	
	def componentMain(self):
		print('Hello')
		#raise NotImplementedError

	@abc.abstractmethod
	def run(self):
		self.componentMain()


class newone(GenericThreadedComponent):
	def initialize(self):
		self._mustshutdown = False
		self.start()
		
	def shutdown(self):
		self._mustshutdown = True 

	
	def run(self):
		self.componentMain()
		
aaa = newone()
aaa.initialize()
#aaa.run()




