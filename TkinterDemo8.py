# Dynamical Content in a Label
import tkinter as tk

def disp():
    print("My Name is Mani")


window = tk.Tk()
window.title("Welcome here")

button1 = tk.Button(window,
                   text="QUIT",
                   fg="red",
                   command=quit)
button1.pack(side=tk.LEFT)

button2 = tk.Button(window,
                   text="Hello",
                   command=disp)
button2.pack(side=tk.RIGHT)

window.mainloop()
