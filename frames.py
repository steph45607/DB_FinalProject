from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

from main import *
from app import *

# Colors
offWhite = "#FAF9F6"
back = "#CFA3F2"

def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration


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

    pubPrompt = Label(root,text = "Publisher:", font=("Roboto", 20), bg=back, fg = offWhite)
    pubPrompt.place(relx=.1, rely = .4, anchor = W)
    pub = Text(root, width=40, height = 1)
    pub.place(relx=.3, rely=.4, anchor=W)

    authPrompt = Label(root,text = "Author_id:", font=("Roboto", 20), bg=back, fg = offWhite)
    authPrompt.place(relx=.1, rely = .45, anchor = W)
    auth = Text(root, width=40, height = 1)
    auth.place(relx=.3, rely=.45, anchor=W)

    isbnPrompt = Label(root,text = "ISBN:", font=("Roboto", 20), bg=back, fg = offWhite)
    isbnPrompt.place(relx=.1, rely = .5, anchor = W)
    isbn = Text(root, width=40, height = 1)
    isbn.place(relx=.3, rely=.5, anchor=W)
    
    groupPrompt = Label(root,text = "Group:", font=("Roboto", 20), bg=back, fg = offWhite)
    groupPrompt.place(relx=.1, rely = .55, anchor = W)
    group = Text(root, width=40, height = 1)
    group.place(relx=.3, rely=.55, anchor=W)

    statusPrompt = Label(root,text = "Status:", font=("Roboto", 20), bg=back, fg = offWhite)
    statusPrompt.place(relx=.1, rely = .6, anchor = W)
    status = Text(root, width=40, height = 1)
    status.place(relx=.3, rely=.6, anchor=W)

    clicked = StringVar()
    options = dropDown()
    drop = OptionMenu(root, clicked, *options)
    drop.place(relx = .5, rely = .85, anchor= CENTER)

    global btnPic
    btnPic = PhotoImage(file = "images/submitBtn.png")
    btn = Button(root, image = btnPic, command=lambda: upload(id, title, auth, pub, status, isbn, group), borderwidth=0, compound = TOP)
    btn.place(relx=.9, rely=.85, anchor=CENTER)

    # Check if author exits or not
    # if not, pop up a window and prompt first and last name, the id is the same
