class ChatMessage():
    def __init__(self,msg_type,message):
        self.message_type = {'WHOISIN':0,'MESSAGE':1,'LOGOUT':2,'PRIVATEMESSAGE':3}
        self._type = self.message_type[msg_type]
        self._message = message
    def getType(self):
        return self._type
    def getMessage(self):
        return self._message
        
#abc = ChatMessage('WHOISIN','hello')

		