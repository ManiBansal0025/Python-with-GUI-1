#Changing button foreground and background color 
from tkinter import *
window = Tk()
window.title("Welcome here")
window.geometry('350x350')
lb = Label(window,text = "Hello",font = ('Arial Bold',50))
lb.pack(side = TOP)
bt = Button(window, text="Click me",fg = "red",bg = "blue")
bt.pack(side = TOP)
window.mainloop()
