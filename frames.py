# from tkinter import *
# from tkinter import Toplevel, Button, TOP, IntVar, StringVar, Label, Text, W, CENTER, OptionMenu, PhotoImage, font
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter.messagebox import askyesno
from main import *
from methods import *
import ttk

# Colors
offWhite = "#FAF9F6"
myColor = "#1A371B"

# To clean the root window, used to change between frames
def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children():  # To know the widgets used in that page
        widget.destroy()  # To delete all the widgets with iteration


# Destroy the window
def close_win(root):
    root.destroy()


def invalidPopup(root):
    invalidpop = Toplevel(root)
    invalidpop.geometry("400x200")
    invalidpop.resizable(False, False)
    invalidpop.configure(bg="white")
    invalidpop.title("Login Failed")

    Label(
        invalidpop,
        font=(myFont, 15),
        text="Invalid username or password !",
        background="white",
        foreground="black",
    ).place(relx=0.15, rely=0.27)
    Label(
        invalidpop,
        font=(myFont, 15),
        text="Please try again. ",
        background="white",
        foreground="black",
    ).place(relx=0.15, rely=0.4)

    def close():
        invalidpop.destroy()

    backButton = backButton = Button(
        invalidpop,
        text="  OK  ",
        command=close,
        foreground="white",
        background="#2C602E",
        font=(myFont, 15),
    )
    backButton.place(relx=0.4, rely=0.6)


def landingPage(root):
    cleanPage(root)
    global myFont
    myFont = font.Font(family="Helvetica")
    # Add image file
    global background
    background = PhotoImage(file="images/backgroundLandingPage.png")
    global logo
    logo = PhotoImage(file="images/logo.png")
    global qr
    qr = PhotoImage(file="images/qr.png")
    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=0, y=0)

    logolabel = Label(root, image=logo)
    logolabel.place(relx=0.143, rely=0.38)

    userButton = Button(
        root,
        font=(myFont, 18),
        command=lambda: loginUser(root),
        text="  User  ",
        background="#2C602E",
        foreground="white",
    )
    userButton.place(relx=0.18, rely=0.6)

    adminButton = Button(
        root,
        font=(myFont, 18),
        command=lambda: loginAdmin(root),
        text=" Admin ",
        background="#2C602E",
        foreground="white",
    )
    adminButton.place(relx=0.29, rely=0.6)

    textWelcome = Label(
        root,
        font=(myFont, 18),
        text="Welcome to BookStack",
        bg="#1A371B",
        foreground="white",
    )
    textWelcome.place(relx=0.63, rely=0.22)

    textIntro1 = Label(
        root,
        font=(myFont, 10),
        text="BookStack is an application made as the final project ",
        bg="#1A371B",
        foreground="white",
    )
    textIntro1.place(relx=0.63, rely=0.31)

    textIntro2 = Label(
        root,
        font=(myFont, 10),
        text="of Maria Clarin, Rachel Anastasia Wijaya, and Stephanie",
        bg="#1A371B",
        foreground="white",
    )
    textIntro2.place(relx=0.63, rely=0.34)

    textIntro3 = Label(
        root,
        font=(myFont, 10),
        text="Staniswinata for Database Technology.",
        bg="#1A371B",
        foreground="white",
    )
    textIntro3.place(relx=0.63, rely=0.37)

    textIntro4 = Label(
        root,
        font=(myFont, 10),
        text="It is designed to manage library logs and documentation ",
        bg="#1A371B",
        foreground="white",
    )
    textIntro4.place(relx=0.63, rely=0.45)

    textIntro5 = Label(
        root, font=(myFont, 10), text="systems", bg="#1A371B", foreground="white"
    )
    textIntro5.place(relx=0.63, rely=0.48)

    qrlabel = Label(root, image=qr, background="#1A371B")
    qrlabel.place(relx=0.618, rely=0.54)

    textIntro6 = Label(
        root,
        font=(myFont, 10),
        text="Visit our GitHub Repository for this project ",
        bg="#1A371B",
        foreground="white",
    )
    textIntro6.place(relx=0.701, rely=0.56)

    textIntro7 = Label(
        root,
        font=(myFont, 10),
        text="by scanning the QR Code!",
        bg="#1A371B",
        foreground="white",
    )
    textIntro7.place(relx=0.701, rely=0.59)


