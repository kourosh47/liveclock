from tkinter import *
import time
#-----------------------------------------------------------------------------------------------------------
class app:
     def __init__(self):   
        self.win=Tk()
        self.win.title("Time show")
        self.win.maxsize(150,100)
        self.win.minsize(150,100)
        self.win.geometry("150x100")
        #-----------------------------------------------------------------------------------------------------------
        self.intro=Label(text="",bg="red",fg="white",font="bold",height=3,width=15)
        self.intro.place(x=5,y=5)
        #-----------------------------------------------------------------------------------------------------------
        self.quitbut=Button(text="Back",bg="blue",fg="white",command=self.win.destroy)
        self.quitbut.place(x=57,y=70)
        #-----------------------------------------------------------------------------------------------------------
        self.time_upd()
        self.win.mainloop()
     def time_upd(self):
        now=time.strftime("%H:%M:%S")
        self.intro.configure(text=now)
        self.win.after(1000,self.time_upd)   

ino=app()
