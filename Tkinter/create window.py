from tkinter import *
window=Tk()
window.title("Window")
window.geometry('400x400')
lbl=Label(text="Enter your name",fg='white', bg='black',height=3, width=20)
lbl.pack()
entry=Entry(fg='white',bg='grey',width=20)
entry.place(x=150,y=100)
button=Button(fg='black',bg='grey',text='submit')
button.pack()
def display():
    
window.mainloop()