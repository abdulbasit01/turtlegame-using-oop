from tkinter import *

import tkinter.ttk
root=Tk()
root.title('startuppage')
root.geometry('450x130')
root.configure(bg='powder blue')
#=================turtle 1 =====================

class bstartup(object):
    def __init__(self):
        self.label=Label(root ,bg='red',text='SELECT MODE OF THE GAME', font=('calibiri', 20, 'bold italic'))
        self.label.pack(fill=X)
    def funct():
        root.destroy()
        import playermoving
#=================turtle 2 =====================
class astartup():
    def funct2():
        root.destroy()
        import bothmoving
b=bstartup()
btn=Checkbutton(root, text="beginner ", command=bstartup.funct)
btn.pack(fill=X)

btn=Checkbutton(root, text="advance ", command=astartup.funct2)
btn.pack(fill=X)

root.mainloop()
