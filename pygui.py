#python 3
from tkinter import *
from tkinter.messagebox import showinfo

def reply():
    showinfo(title='nihaoa',message='我好吗')

window = Tk()
button =Button(window,text='按压',command=reply())
button.pack()
window.mainloop()
#Label(text='Spam').pack()
#mainloop()