def loginAdmin(root):
    cleanPage(root)
    root.title("Enter Admin Login Credentials")

    usernameVar = StringVar()
    passwordVar = StringVar()

    def adminCheck():
        username = usernameVar.get()
        password = passwordVar.get()

        if username == "admin" and password == "admin123":
            print("The name is : " + username)
            print("The password is : " + password)
            menuPage(root)
        else:
            invalidPopup(root)

    Label(
        root,
        font=(myFont, 15),
        text="Username : ",
        background="#2C602E",
        foreground="white",
    ).place(relx=0.17, rely=0.3)
    usernameInput = Entry(root, textvariable=usernameVar, font=(myFont, 13, "normal"))
    usernameInput.place(relx=0.35, rely=0.32, width=270)

    Label(
        root,
        font=(myFont, 15),
        text="Password : ",
        background="#2C602E",
        foreground="white",
    ).place(relx=0.17, rely=0.45)
    passwordInput = Entry(
        root, textvariable=passwordVar, font=(myFont, 13, "normal"), show="*"
    )
    passwordInput.place(relx=0.35, rely=0.47, width=270)

    loginButton = Button(
        root,
        text="Login",
        command=adminCheck,
        foreground="#2C602E",
        background="white",
        font=(myFont, 15),
    )
    loginButton.place(relx=0.35, rely=0.6)

    backButton = backButton = Button(
        root,
        text="Back",
        command=lambda: landingPage(root),
        foreground="#2C602E",
        background="white",
        font=(myFont, 10),
    )
    backButton.place(relx=0.01, rely=0.02)


def loginUser(root):
    cleanPage(root)
    root.title("Enter User Login Credentials")

    usernameVar = StringVar()
    passwordVar = StringVar()

    def userCheck():
        username = usernameVar.get()
        password = passwordVar.get()

        if username == "user" and password == "user123":
            print("The name is : " + username)
            print("The password is : " + password)
        else:
            invalidPopup(root)

    Label(
        root,
        font=(myFont, 15),
        text="Username : ",
        background="#2C602E",
        foreground="white",
    ).place(relx=0.17, rely=0.3)
    usernameInput = Entry(root, textvariable=usernameVar, font=(myFont, 13, "normal"))
    usernameInput.place(relx=0.35, rely=0.32, width=270)

    Label(
        root,
        font=(myFont, 15),
        text="Password : ",
        background="#2C602E",
        foreground="white",
    ).place(relx=0.17, rely=0.45)
    passwordInput = Entry(
        root, textvariable=passwordVar, font=(myFont, 13, "normal"), show="*"
    )
    passwordInput.place(relx=0.35, rely=0.47, width=270)

    loginButton = Button(
        root,
        text="Login",
        command=userCheck,
        foreground="#2C602E",
        background="white",
        font=(myFont, 15),
    )
    loginButton.place(relx=0.35, rely=0.6)

    backButton = backButton = Button(
        root,
        text="Back",
        command=lambda: landingPage(root),
        foreground="#2C602E",
        background="white",
        font=(myFont, 10),
        borderwidth=0,
    )
    backButton.place(relx=0.01, rely=0.02)


