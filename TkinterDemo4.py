#Setting window size
from tkinter import *
window = Tk()
window.title("Welcome here")
window.geometry('350X200')
lb = Label(window,text = "Hello" , font = ("Arial Bold",50))
lb.pack(side = TOP)
window.mainloop()
