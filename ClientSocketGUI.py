from ConfigManager import ConfigManager 
import tkinter as tk
from components import IComponent
#from ClientEngine import ClientEngine


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
class ClientSocketGUI(IComponent):
    def __init__(self):
        self._privateChatExists = False
        self._p2pExists = False
        pass
#self._configManager = ConfigManager.Instance()
#self._client = ClientEngine.Instance()

    def createWindow(self):
        self._root = tk.Tk()
        self._topFrame = tk.Frame(self._root)
        self._bottomFrame = tk.Frame(self._root)
        
        self._loginButton = tk.Button(self._bottomFrame,text='Login')
        self._logoutButton = tk.Button(self._bottomFrame,text='Logout',state=tk.DISABLED)
        self._OnlineUsersButton = tk.Button(self._bottomFrame,text='Online Users',,state=tk.DISABLED)
        self._PrivateChatButton = tk.Button(self._bottomFrame,text='Private Chat',command = self.openPrivateChat)
        self._P2PButton = tk.Button(self._bottomFrame,text='P2P',command = self.openP2PChat)   
        
        self._serverAddrLbl = tk.Label(self._topFrame,text='Server Address:')
        self._PortNumLbl = tk.Label(self._topFrame,text='PortNumber:')
        self._usernameLbl = tk.Label(self._root,text='Enter your username below:')
        self._serverAddrEnt= tk.Entry(self._topFrame)
        self._PortNumEnt = tk.Entry(self._topFrame)
        self._usernameEnt = tk.Entry(self._root)
        
        
        self._textBoxTop = tk.Text(self._root,width=250, height=250)
        self._yBarTop = tk.Scrollbar(self._textBoxTop)
        self._yBarTop.config(command = self._textBoxTop.yview)
        self._textBoxTop.config(yscrollcommand=self._yBarTop.set)
        self._textBoxBottom = tk.Text(self._root)
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
        self._root.mainloop()

    def openPrivateChat(self):
        if not(self._privateChatExists):
                self._privateChatExists = True
                self.createPrivateChat()

    def createPrivateChat(self):
        self._privateChatWindow = tk.Toplevel()
        self._privateChatWindow.protocol("WM_DELETE_WINDOW",self.closePrivateChat)
        self._privateTopFrame = tk.Frame(self._privateChatWindow)
        self._privateBottomFrame = tk.Frame(self._privateChatWindow)
        self._privateUsernameLbl = tk.Label(self._privateTopFrame,text='Enter Username:')
        self._privateUsernameEnt = tk.Entry(self._privateTopFrame)
        self._privatePortNumberLbl = tk.Label(self._privateBottomFrame,text = 'Enter Port Number:')
        self._privatePortNumberEnt = tk.Entry(self._privateBottomFrame)
        self._privateText = tk.Text(self._privateChatWindow)
        self._privateSendButton = tk.Button(self._privateChatWindow,text = 'Send')
        self._privateTopFrame.pack(side = 'top')
        self._privateBottomFrame.pack(side = 'top')
        self._privateText.pack(side = 'top')
        self._privateSendButton.pack(side = 'bottom')
        self._privateUsernameLbl.pack(side = 'left')
        self._privateUsernameEnt.pack(side = 'left')
        self._privatePortNumberLbl.pack(side = 'left')
        self._privatePortNumberEnt.pack(side = 'left')
        #self._privateChatExists = False

    def closePrivateChat(self):
        self._privateChatWindow.destroy()
        self._privateChatExists = False

    def openP2PChat(self):
        if not(self._p2pExists):
                self._p2pExists = True
                self.createP2PChat()

    def createP2PChat(self):
        self._p2pChatWindow = tk.Toplevel()
        self._p2pChatWindow.protocol("WM_DELETE_WINDOW",self.closeP2PChat)
        self._p2pTopFrame = tk.Frame(self._p2pChatWindow)
        self._p2pBottomFrame = tk.Frame(self._p2pChatWindow)
        self._p2pRecieverPortLbl = tk.Label(self._p2pTopFrame, text = "Reciever's Port No:")
        self._p2pRecieverPortEnt = tk.Entry(self._p2pTopFrame)
        self._p2pRecieverIPLbl = tk.Label(self._p2pTopFrame,text = "Reciever's IP Add:")
        self._p2pRecieverIPEnt = tk.Entry(self._p2pTopFrame)
        self._p2pMsgLbl = tk.Label(self._p2pChatWindow, text = "Enter Message Below")
        self._p2pMsgEnt = tk.Entry(self._p2pChatWindow)
        self._p2pText = tk.Text(self._p2pChatWindow)
        self._p2pSendBtn = tk.Button(self._p2pBottomFrame,text = 'Send')
        self._p2pStartBtn = tk.Button(self._p2pBottomFrame, text = 'Start')
        self._senderPortNoLbl = tk.Label(self._p2pBottomFrame, text = "Sender's Port no")
        self._senderPortNoEnt = tk.Entry(self._p2pBottomFrame)
        self._p2pTopFrame.pack(side = 'top')
        self._p2pRecieverPortLbl.pack(side = 'left')
        self._p2pRecieverPortEnt.pack(side = 'left')
        self._p2pRecieverIPLbl.pack(side = 'left')
        self._p2pRecieverIPEnt.pack(side = 'left')
        self._p2pRecieverIPLbl.pack(side='left')
        self._p2pMsgLbl.pack(side = 'top')
        self._p2pMsgEnt.pack(side = 'top')
        self._p2pText.pack(side = 'top')
        self._p2pBottomFrame.pack(side = 'top')
        self._p2pSendBtn.pack(side= 'left')
        self._p2pStartBtn.pack(side = 'left')
        self._senderPortNoLbl.pack(side = 'left')
        self._senderPortNoEnt.pack(side = 'left')
        
        
        #self._privateChatExists = False

    def closeP2PChat(self):
        self._p2pChatWindow.destroy()
        self._p2pExists = False

    def initialize(self):
        self._configManager = ConfigManager.Instance()
        #self._clientEngine = ClientEngine.Instance()
        self.createWindow()

    def append(self,strng):
        NewStr = " "
        NewStr1 = " "
        #j = 0
        stringArray = strng.split(",")
        if ("0" == stringArray[0]):
            NewStr = "No Online Users \n"
        elif ("10" == stringArray[0]):
            for i in (range(1,len(stringArray)-1,3)):
                NewStr+=(stringArray[i]+" at port No: "+ stringArray[i+1] + "\n")
        else:
            self._textBoxTop.insert(tk.END,strng)
        self._textBoxTop.insert(NewStr2)
        self._textBoxBottom.insert(NewStr)

    def appendPrivateChat(self,msg):
        self._privateText.insert(tk.END,msg)
        

    ##def actionPerformed(action):
    ##    pass
    def logout(self):
        #client.sendMessage( new ChatMessage(ChatMessage.LOGOUT, "") );
        

    def loginFailed():
        pass

    def getPublicMessagemsgToBeSent():
        pass

    def componentMain():
        pass


    def windowClosing(action):
        pass

    def shutdown():
        pass


a = ClientSocketGUI.Instance()
a.initialize()
