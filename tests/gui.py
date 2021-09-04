from PyQt5.QtCore import QBitArray, Qt
from PyQt5.QtGui import qAlpha
from PyQt5.QtWidgets import *
app = QApplication([])
window_main = QWidget()
header = QWidget()
footer = QWidget()



layout_main = QVBoxLayout()
layout_header = QHBoxLayout()
layout_footer = QHBoxLayout()


addr_lbl = QLabel('Server Address:')
addr_entry = QLineEdit()
port_lbl = QLabel('Port Number:')
port_entry = QLineEdit()
port_entry.setMaximumWidth(300)
addr_entry.setMaximumWidth(300)
layout_header.addWidget(addr_lbl)
layout_header.addWidget(addr_entry)
layout_header.addWidget(port_lbl)
layout_header.addWidget(port_entry)
header.setLayout(layout_header)

layout_main.addWidget(header)
username_lbl = QLabel('Enter the Username Below')
username_lbl.setAlignment(Qt.AlignCenter)
username_entry = QLineEdit()
layout_main.addWidget(username_lbl)
layout_main.addWidget(username_entry)

login_btn = QPushButton('Login')
logout_btn = QPushButton('Logout')
users_btn = QPushButton('Online Users')
private_btn = QPushButton('Private Chat')
p2p_btn = QPushButton('P2P')
layout_footer.addWidget(login_btn)
layout_footer.addWidget(logout_btn)
layout_footer.addWidget(users_btn)
layout_footer.addWidget(private_btn)
layout_footer.addWidget(p2p_btn)
footer.setLayout(layout_footer)

btm_box1 = QTextEdit()
btm_box2 = QTextEdit()
layout_main.addWidget(btm_box1)
layout_main.addWidget(btm_box2)
layout_main.addWidget(footer)

window_main.setLayout(layout_main)
window_main.show()
app.exec()