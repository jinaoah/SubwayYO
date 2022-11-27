from tkinter import *

window = Tk()
window.geometry("600x600+200+200")

f1 = Frame(window)
f2 = Frame(window)
f3 = Frame(window)

f1.focus_set()
f2.focus_set()
f1.grid(row=0, column =0, sticky="nsew")
f2.grid(row=0, column =0, sticky="nsew")
f3.grid(row=0, column =0, sticky="nsew")

def openFrame(f):
    f.tkraise()

btnF1 = Button(f3, 
    text="F3 -> F1",    
    padx=10, 
    pady=10,
    command=lambda:[openFrame(f1)])
btnF2 = Button(f1, 
    text="F1 -> F2",    
    padx=10, 
    pady=10,
    command=lambda:[openFrame(f2)])
btnF3 = Button(f2, 
    text="F2 -> F3",    
    padx=10, 
    pady=10,
    command=lambda:[openFrame(f3)])

btnF1.pack()
btnF2.pack()

openFrame(f1)
window.mainloop()