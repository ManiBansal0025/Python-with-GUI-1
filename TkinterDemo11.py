# demo for checkbutton
from tkinter import *
window = Tk()
window .title("Welcome here")
window .geometry("350x350")

lb = Label(window,text = "Firstname", font = ("Calibri",10),fg = "blue")
lb.pack (anchor = W)

en = Entry(window, font = ("Calibri",10))
en.pack(anchor = W)

lb1 = Label(window,text = "lastname", font = ("Calibri",10),fg = "blue")
lb1.pack (anchor = W)

en1 = Entry(window, font = ("Calibri",10))
en1.pack(anchor = W)

cb = Checkbutton(window,text = "Male")
cb.place(y = 90 ,x= 10)

cb1 = Checkbutton(window,text = "Female")
cb1.place(y = 90 ,x= 70)

bt = Button(window,text = "Quit", fg = "red",command = quit)
bt.place(y = 150,x = 10)

window.mainloop()
