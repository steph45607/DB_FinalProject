from tkinter import *

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

    btnPic = PhotoImage(file = "images/smallBtn.png")

    # photo = btnPic.subsample(1,1)
    cancelBtn = Button(root, image = btnPic, command=lambda: upload(id, title), borderwidth=0)
    # cancelBtn.config(image = photo)
    # cancelBtn.image = btnPic
    # cancelBtn.place(relx=.2, rely=.6, anchor=CENTER)
    cancelBtn.grid(row = 1, column = 1)
