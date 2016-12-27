#! /usr/bin/python3 -vv
"""
This program is the result of the David Beazley intro course to Tkinter.
"""

import tkinter

def buttonfunk():
    print("you pressed a button")
    
class EntryField(tkinter.Frame):
    """Subclassing Frame to make a custom entry field"""
    
    def __init__(self,parent, label, labelwidth=12):
        tkinter.Frame.__init__(self,parent)
        l = tkinter.Label(self, text=label, width=labelwidth,anchor=tkinter.W)
        l.pack(side=tkinter.LEFT,fill=tkinter.X)
        tkinter.Entry(self).pack(side=tkinter.RIGHT, fill=tkinter.X, expand=True)

if __name__ == "__main__":
    root = tkinter.Tk(className = "My first Application")
    print(vars(root))
    b = tkinter.Button(root, text="PressMe",command=buttonfunk)
    b.pack()
    find = EntryField(root,"Find:")
    find.pack(side=tkinter.TOP,fill=tkinter.X,pady=3)
    replace = EntryField(root,"Replace with:")
    replace.pack(side=tkinter.TOP,fill=tkinter.X,pady=3)
