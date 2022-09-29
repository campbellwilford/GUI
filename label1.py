import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() 

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.Label1 = tkinter.Label(self.main_window,text='Hello World')
        self.Label2 = tkinter.Label(self.main_window,text='This is my GUI program')

        self.Label1.pack()
        self.Label2.pack()

        tkinter.mainloop()

myGUI = MyGUI()

print('Hi there!')