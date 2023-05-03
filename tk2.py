from tkinter import *

#creating root widget
root = Tk()

#creating label widget
myLabel1 = Label(root, text = "First Window")
myLabel2 = Label(root, text = "I am a Student.")

#shoving label widget on in screen using Grid
myLabel1.grid(row =0, column = 0)
myLabel2.grid(row = 1, column = 5)

#calling infinite event loop of the program
root.mainloop()