import E621Fetch
from Tkinter import *

class E621App:
    def __init__(self, master):
        frame = Frame(master);
        frame.pack();
        # Class Variables
        self.dynVar = StringVar();
        self.dynVar.trace('w', self.OnDynChange);
        self.dynVar.set('Hello Message');
        
        # Labels
        #self.dynMsg = Message(message);
        
        # Buttons
        self.btnQuit = Button(master, text = 'QUIT', command=frame.quit);
        self.btnQuit.pack();

    #def OnDynChange(*args):
        #self.dynMsg['text'] = self.dynVar.get();
        #print args

if __name__ == '__main__':
    root = Tk();
    app = E621App(root);
    mainloop();
