# from tkinter import *
from tkinter import Toplevel, Button, TOP, IntVar, StringVar, Label, Text, W, CENTER, OptionMenu, PhotoImage
from main import *
from methods import *

# Colors
offWhite = "#FAF9F6"
back = "#CFA3F2"

def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration

def close_win(root):
    root.destroy()

def popup_three(root, text1, text2, text3, table):
    popup = Toplevel(root)
    popup.geometry("450x250")

    value1_prompt = Label(popup,text = text1, font=("Roboto", 20), bg=back, fg = offWhite)
    value1_prompt.place(relx=.1, rely = .3, anchor = W)
    value1 = Text(popup, width=20, height = 1)
    value1.place(relx=.3, rely=.3, anchor=W)

    value2_prompt = Label(popup,text = text2, font=("Roboto", 20), bg=back, fg = offWhite)
    value2_prompt.place(relx=.1, rely = .35, anchor = W)
    value2 = Text(popup, width=40, height = 1)
    value2.place(relx=.3, rely=.35, anchor=W)

    value3_prompt = Label(popup,text = text3, font=("Roboto", 20), bg=back, fg = offWhite)
    value3_prompt.place(relx=.1, rely = .4, anchor = W)
    value3 = Text(popup, width=40, height = 1)
    value3.place(relx=.3, rely=.4, anchor=W)

    submit = Button(popup, text="Submit", command=lambda:add(popup, table, value1, value2, value3))
    submit.place(relx=.9, rely=.5, anchor=CENTER)

def addBooks(root):
    # Create cards page, user can input manually front and back / word and desc to cards
    cleanPage(root)
    global idvar
    idvar = IntVar()
    global titlevar
    titlevar = StringVar()
    # global cardName

    desc = Label(root, text="Add book details:", font=("Roboto", 30), bg=back, fg = offWhite)
    desc.place(relx=.5, rely=.15, anchor=CENTER)

    idPrompt = Label(root,text = "Book id:", font=("Roboto", 20), bg=back, fg = offWhite)
    idPrompt.place(relx=.1, rely = .3, anchor = W)
    id = Text(root, width=20, height = 1)
    id.place(relx=.3, rely=.3, anchor=W)

    # if id already existed, create a pop up warning

    titlePrompt = Label(root,text = "Title:", font=("Roboto", 20), bg=back, fg = offWhite)
    titlePrompt.place(relx=.1, rely = .35, anchor = W)
    title = Text(root, width=40, height = 1)
    title.place(relx=.3, rely=.35, anchor=W)

    authPrompt = Label(root, text = "Author Name:", font=("Roboto", 20), bg = back, fg = offWhite)
    authPrompt.place(relx=.1, rely = .4, anchor = W)
    author_name = StringVar()
    author_list = dropDown("author_details")
    # print(type(author_list))
    author_dropdown = OptionMenu(root, author_name, *author_list)    
    author_dropdown.place(relx=.3, rely=.4, anchor=W)

    pubPrompt = Label(root,text = "Publisher:", font=("Roboto", 20), bg=back, fg = offWhite)
    pubPrompt.place(relx=.1, rely = .45, anchor = W)
    pub = StringVar()
    pub_list = dropDown("publisher_details")
    # print(type(pub_list))
    pub_dropdown = OptionMenu(root, pub, *pub_list)
    pub_dropdown.place(relx=.3, rely=.45, anchor=W)

    isbnPrompt = Label(root,text = "ISBN:", font=("Roboto", 20), bg=back, fg = offWhite)
    isbnPrompt.place(relx=.1, rely = .5, anchor = W)
    isbn = Text(root, width=40, height = 1)
    isbn.place(relx=.3, rely=.5, anchor=W)
    
    groupPrompt = Label(root,text = "Group:", font=("Roboto", 20), bg=back, fg = offWhite)
    groupPrompt.place(relx=.1, rely = .55, anchor = W)
    group = StringVar()
    group_list = dropDown("group_details")
    # print(type(group_list))
    group_dropdown = OptionMenu(root, group, *group_list)
    group_dropdown.place(relx=.3, rely=.55, anchor=W)

    statusPrompt = Label(root,text = "Status:", font=("Roboto", 20), bg=back, fg = offWhite)
    statusPrompt.place(relx=.1, rely = .6, anchor = W)
    status = StringVar()
    status_list = dropDown("status_details")
    # print(type(status_list))
    status_dropdown = OptionMenu(root, status, *status_list)
    status_dropdown.place(relx=.3, rely=.6, anchor=W)

    damagesPrompt = Label(root,text = "Damages:", font=("Roboto", 20), bg=back, fg = offWhite)
    damagesPrompt.place(relx=.1, rely = .65, anchor = W)
    damages = StringVar()
    damages_list = dropDown("damages_details")
    # print(type(status_list))
    damages_dropdown = OptionMenu(root, damages, *damages_list)
    damages_dropdown.place(relx=.3, rely=.65, anchor=W)

    global btnPic
    btnPic = PhotoImage(file = "images/submitBtn.png")
    btn = Button(root, image = btnPic, command=lambda:print(pub.get()), borderwidth=0, compound = TOP)

    # btn = Button(root, image = btnPic, command=lambda: upload(root, id, title, author_name,pub, isbn, group, status, damages), borderwidth=0, compound = TOP)
    btn.place(relx=.9, rely=.85, anchor=CENTER)

    # btn1 = Button(root, text="drop", command=lambda:author_search(root, clicked.get()))
    # btn1.place(relx = .2, rely = .85, anchor = CENTER)

    # Check if author exits or not
    # if not, pop up a window and prompt first and last name, the id is the same
