class ChatMessage:
    WHOISIN = 0
    MESSAGE = 1 
    LOGOUT = 2
    PRIVATEMESSAGE = 3
    def __init__(self,type,message):
        self._type = type
        self._message = message
        self.WHOISIN = 0
        self.MESSAGE = 1 
        self.LOGOUT = 2
        self.PRIVATEMESSAGE = 3

    def getType(self):
        return self._type

    def getMessage(self):
        return self._message