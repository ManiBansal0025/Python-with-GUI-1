# Demo for tkinter textbox
from tkinter import *
window = Tk()
window .title("Welcome here")
window .geometry("350x350")

lb = Label(window,text = "Firstname", font = ("Calibri",30),fg = "blue")
lb.pack (anchor = W)

en = Entry(window, font = ("Calibri",10))
en.pack(anchor = W)

lb1 = Label(window,text = "lastname", font = ("Calibri",30),fg = "blue")
lb1.pack (anchor = W)

en1 = Entry(window, font = ("Calibri",10))
en1.pack(anchor = W)

bt = Button(window,text = "Quit", fg = "red",command = quit)
bt.pack(anchor = W)

window.mainloop()
