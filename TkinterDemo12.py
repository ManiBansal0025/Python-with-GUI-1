#Demo for combo box and spin box
from tkinter import *
from tkinter import ttk
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

month = StringVar()
combobox = ttk.Combobox(window,textvariable = month,font = ("Calibri",9))
combobox.place(y = 110,x=10)
combobox.config(values = ('Jan','Feb','Mar','April','May','June','July','Sept','Oct','Nov','Dec'))
month.set("Not a month!!")

year = StringVar()
spinbox = Spinbox(window,from_ = 1999, to=2030 ,textvariable = year,font = ("Calibri",9))
spinbox.place(y = 110, x = 170)
print(year.get())

bt = Button(window,text = "Quit", fg = "red",command = quit)
bt.place(y = 150,x = 10)

window.mainloop()
