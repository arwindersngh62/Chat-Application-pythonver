from pythonver.SocketServerEngine import SocketServerEngine
from SocketConnectionHandler import SocketConnectionHandler
socketConn = SocketConnectionHandler()
socketServer = SocketServerEngine()
print('Testing SocketConnectionHandler....')
print('Displaying attributes..')
attr = vars(socketConn)
for value in attr:
    print(f'value for {value} is::     {attr[value]}')
print('starting handler')
socketConn.start()
from socket import socket
print('addding socket to the handler')
a =socket()
socketConn.setSocketConnection(a)
print('socket added')
print('removing socket')
socketConn.socketConnectionHandlerRelease()
print('stopping')
socketConn.stop()
print('SocketConnectionHandler works okay')
print('Testing SocketServerEngine socketServer')
