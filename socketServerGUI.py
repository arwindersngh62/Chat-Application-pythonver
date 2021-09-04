from components import IComponent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from components import IComponent
from ConfigManager import ConfigManager
import SocketServerEngine

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
class SocketServerGUI(IComponent):
    def __init__(self):
        pass

    def initialize(self):
        self._configManager = ConfigManager.Instance()
        self._server = SocketServerEngine.SocketServerEngine.Instance()
        self._serverRunning = False
        self._server = None
        self.createWindow()

    def componentMain(self):
        pass

    def shutdown(self):
        pass


    def createWindow(self):
        self._app = QApplication([])
        window_main = QWidget()
        window_main.resize(800,800)
        window_main.setWindowTitle("Server GUI")
        window_top = QWidget()
        window_bottom = QWidget()

        self._app.lastWindowClosed.connect(self.windowClosed)


        layout_main = QVBoxLayout()
        layout_top = QFormLayout()
        layout_top.setFormAlignment(Qt.AlignCenter)
        layout_bottom = QVBoxLayout()


        self._strt_btn = QPushButton('Start')
        #strt_btn.move(100,100)
        self._strt_btn.setMaximumWidth(100)
        self._strt_btn.clicked.connect(self.actionPerformed)
        self._port_lbl = QLineEdit()
        self._port_lbl.setMaximumWidth(100)
        #port_lbl.move(200,100)
        layout_top.addRow(self._strt_btn,self._port_lbl)
        #layout_top.addWidget(port_lbl)
        window_top.setLayout(layout_top)

        self._roomBox = QTextEdit()
        self._roomBox.setReadOnly(True)
        self._roomBox.append("Chat Room.")
        self._eventBox = QTextEdit()
        self._eventBox.setReadOnly(True)
        self._eventBox.append("Event Log.")

        layout_bottom.addWidget(self._roomBox)
        layout_bottom.addWidget(self._eventBox)
        window_bottom.setLayout(layout_bottom)

        layout_main.addWidget(window_top)
        layout_main.addWidget(window_bottom)
        window_main.setLayout(layout_main)
        window_main.show()
        self._app.exec()


    def actionPerformed(self):
        if self._serverRunning == True:
            self._serverRunning = False
            self._port_lbl.setReadOnly(False)
            self._strt_btn.setText("Start")
            self.appendEvent("Server Stopped")
            #self._server.shutdown()
        else:
            try:
                port = int(self._port_lbl.text().strip())
            except:
                self.appendEvent("Invalid Port Number")
            if port:
                self._serverRunning =True
                self._port_lbl.setReadOnly(True)
                self._strt_btn.setText("Stop")
                self.appendEvent("Server Started")
                self._configManager.setValue("Server.PortNumber",port)
                self._server = SocketServerEngine.SocketServerEngine.Instance()
                self._server.initialize()
            else:
                self.appendEvent("Please Enter a Port Number")
            #except:
             #   print("Invalid port number")

    def appendRoom(self,value):
        self._roomBox.append(str(value))

    def appendEvent(self,value):
        self._eventBox.append(str(value))

    def windowClosed(self):
        if not(self._server == None) and self._server.getIsRunning():
            self._server.shutdown()
        
        #print("Now Closing!!!!")
    
#abc = SocketServerGUI()
#abc.initialize()