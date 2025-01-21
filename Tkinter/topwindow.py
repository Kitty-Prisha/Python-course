from tkinter import *
window=Tk()
window.geometry("400x400")
window.title("Root window")
def top():
    Topwindow=Toplevel()
    Topwindow.geometry("180x180")
    Topwindow.title("Top window")
    label=Label(Topwindow,text="This is a top level window")
    label.pack()
root=Label(window,text="This is a root window") 
button=Button(window,text="Click here",command=top)
button.pack()
window.mainloop()   