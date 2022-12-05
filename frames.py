from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

from main import *
from app import *

# Colors
offWhite = "#FAF9F6"
back = "#35838B"

def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration


def createCards(root):
    # Create cards page, user can input manually front and back / word and desc to cards
    cleanPage(root)
    global idvar
    idvar = IntVar()
    global titlevar
    titlevar = StringVar()
    # global cardName

    desc = Label(root, text="Enter the word:", font=("Roboto", 30), bg=back)
    desc.place(relx=.25, rely=.2, anchor=CENTER)

    id = Text(root, width=20, height = 1)
    id.place(relx=.25, rely=.3, anchor=CENTER)

    title = Text(root, width=20, height = 1)
    title.place(relx=.75, rely=.3, anchor=CENTER)

    global btnPic

    btnPic = PhotoImage(file = "submitBtn.png")

    # photo = btnPic.subsample(1,1)
    btn = Button(root, image = btnPic, command=lambda: upload(id, title), borderwidth=0, compound = TOP)
    # cancelBtn.config(image = photo)
    # cancelBtn.image = btnPic
    btn.place(relx=.2, rely=.6, anchor=CENTER)
    # cancelBtn.grid(row = 1, column = 1)
