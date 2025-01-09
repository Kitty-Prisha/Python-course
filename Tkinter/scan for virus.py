from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("200x200")
window.title("Alert")
def msg():
    messagebox.showwarning("WARNING","Virus detected!")
button=Button(text="Scan for virus",command=msg)
button.place(x=80,y=80)
window.mainloop()
