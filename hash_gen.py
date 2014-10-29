import os
import sys
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import tkinter.filedialog
from tkinter import messagebox
import hashlib

class core():
    def __init__(self):
        pass
        g = gui()
        #gui.__init__(self)
        
    def openf(self):
        self.openfiles = tkinter.filedialog.askopenfilename( initialdir="~/passage",

                                        filetypes=[("Tous les fichiers", "*")])
        self.filetitle['text']='Fichier : {0}\n'.format(self.openfiles)
        

    def hashing(self, typ):
        read_size = 1024 # You can make this bigger
        if typ == 'md5':
            hsh = hashlib.md5()
        elif typ == 'sha1':
            hsh = hashlib.sha1()
        elif typ == 'sha256':
            hsh = hashlib.sha256()
        elif typ == 'sha512':
            hsh = hashlib.sha512()
            
        with open(self.openfiles, 'rb+') as f:
            for chunk in iter(lambda: f.read(8192), b''): 
                hsh.update(chunk)
        return hsh.hexdigest()

    
class gui(Tk, core):
    def __init__(self):
        #core.__init__(self)
        #Main window
        self.main = Tk()
        self.main.title('Hash Generator')
        self.main.resizable(width=False, height=False)

        hash_tuple = ('md5', 'sha1', 'sha256', 'sha512') #Dict for hash library
        self.arg = StringVar()
        self.Combo = Combobox(self.main, value=hash_tuple, textvariable = self.arg)
        self.Combo.grid(row = 3, column = 1, sticky=(E,N))
        self.main.columnconfigure(0, weight=1)
        self.main.rowconfigure(0, weight=1)  
        
        self.openfile = Button(self.main, text='Open file', command = self.openf).grid(
            row = 0, column = 1, pady = 0)
        
        self.hash = Text(self.main, width = 80, height = 2)
        self.hash.grid(row = 1, column = 1, pady = 5)
        
        self.Bhash = Button(self.main, text = 'Hash !')
        self.Bhash.grid(row = 3, column = 1, padx = 0)
        self.Bhash['command'] = self.show
        
        self.filetitle = Label(self.main, text='Fichiers')
        self.filetitle.grid(row = 4, column = 1)
        self.main.mainloop()

    def show(self):
        self.hash.delete(1.0, 2.0)
        self.value = self.arg.get()
        self.hash.insert(1.0, self.hashing(self.value)) 
    
if __name__ == '__main__':     
    t = core()
