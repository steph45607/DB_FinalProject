# from tkinter import *
from tkinter import ACTIVE, END, Entry, Event, Listbox, Toplevel, Button, TOP, IntVar, StringVar, Label, Text, W, CENTER, OptionMenu, PhotoImage
from tkinter.ttk import Combobox
from main import *
from methods import *


# Colors
offWhite = "#FAF9F6"
back = "#CFA3F2"

# def update(list):
#     book_list = searchBooks("book_details")
#     list.delete(0, END)

#     for item in book_list:
#         list.insert(END, item)

# # def fillout(event):
# #     my_entry.delete(0, END)

# #     entry.insert(0, list.get(ACTIVE))

# def searchFill(root):
#     my_label = Label(root, text= "Start typing...", font= ("Helvetica", 14), fg = "grey")

#     my_label.pack(pady=20)

#     my_entry = Entry(root, font=("Helvetica", 20))
#     my_entry.pack()

#     my_list = Listbox(root, width = 50)
#     my_list.pack(pady=40)

#     update(my_list)

#     # my_list.bind("<<ListboxSelect>>", fillout)

def search_records(root):
    pubPrompt = Label(root,text = "Search:", font=("Roboto", 20), bg=back, fg = offWhite)
    pubPrompt.place(relx=.1, rely = .45, anchor = W)
    pub = StringVar()
    pub_list = searchBooks("book_details")
    # print(type(pub_list))
    pub_dropdown = OptionMenu(root, pub, *pub_list)
    pub_dropdown.place(relx=.3, rely=.45, anchor=W)

    test = StringVar()
    country = Combobox(root, textvariable=test)
    country["values"] = pub_list
    country["state"] = "normal"
    country.place(relx=.3, rely=.55, anchor=W)

    btn = Button(root, text="submit", command = lambda:print(test.get()))
    btn.place(relx=0.5, rely=0.8, anchor=CENTER)