import tkinter
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() 

        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.radio_var = tkinter.IntVar()

        self.rb1 = tkinter.Radiobutton(self.topframe,text='Option1',variable=self.radio_var,value=1)
        self.rb2 = tkinter.Radiobutton(self.topframe,text='Option2',variable=self.radio_var,value=2)
        self.rb3 = tkinter.Radiobutton(self.topframe,text='Option3',variable=self.radio_var,value=3)

        self.rb2.select()

        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()

        self.OKbutton = tkinter.Button(self.bottomframe,text='OK!',command=self.show_choice)
        self.RESETbutton = tkinter.Button(self.bottomframe,text='Reset!',command=self.rb1.select)
        self.QUITbutton = tkinter.Button(self.bottomframe,text='Quit',command=self.main_window.destroy)

        self.OKbutton.pack(side='left')
        self.RESETbutton.pack(side='left')
        self.QUITbutton.pack(side='right')

        self.topframe.pack(side='top')
        self.bottomframe.pack(side='top')

        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo('Selection','You have selected option' + str(self.radio_var.get()))

myGUI = MyGUI()

print('Hi there!')







