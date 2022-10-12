from tkinter import *
from tkinter import messagebox
from turtle import bgcolor
from webbrowser import BackgroundBrowser

class Pizza:
    def __init__(self, pizza):
        
        self.pizza = pizza
        pizza.title('Pizza Order')

        pizza.background = bgcolor('pink')

        self.label = Label(pizza, text="Order Your Campbell's Pizza!")
        self.label.pack()

        self.name_label = Label(pizza, text='Please Enter Your Name:')
        self.name_label.pack()

        self.name_entry = Entry(pizza)
        self.name_entry.pack()

        self.crust_label = Label(pizza, text='What Type of Crust?')
        self.crust_label.pack()

        self.crust_var = StringVar(pizza)
        self.crust_var.set('Thick Crust')
        self.crust_option = OptionMenu(pizza, self.crust_var, 'Thick Crust', 'Thin Crust', 'Cheese Stuffed Crust')
        self.crust_option.pack()

        self.sauce_label = Label(pizza, text='What Type of Sauce?')
        self.sauce_label.pack()

        self.sauce_var = StringVar(pizza)
        self.sauce_var.set('Red Sauce')
        self.sauce_option = OptionMenu(pizza, self.sauce_var, 'Red Sauce', 'Green Sauce','No Sauce')
        self.sauce_option.pack()

        self.toppings_label = Label(pizza, text='Any Toppings Today?')
        self.toppings_label.pack()

        self.parmesan_var = IntVar()
        self.parmesan_check = Checkbutton(pizza, text='Parmesan Cheese', variable=self.parmesan_var)
        self.parmesan_check.pack()
        
        self.pepperoni_var = IntVar()
        self.pepperoni_check = Checkbutton(pizza, text='Pepperoni', variable=self.pepperoni_var)
        self.pepperoni_check.pack()

        self.basil_var = IntVar()
        self.basil_check = Checkbutton(pizza, text='Basil', variable=self.basil_var)
        self.basil_check.pack()

        self.pineapple_var = IntVar()
        self.pineapple_check = Checkbutton(pizza, text='Pineapple', variable=self.pineapple_var)
        self.pineapple_check.pack()

        self.calculate_button = Button(pizza, text='Calculate', command=self.calculate)
        self.calculate_button.pack()

        self.quit_button = Button(pizza, text='Quit', command=pizza.quit)
        self.quit_button.pack()

    def calculate(self):
        name = self.name_entry.get()
        crust = self.crust_var.get()
        sauce = self.sauce_var.get()
        parmesan = self.parmesan_var.get()
        pepperoni = self.pepperoni_var.get()
        basil = self.basil_var.get()
        pineapple = self.pineapple_var.get()

        total = 0
        if crust == 'Thin':
            total += 12
        elif crust == 'Thick':
            total += 14
        elif crust == 'Stuffed':
            total += 15
        
        if sauce == 'Red Sauce':
            total =+ 1
        if sauce == 'Green Sauce':
            total +=2
        if sauce == 'No Sauce':
            total =+ 0
        
        if parmesan ==1:
            total += 2
        if pepperoni == 1:
            total += 2
        if basil == 1:
            total += 2
        if pineapple == 1:
            total += 1

        messagebox.showinfo('Total', 'Total: $' + str(total) + '\nName: ' + name)

root = Tk()
my_gui = Pizza(root)
root.mainloop()