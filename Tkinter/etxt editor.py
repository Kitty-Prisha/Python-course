#import libraries
from tkinter import *
import tkinter.filedialog import askopenfilename,asksaveasfilname
#create window
window=Tk()
window.title("Text editor")
window.geometry("500x500")
window.rowconfigure(0,minisize=800,weight=1)
window.columnconfigure(1,minisize=800,weight=1)
txt_edit = Text(window)

fr_buttons = Frame(window, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="Open", command=open_file)

btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()


