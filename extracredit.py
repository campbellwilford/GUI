import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk() 

        self.main_window.geometry('500x200')
        self.main_window.title('InputBox Demo')

        self.topframe = tkinter.Frame(self.main_window)
        self.midframe = tkinter.Frame(self.main_window)
        self.bottomframe = tkinter.Frame(self.main_window)

        self.prompt_label1 = tkinter.Label(self.topframe,text='Enter the score for test 1:')
        self.prompt_label2 = tkinter.Label(self.topframe,text='Enter the score for test 2:')
        self.prompt_label3 = tkinter.Label(self.topframe,text='Enter the score for test 3:')
        
        self.kilo_entry = tkinter.Entry(self.topframe,width=10)

        self.desc_label = tkinter.Label(self.midframe,text='Converted to Miles:')

        self.miles_var = tkinter.StringVar()
        
        self.miles_label = tkinter.Label(self.midframe,textvariable=self.miles_var)

        self.desc_label.pack(side='left')
        self.miles_label.pack(side='left')
        

        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')

        self.topframe.pack(side='top')
        self.midframe.pack(side='top')
        self.bottomframe.pack(side='top')

        self.calc_button = tkinter.Button(self.main_window,text='Convert',command=self.convert)
        self.quitbutton = tkinter.Button(self.main_window,text='Quit',command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quitbutton.pack(side='right')

        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214,2)

        #tkinter.messagebox.showinfo('Results', str(kilo) + 'kilometers is equal to ' + str(miles) + 'miles')

        self.miles_var.set(miles)

myGUI = MyGUI()

print('Hi there!')




