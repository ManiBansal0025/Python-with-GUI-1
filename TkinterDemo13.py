#Demo for labelframe
from tkinter import *

 window = Tk()
 window.title("Welcome here")
 window.geometry("1300x800")
 window.config(bg = "blue")
 
 frame1 = Frame(window,bg = "grey")
 frame1.pack(side = TOP)
 frame2 = Frame(window,bg = "grey")
 frame2.pack(side = BOTTOM)
 
 label = Label(frame1, text = "First frame",fg = "dark green", width =70, height = 10)
 label.pack()
 label = Label(frame2, text = "Second frame",fg = "dark green", width =70, height = 10)
 label.pack()
 
 window.mainloop()