def menuPage(root):
    cleanPage(root)
    global background
    background = PhotoImage(file="images/backgroundMenu.png")

    myFont = font.Font(family="Helvetica")
    myColor = "#1A371B"

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    # title for admin menu
    Label(
        root,
        font=("Helvetica Bold", 25),
        text=" Admin Menu ",
        background=myColor,
        foreground="white",
    ).place(relx=0.38, rely=0.1)

    # view transaction btn
    global tranBtnPhoto
    tranBtnPhoto = PhotoImage(file="images/transactionlist.png").subsample(8, 8)
    transactionBtn = Button(
        root,
        text="View Transactions ",
        image=tranBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 15),
        borderwidth=0,
    )
    transactionBtn.place(relx=0.23, rely=0.24, width=240)

    # add transaction btn
    global addTransBtnPhoto
    addTransBtnPhoto = PhotoImage(file="images/addtransaction.png").subsample(8, 8)
    addTransactionBtn = Button(
        root,
        text="Add Transactions  ",
        image=addTransBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 15),
        borderwidth=0,
    )
    addTransactionBtn.place(relx=0.23, rely=0.4, width=240)

    # view books btn
    global bookBtnPhoto
    bookBtnPhoto = PhotoImage(file="images/bookbtn.png").subsample(8, 8)
    bookBtn = Button(
        root,
        text=" View Books  ",
        image=bookBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 15),
        command=lambda: displayBooks(root),
        borderwidth=0,
    )
    bookBtn.place(relx=0.5, rely=0.24, width=240)

    # add books btn
    global addbookBtnPhoto
    addbookBtnPhoto = PhotoImage(file="images/addbook.png").subsample(8, 8)
    addBookBtn = Button(
        root,
        text=" Add Books  ",
        image=addbookBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 15),
        command=lambda: addBooks(root),
        borderwidth=0,
    )  # command=lambda:addBooks(root)
    addBookBtn.place(relx=0.5, rely=0.4, width=240)

    # confirmation popup message if want to log out
    def confirm(root):
        answer = askyesno(
            title="Log out confirmation",
            message="Are you sure that you want to log out?",
        )
        if answer:
            landingPage(root)

    # log out button
    backBtn = Button(
        root,
        text=" Log Out ",
        foreground="black",
        background="white",
        command=lambda: confirm(root),
        font=(myFont, 13),
        borderwidth=0,
    )
    backBtn.place(relx=0.9, rely=0.02)


def popup_three(root, text1, text2, text3, table):
    popup = Toplevel(root)
    popup.geometry("450x250")
    popup.config(bg="#2C602E")

    Label(
        popup,
        font=("Helvetica Bold", 23),
        text=f" Add new {table} value",
        background=myColor,
        foreground="white",
    ).place(relx=0.38, rely=0.1)

    value1_prompt = Label(
        popup, text=text1, font=("Helvetica", 15), bg=myColor, fg=offWhite
    )
    value1_prompt.place(relx=0.1, rely=0.3, anchor=W)
    value1 = Entry(popup, width=20)
    value1.place(relx=0.3, rely=0.3, width=500, anchor=W)

    value2_prompt = Label(
        popup, text=text2, font=("Helvetica", 15), bg=myColor, fg=offWhite
    )
    value2_prompt.place(relx=0.1, rely=0.5, anchor=W)
    value2 = Entry(popup, width=20)
    value2.place(relx=0.3, rely=0.5, width=500, anchor=W)

    value3_prompt = Label(
        popup, text=text3, font=("Helvetica", 15), bg=myColor, fg=offWhite
    )
    value3_prompt.place(relx=0.1, rely=0.7, anchor=W)
    value3 = Entry(popup, width=20)
    value3.place(relx=0.3, rely=0.7, width=500, anchor=W)

    submit = Button(
        popup,
        text="Create",
        command=lambda: add_three(popup, table, value1, value2, value3),
    )
    submit.place(relx=0.3, rely=0.9)


