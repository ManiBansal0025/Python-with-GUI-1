# Handle button click event
from tkinter import *
window = Tk()
window.title("Welcome here")
window.geometry('350x350')
lb = Label(window, text = "Hello", fg = "blue",bg = "red",font = ('Arial Bold',30))
lb.pack(side = TOP)
def clicked():
    print("clicked!")
bt = Button (text = "Click me",fg = "blue",command = clicked)
bt.pack(side = BOTTOM)
window.mainloop()
