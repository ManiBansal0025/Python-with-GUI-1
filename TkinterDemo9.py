# Handle button click event
from tkinter import *
def disp():
	lb.configure(text = "Hey")

window = Tk()
window.title("Welcome")
window.geometry('350x350')

lb = Label(window,text = "Hello",font = ('Calibri',30))
lb.place(x=70,y=60)

button1 = Button(window,text = "Click me", command= disp)
button1.pack(side = TOP)

button2 = Button(window,text = "QUIT", command= quit)
button2.pack(side = BOTTOM)

window.mainloop()
