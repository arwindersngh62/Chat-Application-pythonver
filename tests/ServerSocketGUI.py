from components import IComponent
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from components import IComponent

class SocketServerGUI(IComponent):
    def __init__(self):
        pass

    def initialize(self):
        self.createWindow()

    def componentMain(self):
        pass

    def shutdown(self):
        pass


    def createWindow(self):
        self._app = QApplication([])
        window_main = QWidget()
        window_top = QWidget()
        window_bottom = QWidget()



        layout_main = QVBoxLayout()
        layout_top = QFormLayout()
        layout_top.setFormAlignment(Qt.AlignCenter)
        layout_bottom = QVBoxLayout()


        strt_btn = QPushButton('Start')
        #strt_btn.move(100,100)
        strt_btn.setMaximumWidth(100)
        port_lbl = QLineEdit()
        port_lbl.setMaximumWidth(100)
        #port_lbl.move(200,100)
        layout_top.addRow(strt_btn,port_lbl)
        #layout_top.addWidget(port_lbl)
        window_top.setLayout(layout_top)

        btm_box1 = QTextEdit()
        btm_box1.append("Hello")
        btm_box1.append("hello")
        btm_box2 = QTextEdit()
        layout_bottom.addWidget(btm_box1)
        layout_bottom.addWidget(btm_box2)
        window_bottom.setLayout(layout_bottom)

        layout_main.addWidget(window_top)
        layout_main.addWidget(window_bottom)
        window_main.setLayout(layout_main)
        window_main.show()
        self._app.exec()

#abc = SocketServerGUI()
#abc.initialize()