from tkinter import *
window=Tk()
window.title("Window")
window.geometry('400x400')
lbl=Label(text="Enter your name",fg='white', bg='black',height=3, width=20)
lbl.pack()
entry=Entry(fg='white',bg='grey',width=20)
entry.place(x=150,y=100)


name_entry=Entry()
def display():
    name=name_entry.get()
    messgae="Welcome to application!"
    greet="Hello"+name+"/n"
    text_box.insert(END,greet)
    text_box.insert(END,messgae)
    text_box=Text(height=3)
    text_box.pack()
button=Button(fg='black',bg='grey',text='Begin',command=display())
button.pack()


window.mainloop()