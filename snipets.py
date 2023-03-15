from tkinter import *

root = Tk()

user_variable = StringVar(root)


def print_name():
    entry_field = field1.get()
    result['text'] = f'Labas, {entry_field}'
    user_variable.set(f'Labas, {entry_field}')
    status['text'] = 'Sukurta'


def clear_field():
    result['text'] = ''
    status['text'] = 'Išvalyta'


def restore_field():
    result['text'] = user_variable.get()
    status['text'] = 'Atkurta'


meniu = Menu(root)
root.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

meniu.add_cascade(label='Parinktys', menu=submeniu)
submeniu.add_command(label='Išvalyti', command=clear_field)
submeniu.add_command(label='Atkurti', command=restore_field)
submeniu.add_separator()
submeniu.add_command(label='Išeiti', command=root.quit)

lable1 = Label(root, text='Įveskite vardą')
field1 = Entry(root)
button = Button(root, text='Patvirtinti', command=print_name)
result = Label(root, text='')
status = Label(root, text='', bd=2, relief=SUNKEN, anchor=W)
root.bind('<Return>', lambda event: print_name())
root.bind('<Escape>', lambda event: root.destroy())

lable1.grid(row=0, column=0)
field1.grid(row=0, column=1)
button.grid(row=0, column=2)
result.grid(row=1, columnspan=3)
status.grid(row=2, columnspan=3, sticky=W + E)
root.mainloop()

# class Demo1:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text='New Window', width=25, command=self.new_window)
#         self.frame.pack()
#
#     def new_window(self):
#         self.newWindow = tk.Toplevel(self.master)
#         self.app = Demo2(self.newWindow)
#
#
# class Demo2:
#     def __init__(self, master):
#         self.master = master
#         self.frame = tk.Frame(self.master)
#         self.button1 = tk.Button(self.frame, text='Quit', width=25, command=self.close_windows)
#         self.frame.pack()
#
#     def close_windows(self):
#         self.master.destroy()
#
#
# def main():
#     root = tk.Tk()
#     app = Demo1(root)
#     root.mainloop()
#
#
# if __name__ == '__main__':
#     main()
