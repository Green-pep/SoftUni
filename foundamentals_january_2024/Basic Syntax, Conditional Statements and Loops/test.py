import tkinter
from tkinter import *

def creating_name():
    name_for_file = text_entry.get()
    name_for_file = name_for_file.split()
    new_name = []
    for word in name_for_file:
        word = word.lower()
        new_name.append(word)
    print(new_name)


window = Tk()
window.geometry("500x500")
window.title("Name Creator")
window.config(background="#e4e5f1")
is_dark_mode = True

text_entry = tkinter.Entry(window)
text_entry.pack()

button = Button(window, text="Change Name", command=creating_name)
button.pack(side=tkinter.LEFT, padx=10, pady=10)

window.mainloop()
