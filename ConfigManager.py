from components import IComponent
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
class ConfigManager(IComponent):

	def initialize(self):
		self._configValues= {}
	
	def componentMain():
		pass
	
	def shutdown():
		pass

	def getValue(self,key):
		if (not(key in self._configValues.keys())):
			print("Missing Key ["+ key+"]")
			return ""
		return(str(self._configValues[key]))

	def getValueInt(self,key):
		if (not(key in self._configValues.keys())):
			print("Missing Key ["+ key+"]")
			return 0
		return(int(self._configValues[key]))

	def getValuefloat(self,key):
		if (not(key in self._configValues.keys())):
			print("Missing Key ["+ key+"]")
			return 0
		return(float(self._configValues[key]))

	def setValue(self,key,value):
		self._configValues[str(key)] = str(value)

	def setDefaultValue(self,key,value):
		if (not(key in self._configValues.keys())):
			self._configValues[str(key)] = str(value)
			print("[ChatApplicationServer_ConfigManager]: Overriding config entry '" + key + "'")

#aa = ConfigManager.Instance()