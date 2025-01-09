from tkinter import *
window=Tk()
window.title("Even handler")
window.geometry("100x100")
def handle(event):
    print(event.char)
window.bind("<Key>", handle)  
def handleclick(event):
    print("The button was clicked")
button=Button(text="Click me!")
button.pack()
button.bind("<Button-1>", handleclick)
window.mainloop()
    