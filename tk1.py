from tkinter import *

#creating root widget
root = Tk()

#creating label widget
myLabel = Label(root, text = "First Window")

#shoving label widget on in screen using Pack
myLabel.pack()

#calling infinite event loop of the program
root.mainloop()