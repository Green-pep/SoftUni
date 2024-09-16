import tkinter
from tkinter import *
from tkinter import ttk


def creating_name():
    name_for_file = text_entry.get()
    name_for_file = name_for_file.split()
    new_name = []
    for word in name_for_file:
        word = word.lower()
        new_name.append(word)
    return "_".join(new_name)


def update_label():
    result = creating_name()
    result_label.config(text=result)


def color_mode():
    global is_dark_mode
    if is_dark_mode:
        window.config(background="#092635")
        is_dark_mode = False
    else:
        window.config(background="#e4e5f1")
        is_dark_mode = True


def copy_select():
    window.clipboard_clear()
    window.clipboard_append(result_label.cget("text"))


window = Tk()
window.geometry("500x500")
window.title("Name Creator")
window.config(background="#e4e5f1")
is_dark_mode = True

style = ttk.Style()
style.configure('TButton', font=('Arial', 10), borderwidth='4')
style.map('TButton', foreground=[('active', '!disabled', 'green')], background=[('active', 'black')])

text_entry = tkinter.Entry(master=window, width=30, font=('Arial', 12), fg='black', borderwidth=2, relief=tkinter.FLAT)
text_entry.grid(row=0, column=0, columnspan=2, padx=20, pady=10, sticky='ew')

create_name_button = tkinter.Button(window, text="Create Name", command=update_label)
create_name_button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

change_mode_button = tkinter.Button(window, text="Change Mode", command=color_mode)
change_mode_button.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

result_label = tkinter.Label(window, font=('Arial', 12), fg='black', borderwidth=2, relief=tkinter.GROOVE)
result_label.grid(row=2, column=0, columnspan=2, padx=20, pady=10, sticky='ew')

copy_button = tkinter.Button(window, text="Copy Result", command=copy_select)
copy_button.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky='ew')

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)


window.mainloop()


getattr()
