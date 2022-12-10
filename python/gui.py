import tkinter as tk
from tkinter import *


root = tk.Tk()
root.geometry('350x200')
root.title('Login Form')
label1 = tk.Label(root, text='Username: ')
label1.grid()
label2 = tk.Label(root, text='Password: ')
print(type(label1))
label2.grid()
Username = tk.Entry(root, width=20)
Password = tk.Entry(root, width=20)

Username.grid(row=0, column=1)
Password.grid(row=1, column=1)


def SubmitForm(Username, Password):
    user_list = []
    pass_list = []
    if Username not in user_list and Password not in pass_list:
        user_list.append(Username)
        pass_list.append(Password)
        next_window = Toplevel(root)
        next_window.geometry('350x200')
        next_window.title('Showing User Details')
        label5 = tk.Label(next_window, text='Username:')
        label5.grid(row=0, column=0)
        label6 = tk.Label(next_window, text='Password:')
        label6.grid(row=1, column=0)
        label3 = tk.Label(next_window, text=Username)
        label3.grid(row=0, column=1)
        label4 = tk.Label(next_window, text=Password)
        label4.grid(row=1, column=1)


def print_details():
    Uss = Username.get()
    passw = Password.get()
    SubmitForm(Uss, passw)


Button = tk.Button(root, text='Click for Submit', command=print_details)
Button.grid(row=2, column=1)
root.mainloop()
