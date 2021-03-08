import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        
        self.master = master
        #self.resizable(0, 0)
        self.pack()
        self.create_widgets()
        
        

    def create_widgets(self):
        self._topFrame = tk.Frame(self)
        self._bottomFrame = tk.Frame(self)
        
        self._loginButton = tk.Button(self._bottomFrame,text='Login')
        self._logoutButton = tk.Button(self._bottomFrame,text='Logout')
        self._OnlineUsersButton = tk.Button(self._bottomFrame,text='Online Users')
        self._PrivateChatButton = tk.Button(self._bottomFrame,text='Private Chat',command = self.createPrivateChat)
        self._P2PButton = tk.Button(self._bottomFrame,text='P2P')   
        
        self._serverAddrLbl = tk.Label(self._topFrame,text='Server Address:')
        self._PortNumLbl = tk.Label(self._topFrame,text='PortNumber:')
        self._usernameLbl = tk.Label(self,text='Enter your username below:')
        self._serverAddrEnt= tk.Entry(self._topFrame)
        self._PortNumEnt = tk.Entry(self._topFrame)
        self._usernameEnt = tk.Entry(self)
        
        
        self._textBoxTop = tk.Text(self,width=250, height=250)
        self._yBarTop = tk.Scrollbar(self._textBoxTop)
        self._yBarTop.config(command = self._textBoxTop.yview)
        self._textBoxTop.config(yscrollcommand=self._yBarTop.set)
        self._textBoxBottom = tk.Text(self)
        #Quote=("""Suck\ne\ne\ne\ne\ne\ne\ne\ne\ne\nee\ne\ne\ne\ne\ne\ne\ne\nee\ned\ne\ne\nde\nd\ne\nded\nc\nc\nx\nc\nx\nc\nzc\ns\nds\nx\nwd\ns\nd\nwd""")
        self._yBarTop.pack(side='right')
        #self._textBoxTop.insert("end",Quote)
        self._yBarTop.pack(fill='y')
        
        self._topFrame.pack(side = "top",fill='both',expand=True)
        self._bottomFrame.pack(side = "bottom",fill='both',expand=True)
        
        self._usernameLbl.pack(side='top',fill='x')
        self._usernameEnt.pack(side="top",fill='x')
        
        self._loginButton.pack(side="left")
        self._logoutButton.pack(side="left")
        self._OnlineUsersButton.pack(side="left")
        self._PrivateChatButton.pack(side="left")
        self._P2PButton.pack(side="left")
        self._serverAddrLbl.pack(side="left")
        self._serverAddrEnt.pack(side="left")
        self._PortNumLbl.pack(side="left")
        self._PortNumEnt.pack(side="left")

        self._textBoxTop.pack(side="top",fill='both')
        self._textBoxBottom.pack(side="top",fill='both')

    def createPrivateChat(self):
        self._privateChatWindow = tk.Toplevel()
        
    def createP2PChat(self):
        self._P2PChat = tk.Toplevel()

root = tk.Tk()
root.resizable(0, 0)
root.title('Chat Client')
app = Application(master=root)
app.mainloop()