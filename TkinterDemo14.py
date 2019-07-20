# Demo for message boxes
from tkinter import *
from tkinter.messagebox import *
root=Tk()
root.title("Message Boxes")
root.geometry("500x500")
root.wm_minsize(width=300,height=300)

#To Show some info It returns ok
print(showinfo("Information","Today is Thursday"))

#To Show warning message It returns ok
#showwarning("Warning","Hey Subscribe my Channel")

#To Show Error message It returns ok
#showerror("Error","You Have to Subscribe My Channel ")

root.mainloop()


