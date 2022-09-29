import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() 

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.Label1 = tkinter.Label(self.topframe,text='John')
        self.Label2 = tkinter.Label(self.topframe,text='Jim')
        self.Label3 = tkinter.Label(self.topframe,text='Jerry')

        self.Label1.pack(side='left')
        self.Label2.pack(side='left')
        self.Label3.pack(side='left')

        self.Label4 = tkinter.Label(self.bottomframe,text='Jill')
        self.Label5 = tkinter.Label(self.bottomframe,text='Janie')
        self.Label6 = tkinter.Label(self.bottomframe,text='Jen')

        self.Label4.pack(side='left')
        self.Label5.pack(side='left')
        self.Label6.pack(side='left')

        self.topframe.pack()
        self.bottomframe.pack()

        self.mybutton = tkinter.Button(self.main_window,text='Click Me!',command=self.do_something())
        self.quitbutton = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)

        self.mybutton.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Responde','Thanks for clicking me!')

myGUI = MyGUI()

print('Hi there!')