def addBooks(root):
    cleanPage(root)
    global background
    background = PhotoImage(file="images/backgroundMenu.png")

    myFont = font.Font(family="Helvetica")
    myColor = "#1A371B"

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 23),
        text=" Add Book Details ",
        background=myColor,
        foreground="white",
    ).place(relx=0.38, rely=0.1)

    # bookID input
    bookIDVar = StringVar()
    Label(
        root,
        font=(myFont, 15),
        text="Book ID   : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.18)
    id = Entry(
        root,
        textvariable=bookIDVar,
        font=(myFont, 13, "normal"),
    )
    id.place(relx=0.28, rely=0.205, width=500, anchor=W)

    # title Input
    titleVar = StringVar()
    Label(
        root,
        font=(myFont, 15),
        text="Title         : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.23)
    title = Entry(
        root,
        textvariable=titleVar,
        font=(myFont, 13, "normal"),
    )
    title.place(relx=0.28, rely=0.255, width=500, anchor=W)

    # Author input
    author_name = StringVar()
    author_list = dropDownWithNew("author_details")
    Label(
        root,
        font=(myFont, 15),
        text="Author      : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.29)
    author_dropdown = OptionMenu(root, author_name, *author_list).place(
        relx=0.28, rely=0.31, width=500, anchor=W
    )

    # publisher input
    pub = StringVar()
    pub_list = dropDownWithNew("publisher_details")
    Label(
        root,
        font=(myFont, 15),
        text="Publisher  : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.35)
    pub_dropdown = OptionMenu(root, pub, *pub_list).place(
        relx=0.28, rely=0.370, width=500, anchor=W
    )

    # isbn input
    isbnVar = StringVar()
    Label(
        root,
        font=(myFont, 15),
        text="ISBN        : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.405)
    isbn = Entry(
        root,
        textvariable=isbnVar,
        font=(myFont, 13, "normal"),
    )
    isbn.place(relx=0.28, rely=0.425, width=500, anchor=W)

    # group input
    group = StringVar()
    group_list = dropDownWithNew("group_details")
    Label(
        root,
        font=(myFont, 15),
        text="Group      : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.455)
    group_dropdown = OptionMenu(root, group, *group_list)
    group_dropdown.place(relx=0.28, rely=0.48, width=500, anchor=W)

    # status input
    status = StringVar()
    status_list = dropDown("status_details")
    Label(
        root,
        font=(myFont, 15),
        text="Status      : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.515)
    status_dropdown = OptionMenu(root, status, *status_list)
    status_dropdown.place(relx=0.28, rely=0.540, width=500, anchor=W)

    # damages input
    damages = StringVar()
    damages_list = dropDown("damages_details")
    Label(
        root,
        font=(myFont, 15),
        text="Damages : ",
        background=myColor,
        foreground="white",
    ).place(relx=0.17, rely=0.57)
    damages_dropdown = OptionMenu(root, damages, *damages_list)
    damages_dropdown.place(relx=0.28, rely=0.6, width=500, anchor=W)

    subButton = Button(
        root,
        text=" Submit ",
        command=lambda: upload(
            root, id, title, author_name, pub, isbn, group, status, damages
        ),
        foreground=myColor,
        background="white",
        font=(myFont, 15),
    )
    subButton.place(relx=0.28, rely=0.7, anchor=W)

    # i cant fnd the command for the display button but here it is tinggal nambahin the command
    displayButton = Button(
        root,
        text=" Display ",
        foreground=myColor,
        background="white",
        font=(myFont, 15),
    )
    displayButton.place(relx=0.38, rely=0.7, anchor=W)

    # havent added any commands, but this button to return to prev page
    backButton = Button(
        root,
        text="  Back  ",
        foreground=myColor,
        background="white",
        font=(myFont, 15),
        command=lambda: menuPage(root),
    )
    backButton.place(relx=0.48, rely=0.7, anchor=W)

    refreshBtn = Button(
        root,
        text="Refresh",
        foreground=myColor,
        background="white",
        font=(myFont, 15),
        command=lambda: addBooks(root),
    )
    refreshBtn.place(relx=0.58, rely=0.7, anchor=W)


def displayBooks(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.grid(row=1, column=1, padx=20, pady=50)
    view["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=190)
    view.column("3", width=70)
    view.column("4", width=70)
    view.column("5", width=150)
    view.column("6", width=100)
    view.column("7", width=170)
    view.column("8", width=80)
    view.column("9", width=80)
    view.heading("1", text="ID")
    view.heading("2", text="Title")
    view.heading("3", text="Author First Name")
    view.heading("4", text="Author First Name")
    view.heading("5", text="Publisher")
    view.heading("6", text="ISBN")
    view.heading("7", text="Group")
    view.heading("8", text="Status")
    view.heading("9", text="Damage")

    for i in set:  # type: ignore
        print(i)
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

    deleteBtn = Button(
        root,
        text="Delete",
        foreground="black",
        background="white",
        command=lambda: delete(view, view.selection()[0]),
        font=(myFont, 13),
        borderwidth=0,
    )
    deleteBtn.place(relx=0.8, rely=0.8)

    backBtn = Button(
        root,
        text="Back",
        foreground="black",
        background="white",
        command=lambda: menuPage(root),
        font=(myFont, 13),
        borderwidth=0,
    )
    backBtn.place(relx=0.05, rely=0.03)
