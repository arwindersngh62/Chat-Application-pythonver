class property_loader():
    def __init__(self,file_name):
        self._data = open(file_name,"r")
        self._properties={}
    def load(self):
        for line in self._data:
            if line[0] == '#' or line[0] == '\n' :
                continue
            else:
                properties = line.split('=')
                properties[1] = properties[1].strip('\n') 
                self._properties[properties[0]] = properties[1]
        return(True)
    def setValue(self,prop_name):
        for line in self._data:
            if line[0] == '#' or line[0] == '\n' :
                continue
            else:
                properties = line.split('=')
                properties[1] = properties[1].strip('\n') 
                if prop_name == properties[0]:
                    self._properties[prop_name] = properties[1]
                    return(True)
                    break
        return(False)
    def getProperty(self,prop_name):
        return(self._properties[prop_name])
