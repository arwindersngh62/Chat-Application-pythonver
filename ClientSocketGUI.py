#from pythonver.ChatMessage import ChatMessage
import threading
from ConfigManager import ConfigManager
from components import IComponent
from PyQt5.QtCore import QBitArray, Qt
from PyQt5.QtGui import qAlpha
from PyQt5.QtWidgets import *
from functools import partial
import ClientEngine
from ChatMessage import ChatMessage
import time



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



class ClientSocketGUI():
    _instance = None
    _lock = threading.Lock()
    def __init__(self):
        self.timestamp = str(time.time())
        # Cannot hide ctor, so raise an error from 2nd instantiation
        if (ClientSocketGUI._instance != None):
            raise('This is a Singleton! use Singleton.GetInstance method')
        # Simulate ctor delay
        time.sleep(2)
        ClientSocketGUI._instance = self
        print(f'singleton class created {threading.current_thread()}')
        #PrintFlushed(‘Singleton was created by thread ID ‘ +  str(threading.current_thread().ident))
    @staticmethod
    def Instance():
        if (ClientSocketGUI._instance == None):
            ClientSocketGUI._lock.acquire()
            if (ClientSocketGUI._instance == None):
                ClientSocketGUI._instance = ClientSocketGUI()
            ClientSocketGUI._lock.release()
        return ClientSocketGUI._instance
    @staticmethod
    def Reset():
        ClientSocketGUI._instance = None



    def initialize(self):
        self._configManager = ConfigManager.Instance()
        self._client = ClientEngine.ClientEngine.Instance()
        self._client_Running = False
        self._server = None
        self._started = True
        self.createWindow()
    
    def componentMain(self):
        pass

    def shutdown(self):
        pass


    def createWindow(self):
        app = QApplication([])
        window_main = QWidget()
        header = QWidget()
        footer = QWidget()
        layout_main = QVBoxLayout()
        layout_header = QHBoxLayout()
        layout_footer = QHBoxLayout()


        addr_lbl = QLabel('Server Address:')
        self._addr_entry = QLineEdit()
        port_lbl = QLabel('Port Number:')
        self._port_entry = QLineEdit()
        self._port_entry.setMaximumWidth(300)
        self._addr_entry.setMaximumWidth(300)
        layout_header.addWidget(addr_lbl)
        layout_header.addWidget(self._addr_entry)
        layout_header.addWidget(port_lbl)
        layout_header.addWidget(self._port_entry)
        header.setLayout(layout_header)

        layout_main.addWidget(header)
        self._username_lbl = QLabel('Enter the Username Below')
        self._username_lbl.setAlignment(Qt.AlignCenter)
        self._username_entry = QLineEdit()
        layout_main.addWidget(self._username_lbl)
        layout_main.addWidget(self._username_entry)

        self._login_btn = QPushButton('Login')
        self._login_btn.clicked.connect(partial(self.actionPerformed,"login"))
        self._logout_btn = QPushButton('Logout')
        self._logout_btn.clicked.connect(partial(self.actionPerformed,"logout"))
        self._users_btn = QPushButton('Online Users')
        self._users_btn.clicked.connect(partial(self.actionPerformed,"whoisin"))
        self._private_btn = QPushButton('Private Chat')
        self._private_btn.clicked.connect(partial(self.actionPerformed,"privatechat"))
        self._p2p_btn = QPushButton('P2P')
        self._p2p_btn.clicked.connect(partial(self.actionPerformed,"P2P"))
        layout_footer.addWidget(self._login_btn)
        layout_footer.addWidget(self._logout_btn)
        layout_footer.addWidget(self._users_btn)
        layout_footer.addWidget(self._private_btn)
        layout_footer.addWidget(self._p2p_btn)
        footer.setLayout(layout_footer)

        self._btm_box1 = QTextEdit()
        self._btm_box2 = QTextEdit()
        layout_main.addWidget(self._btm_box1)
        layout_main.addWidget(self._btm_box2)
        layout_main.addWidget(footer)

        window_main.setLayout(layout_main)
        window_main.show()
        app.exec()

    def append(self,str):
        NewStr = " "
        NewStr2 = " "
        j = 0
        stringArray = str.split(",");
        if ("0" == stringArray[0]):
                NewStr="No Online Users \n"
        elif ("10" == stringArray[0]):
            for i in range(1,len(stringArray),3):
                j=j+1
                NewStr = NewStr.append(stringArray[i] + " at Port No: "+ stringArray[i+1] + "\n" )
        else:
            self._btm_box1.append(str);
         
        self._btm_box1.append(NewStr2);
        self._btm_box2.append(NewStr);

    #TODO 
    def apppendPrivateChat(self):
        pass

    def actionPerformed(self,event):
        if event == "logout":
            # Client.send Message(logout) TODO
            self._logout_btn.setDisabled(True)
            self._users_btn.setDisabled(True)
            self._login_btn.setDisabled(False)
            self._username_lbl.setText("Enter your UserName Below")
            msg = ChatMessage('LOGOUT','')
            self._client.sendMessage(msg)
            return

        elif event == "whoisin":
            msg = ChatMessage('WHOISIN','')
            self._client.sendMessage(msg)
            #client.sendMessage(new ChatMessage(ChatMessage.WHOISIN, ""));
            return

        elif event == "privatechat":
            #f.setVisible( true );
            return

        elif event == "sendbtn":
            #String privateMsg = textPortNo.getText()+ "," + ta3.getText()+ "-" + configManager.getValue( "Client.Username" ) +"-#";
            #System.out.println("2nd window : "+ privateMsg );
            #client.sendMessage(new ChatMessage(ChatMessage.PRIVATEMESSAGE, privateMsg))
            return

        elif event == "P2P":
            #P2PClient p2p = new P2PClient();
            pass

        elif event == "login":
            username = self._username_entry.text().strip()
            if len(username) ==0 : 
                self.append("One of the server address, port number or username are missing - Please try again!!\n")
                return
            server_addr = self._addr_entry.text().strip()
            if len(server_addr) ==0 : 
                self.append("One of the server address, port number or username are missing - Please try again!!\n")
                return
            port_num = self._port_entry.text().strip()
            if len(port_num) ==0 : 
                self.append("One of the server address, port number or username are missing - Please try again!!\n")
                return

            try:
            #Get the updates values  for the server address, port and client username... */
                self._configManager.setValue( "Server.Address" , self._addr_entry.text())
                self._configManager.setValue( "Server.PortNumber" , self._port_entry.text())
                self._configManager.setValue( "Client.Username" ,self._username_entry.text())
                    
                self._username_entry.setText(" ")
                self._username_lbl.setText("Enter your message below")
                    
                    #disable login button
                self._login_btn.setDisabled(True)
                    #enable the 2 buttons
                self._logout_btn.setDisabled(False)
                self._users_btn.setDisabled(False)
                    #disable the Server and Port JTextField
                self._addr_entry.setReadOnly(True)
                self._port_entry.setReadOnly(True)
                    #Action listener for when the user enter a message
                    
                self._client.initialize()
                
            except:
                pass

    def getPublicMsgToBeSent(self):
        return self._username_entry.text()

    def windowClosed(self):
        if not(self._client == None) and self._client.getIsRunning():
            self._client.shutdown()
if __name__ == "__main__":
    print("In client engine gui")
    configm = ConfigManager.Instance()
    configm.initialize()
    cgui = ClientSocketGUI.Instance()
    print(cgui)
    cgui.initialize()
