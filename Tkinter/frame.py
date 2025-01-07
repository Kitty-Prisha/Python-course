from tkinter import *
window=Tk()
window.title("Frame")
window.geometry('400x400')
frame=Frame(master=window, bg="yellow", height=100,width=100, relief=SUNKEN )
frame.place(x=50, y=200)
window.mainloop()