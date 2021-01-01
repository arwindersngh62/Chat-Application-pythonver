class ComponentInitException(Exception):
    def __init__(self, message):

        # Call the base class constructor with the parameters it needs
        super(ComponentInitException, self).__init__(message)

class PropertyLoadException(Exception):
    def __init__(self,prop, message):

        # Call the base class constructor with the parameters it needs
        super(PropertyLoadException, self).__init__(message,prop)
    def getProperty():
        return(str(prop))	



