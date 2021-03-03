class ChatMessage():
    def __init__(self,msg_type,message):
        message_type = {'WHOISIN':0,'MESSAGE':1,'LOGOUT':2,'PRIVATEMESSAGE':3}
        self._type = message_type[msg_type]
        self._message = message
    def getType(self):
        return self._type
    def getMessage():
        return self._message
        
#abc = ChatMessage('WHOISIN','hello')

		