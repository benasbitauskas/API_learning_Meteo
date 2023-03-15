from tkinter import *
from main import show_forecast
root = Tk()

user_variable = StringVar(root)


def print_forecast():
    entry_field = field1.get()
    forecast = show_forecast(entry_field)
    result['text'] = f'Prognozė {forecast} C'
    user_variable.set(f'Prognozė {forecast} C')
    status['text'] = 'print_forecast'


lable1 = Label(root, text='Miestas: ')
field1 = Entry(root)
button1 = Button(root, text='Gauti prognozę')
result = Label(root, text='')
status = Label(root, text='', bd=2, relief=SUNKEN, anchor=W)
root.bind('<Return>', lambda event: print_forecast())
root.bind('<Escape>', lambda event: root.destroy())

lable1.grid(row=0, column=0)
field1.grid(row=0, column=1)
button1.grid(row=0, column=2)
result.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W + E)
root.mainloop()
