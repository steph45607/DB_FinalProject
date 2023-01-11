# from tkinter import *
# from tkinter import Toplevel, Button, TOP, IntVar, StringVar, Label, Text, W, CENTER, OptionMenu, PhotoImage, font
from tkinter import *
from tkinter import ttk
import tkinter.font as font
from tkinter.messagebox import askyesno
from tkcalendar import DateEntry
from main import *
from methods import *
import ttk

from methods import add_three

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

    logolabel = Label(root, image=logo, background="white")
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
    global background
    background = PhotoImage(file="images/backgroundLogin.png")
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=0, y=0)
    
    usernameVar = StringVar()
    passwordVar = StringVar()

    def adminCheck():
        username = usernameVar.get()
        password = passwordVar.get()

        if username == "admin" and password == "admin123":
            adminMenuPage(root)
        else:
            invalidPopup(root)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text=" Admin Login ",
        background="white",
        foreground="#1A371B",
    ).place(relx=0.38, rely=0.1)

    Label(
        root,
        font=(myFont, 15),
        text="Username : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.46)
    usernameInput = Entry(root, textvariable=usernameVar, font=(myFont, 13, "normal"))
    usernameInput.place(relx=0.5, rely=0.47, width=270)

    Label(
        root,
        font=(myFont, 15),
        text="Password : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.51)
    passwordInput = Entry(
        root, textvariable=passwordVar, font=(myFont, 13, "normal"), show="*"
    )
    passwordInput.place(relx=0.5, rely=0.52, width=270)

    loginButton = Button(
        root,
        text=" Login ",
        command=adminCheck,
        foreground="#2C602E",
        background="white",
        font=(myFont, 15),
    )
    loginButton.place(relx=0.382, rely=0.57)

    backButton = backButton = Button(
        root,
        text=" Back ",
        command=lambda: landingPage(root),
        foreground="white",
        background="#1A371B",
        font=(myFont, 10),
    )
    backButton.place(relx=0.01, rely=0.02)


def loginUser(root):
    cleanPage(root)
    global background
    background = PhotoImage(file="images/backgroundLogin.png")
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=0, y=0)

    usernameVar = StringVar()
    passwordVar = StringVar()

    def userCheck():
        username = usernameVar.get()
        password = passwordVar.get()

        if username == "user" and password == "user123":
            userMenuPage(root)
        else:
            invalidPopup(root)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text=" User Login ",
        background="white",
        foreground="#1A371B",
    ).place(relx=0.38, rely=0.1)

    Label(
        root,
        font=(myFont, 15),
        text="Username : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.46)
    usernameInput = Entry(root, textvariable=usernameVar, font=(myFont, 13, "normal"))
    usernameInput.place(relx=0.5, rely=0.47, width=270)

    Label(
        root,
        font=(myFont, 15),
        text="Password : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.51)
    passwordInput = Entry(
        root, textvariable=passwordVar, font=(myFont, 13, "normal"), show="*"
    )
    passwordInput.place(relx=0.5, rely=0.52, width=270)

    loginButton = Button(
        root,
        text=" Login ",
        command=userCheck,
        foreground="#2C602E",
        background="white",
        font=(myFont, 15),
    )
    loginButton.place(relx=0.382, rely=0.57)

    backButton = backButton = Button(
        root,
        text=" Back ",
        command=lambda: landingPage(root),
        foreground="white",
        background="#1A371B",
        font=(myFont, 10),
    )
    backButton.place(relx=0.01, rely=0.02)

def userMenuPage(root):
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
        font=("Helvetica Bold", 30),
        text=" User Menu ",
        background=myColor,
        foreground="white",
    ).place(relx=0.38, rely=0.17)

    # view groups btn
    global viewgroupsBtnPhoto
    viewgroupsBtnPhoto = PhotoImage(file="images/viewGroups.png").subsample(6, 6)
    viewGroupsBtn = Button(
        root,
        text=" View Groups  ",
        image=viewgroupsBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 18),
        command=lambda: userDisplayGroups(root),
        borderwidth=0,
    )#command for view groups
    viewGroupsBtn.place(relx=0.5, rely=0.31, width=240)

    # view books btn
    global bookBtnPhoto
    bookBtnPhoto = PhotoImage(file="images/bookbtn.png").subsample(6, 6)
    bookBtn = Button(
        root,
        text=" View Books  ",
        image=bookBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 18),
        command=lambda: userDisplayBooks(root),
        borderwidth=0,
    )
    bookBtn.place(relx=0.22, rely=0.31, width=240)


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

def adminMenuPage(root):
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
        command=lambda:displayTransaction(root),
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
        command=lambda:addTransaction(root),
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

    # view user btn
    global viewUserBtnPhoto
    viewUserBtnPhoto = PhotoImage(file="images/viewUser.png").subsample(8, 8)
    viewUserBtn = Button(
        root,
        text=" View Users  ",
        image=viewUserBtnPhoto,
        compound=LEFT,
        foreground="black",
        background="white",
        font=(myFont, 15),
        command=lambda:displayUsers(root),
        borderwidth=0,
    )  # command= for view users
    viewUserBtn.place(relx=0.36, rely=0.56, width=240)

    authorBtn = Button(root, text = "Author List", command=lambda:displayAuthor(root))
    authorBtn.place(relx = 0.3, rely = 0.9)

    publisherBtn = Button(root, text = "Publisher List", command=lambda:displayPublisher(root))
    publisherBtn.place(relx = 0.4, rely = 0.9)

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
    # bookIDVar = StringVar()
    # Label(
    #     root,
    #     font=(myFont, 15),
    #     text="Book ID   : ",
    #     background=myColor,
    #     foreground="white",
    # ).place(relx=0.17, rely=0.18)
    # id = Entry(
    #     root,
    #     textvariable=bookIDVar,
    #     font=(myFont, 13, "normal"),
    # )
    # id.place(relx=0.28, rely=0.205, width=500, anchor=W)

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
            root, title, author_name, pub, isbn, group, status, damages
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
    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

    refreshBtn = Button(
        root,
        text="Refresh",
        foreground=myColor,
        background="white",
        font=(myFont, 15),
        command=lambda: addBooks(root),
    )
    refreshBtn.place(relx=0.48, rely=0.7, anchor=W)

def addTransaction(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Add Transaction",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Title : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.19)
    searchBook = StringVar()
    
    searchInput = Entry(root, textvariable=searchBook, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.19, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchTitle_book(bookView, searchBook),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.525, rely=0.188)

    refreshBookBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_book(searchBook, bookView),
        font=(myFont, 9),
    )
    refreshBookBtn.place(relx=0.585, rely=0.188)

    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id"
    )
    books = cursor.fetchall()

    bookView = ttk.Treeview(root, selectmode="browse", height=5)
    bookView.place(relx=0.024, rely=0.25)
    bookView["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    bookView["show"] = "headings"
    bookView.column("1", width=50)
    bookView.column("2", width=160)
    bookView.column("3", width=115)
    bookView.column("4", width=115)
    bookView.column("5", width=150)
    bookView.column("6", width=100)
    bookView.column("7", width=100)
    bookView.column("8", width=80)
    bookView.column("9", width=80)
    bookView.heading("1", text="ID")
    bookView.heading("2", text="Title")
    bookView.heading("3", text="Author First Name")
    bookView.heading("4", text="Author Last Name")
    bookView.heading("5", text="Publisher")
    bookView.heading("6", text="ISBN")
    bookView.heading("7", text="Group")
    bookView.heading("8", text="Status")
    bookView.heading("9", text="Damage")

    for i in books:  # type: ignore
        bookView.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )
    
        Label(
        root,
        font=(myFont, 15),
        text="Search By Borrwer ID : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.49)
    searchUser = StringVar()
    
    searchInput = Entry(root, textvariable=searchUser, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.19, rely=0.49, width=330)

    searchTranBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchUserID_user(userView, searchUser),
        font=(myFont, 9),
    )
    searchTranBtn.place(relx=0.525, rely=0.488)

    refreshTranBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_user(searchUser, userView),
        font=(myFont, 9),
    )
    refreshTranBtn.place(relx=0.585, rely=0.488)

    cursor.execute(
        "SELECT u.id, u.name, u.email, r.role_name FROM user_details u JOIN role_details r ON u.role_id = r.id"
    )
    users = cursor.fetchall()

    userView = ttk.Treeview(root, selectmode="browse", height=5)
    userView.place(relx=0.024, rely=0.55)
    userView["columns"] = ("1", "2", "3", "4")
    userView["show"] = "headings"
    userView.column("1", width=150)
    userView.column("2", width=160)
    userView.column("3", width=115)
    userView.column("4", width=115)
    userView.heading("1", text="ID")
    userView.heading("2", text="Name")
    userView.heading("3", text="Email")
    userView.heading("4", text="Role")


    for i in users:  # type: ignore
        userView.insert(
            "", "end", values=(i[0], i[1], i[2], i[3])
        )
    
    calendar = DateEntry(root, selectmode = 'day')
    calendar.place(relx = 0.1, rely= 0.85)

    addBtn = Button(
        root,
        text=" Add ",
        foreground="black",
        background="white",
        command=lambda: addTransactionMethod(bookView,userView, bookView.selection()[0], userView.selection()[0], calendar.get_date()),
        font=(myFont, 10),
    )
    addBtn.place(relx=0.915, rely=0.658)

    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def displayBooks(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Registered Books ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Title : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.18)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.19, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchTitle_book(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.525, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:sortBooks(view, "b.id", "ASC"),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.585, rely=0.188)

    Label(
        root,
        font=(myFont, 15),
        text="Sort By : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.652)
    

    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.024, rely=0.25)
    view["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=160)
    view.column("3", width=115)
    view.column("4", width=115)
    view.column("5", width=150)
    view.column("6", width=100)
    view.column("7", width=100)
    view.column("8", width=80)
    view.column("9", width=80)
    view.heading("1", text="ID")
    view.heading("2", text="Title")
    view.heading("3", text="Author First Name")
    view.heading("4", text="Author Last Name")
    view.heading("5", text="Publisher")
    view.heading("6", text="ISBN")
    view.heading("7", text="Group")
    view.heading("8", text="Status")
    view.heading("9", text="Damage")

    for i in set:  # type: ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

    deleteBtn = Button(
        root,
        text=" Delete ",
        foreground="black",
        background="white",
        command=lambda: deleteBook(view, view.selection()[0]),
        font=(myFont, 10),
    )
    deleteBtn.place(relx=0.915, rely=0.658)

    idBtn = Button(root, text = " Book ID ", command=lambda:sortBooks(view, "b.id", "ASC"), font=(myFont, 10))
    idBtn.place(relx=0.11, rely=0.657)

    titleBtn = Button(root, text = " Title ", command = lambda:sortBooks(view, "b.title", "ASC"), font=(myFont, 10))
    titleBtn.place(relx=0.18, rely=0.657)

    authorBtn = Button(root, text = " Author ", command=lambda:sortBooks(view, "a.firstName", "ASC"), font=(myFont, 10))
    authorBtn.place(relx=0.227, rely=0.657)

    publisherBtn = Button(root, text = " Publisher ", command=lambda:sortBooks(view, "p.name", "ASC"), font=(myFont, 10))
    publisherBtn.place(relx=0.287, rely=0.657)

    availBtn = Button(root, text = " Available ", command=lambda:sortStatusBooks(view, "s.detail", "available"), font=(myFont, 10))
    availBtn.place(relx=0.363, rely=0.657)

    unavailBtn = Button(root, text = " Unavailable ", command=lambda:sortStatusBooks(view, "s.detail", "unavailable"), font=(myFont, 10))
    unavailBtn.place(relx=0.436, rely=0.657)

    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def userDisplayBooks(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Registered Books ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Title : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.18)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.19, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchTitle_book(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.525, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:sortBooks(view, "b.id", "ASC"),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.585, rely=0.188)

    Label(
        root,
        font=(myFont, 15),
        text="Sort By : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.652)
    

    cursor.execute(
        "select b.id, b.title, a.firstName, a.lastName, p.name, b.isbn, g.group_name, s.detail, d.detail from book_details b join author_details a on b.author_id = a.id join publisher_details p on b.pub_id = p.id join group_details g on b.group_id = g.id join status_details s on b.status_id = s.id join damages_details d on b.damages_id = d.id"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.024, rely=0.25)
    view["columns"] = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=160)
    view.column("3", width=115)
    view.column("4", width=115)
    view.column("5", width=150)
    view.column("6", width=100)
    view.column("7", width=100)
    view.column("8", width=80)
    view.column("9", width=80)
    view.heading("1", text="ID")
    view.heading("2", text="Title")
    view.heading("3", text="Author First Name")
    view.heading("4", text="Author Last Name")
    view.heading("5", text="Publisher")
    view.heading("6", text="ISBN")
    view.heading("7", text="Group")
    view.heading("8", text="Status")
    view.heading("9", text="Damage")

    for i in set:  # type: ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8])
        )

    idBtn = Button(root, text = " Book ID ", command=lambda:sortBooks(view, "b.id", "ASC"), font=(myFont, 10))
    idBtn.place(relx=0.11, rely=0.657)

    titleBtn = Button(root, text = " Title ", command = lambda:sortBooks(view, "b.title", "ASC"), font=(myFont, 10))
    titleBtn.place(relx=0.18, rely=0.657)

    authorBtn = Button(root, text = " Author ", command=lambda:sortBooks(view, "a.firstName", "ASC"), font=(myFont, 10))
    authorBtn.place(relx=0.227, rely=0.657)

    publisherBtn = Button(root, text = " Publisher ", command=lambda:sortBooks(view, "p.name", "ASC"), font=(myFont, 10))
    publisherBtn.place(relx=0.287, rely=0.657)

    availBtn = Button(root, text = " Available ", command=lambda:sortStatusBooks(view, "s.detail", "available"), font=(myFont, 10))
    availBtn.place(relx=0.363, rely=0.657)

    unavailBtn = Button(root, text = " Unavailable ", command=lambda:sortStatusBooks(view, "s.detail", "unavailable"), font=(myFont, 10))
    unavailBtn.place(relx=0.436, rely=0.657)

    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: userMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def userDisplayGroups(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Book Groups ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Group : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.02, rely=0.18)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.19, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchGroup(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.525, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:sortGroups(view, "id", "ASC"),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.585, rely=0.188)
    

    cursor.execute(
        "select * from group_details"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.024, rely=0.25)
    view["columns"] = ("1", "2", "3")
    view["show"] = "headings"
    view.column("1", width=100)
    view.column("2", width=150)
    view.column("3", width=150)
    view.heading("1", text="Group ID")
    view.heading("2", text="Group Name")
    view.heading("3", text="Location")

    for i in set:  # type: ignore
        # print(i)
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: userMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def displayTransaction(root):
    checkOverdue()
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Transaction History",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Borrower ID : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.183)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.3225, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchBorrowerID_transaction(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.66, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_transaction(searchVar, view),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.72, rely=0.188)

    Label(
        root,
        font=(myFont, 15),
        text="Sort By : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.652)
    

    cursor.execute(
        "SELECT t.transaction_id, b.title, u.id, u.name, t.borrow_date, t.due_date, s.detail FROM transaction_details t JOIN book_details b ON t.book_id = b.id JOIN user_details u ON t.borrower_id = u.id JOIN transactionStatus_details s ON t.borrow_status = s.id"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.08, rely=0.25)
    view["columns"] = ("1", "2", "3", "4", "5", "6", "7")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=180)
    view.column("3", width=115)
    view.column("4", width=180)
    view.column("5", width=100)
    view.column("6", width=100)
    view.column("7", width=120)
    view.heading("1", text="ID")
    view.heading("2", text="Book Title")
    view.heading("3", text="Borrower ID")
    view.heading("4", text="Borrower Name")
    view.heading("5", text="Date")
    view.heading("6", text="Due")
    view.heading("7", text="Status")

    for i in set:  # type: ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6])
        )

    deleteBtn = Button(
        root,
        text="   Delete   ",
        foreground="black",
        background="#BDCBBD",
        width=11,
        command=lambda: deleteTransaction(view, view.selection()[0]),
        font=(myFont, 13),
    )
    deleteBtn.place(relx=0.82, rely=0.71)

    hasReturneddBtn = Button(
        root,
        text=" Complete ",
        foreground="black",
        background="#BDCBBD",
        width=11,
        command=lambda: isReturned(view, view.selection()[0]),
        font=(myFont, 13),
    )
    hasReturneddBtn.place(relx=0.82, rely=0.648)

    idBtn = Button(root, text = "Transaction ID", command=lambda:sortTransaction(view, "t.transaction_id", "ASC"), font=(myFont, 10))
    idBtn.place(relx=0.19, rely=0.657)

    borrowIDBtn = Button(root, text = " Borrower ID ", command = lambda:sortTransaction(view, "u.id", "ASC"), font=(myFont, 10))
    borrowIDBtn.place(relx=0.29, rely=0.657)

    borrowNameBtn = Button(root, text = " Borrower Name ", command=lambda:sortTransaction(view, "u.name", "ASC"), font=(myFont, 10))
    borrowNameBtn.place(relx=0.38, rely=0.657)

    dateOldBtn = Button(root, text = " Borrow Date Oldest",command=lambda:sortTransaction(view, "t.borrow_date", "ASC") , font=(myFont, 10))
    dateOldBtn.place(relx=0.493, rely=0.657)

    dateNewBtn = Button(root, text = " Borrow Date Latest ",command=lambda:sortTransaction(view, "t.borrow_date", "DESC") , font=(myFont, 10))
    dateNewBtn.place(relx=0.625, rely=0.657)

    dueBtn = Button(root, text = " Overdue Transactions ", command=lambda:sortStatusTransaction(view, "s.detail", "t.due_date","overdue", "ASC"), font=(myFont, 10))
    dueBtn.place(relx=0.19, rely=0.717)

    returnedBtn = Button(root, text = " Returned Transactions ", command=lambda:sortStatusTransaction(view, "s.detail", "t.borrow_status", "returned", "ASC"), font=(myFont, 10))
    returnedBtn.place(relx=0.3369, rely=0.717)

    activeBtn = Button(root, text = " Active Transactions ", command=lambda:sortStatusTransaction(view, "s.detail", "t.borrow_date", "active", "ASC"), font=(myFont, 10))
    activeBtn.place(relx=0.49, rely=0.717)

    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def displayUsers(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="User List",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By User ID : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.183)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.3225, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchUserID_user(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.66, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_user(searchVar, view),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.72, rely=0.188)

    Label(
        root,
        font=(myFont, 15),
        text="Sort By : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.652)
    

    cursor.execute(
        "SELECT u.id, u.name, u.email, r.role_name FROM user_details u JOIN role_details r ON u.role_id = r.id"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.08, rely=0.25)
    view["columns"] = ("1", "2", "3", "4")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=180)
    view.column("3", width=115)
    view.column("4", width=180)
    view.heading("1", text="ID")
    view.heading("2", text="Name")
    view.heading("3", text="Email")
    view.heading("4", text="Role")


    for i in set:  # type: ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2], i[3])
        )

    idBtn = Button(root, text = "User ID", command=lambda:sortUsers(view, "u.id", "ASC"), font=(myFont, 10))
    idBtn.place(relx=0.19, rely=0.657)

    borrowIDBtn = Button(root, text = "Name", command = lambda:sortUsers(view, "u.name", "ASC"), font=(myFont, 10))
    borrowIDBtn.place(relx=0.29, rely=0.657)

    borrowNameBtn = Button(root, text = "Students", command=lambda:sortUserRoles(view, "r.role_name", "student"), font=(myFont, 10))
    borrowNameBtn.place(relx=0.38, rely=0.657)

    dateOldBtn = Button(root, text = "Teacher",command=lambda:sortUserRoles(view, "r.role_name", "teacher") , font=(myFont, 10))
    dateOldBtn.place(relx=0.493, rely=0.657)

    dateNewBtn = Button(root, text = "Staff",command=lambda:sortUserRoles(view, "r.role_name", "staff") , font=(myFont, 10))
    dateNewBtn.place(relx=0.625, rely=0.657)

    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def displayAuthor(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Author List",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Author ID : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.183)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.3225, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchAuthorID(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.66, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_author(searchVar, view),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.72, rely=0.188)

    Label(
        root,
        font=(myFont, 15),
        text="Sort By : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.652)
    

    cursor.execute(
        "SELECT * FROM author_details"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.08, rely=0.25)
    view["columns"] = ("1", "2", "3")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=180)
    view.column("3", width=115)
    view.heading("1", text="ID")
    view.heading("2", text="First Name")
    view.heading("3", text="Last Name")



    for i in set:  # type: ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

    idBtn = Button(root, text = "Author ID", command=lambda:sortAuthor(view, "id", "ASC"), font=(myFont, 10))
    idBtn.place(relx=0.19, rely=0.657)

    borrowIDBtn = Button(root, text = "First Name", command = lambda:sortAuthor(view, "firstName", "ASC"), font=(myFont, 10))
    borrowIDBtn.place(relx=0.29, rely=0.657)

    borrowNameBtn = Button(root, text = "Last Name", command=lambda:sortAuthor(view, "lastName", "ASC"), font=(myFont, 10))
    borrowNameBtn.place(relx=0.38, rely=0.657)


    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

def displayPublisher(root):
    myFont = font.Font(family="Helvetica")
    cleanPage(root)

    global background
    background = PhotoImage(file="images/backgroundDisplay.png")

    # Show image using label
    backgroundlabel = Label(root, image=background, background="white")
    backgroundlabel.place(x=-1, y=-1)

    Label(
        root,
        font=("Helvetica Bold", 25),
        text="Publisher List",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.38, rely=0.06)

    Label(
        root,
        font=(myFont, 15),
        text="Search By Publisher ID : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.183)
    searchVar = StringVar()
    
    searchInput = Entry(root, textvariable=searchVar, font=(myFont, 13, "normal"))
    searchInput.place(relx=0.3225, rely=0.19, width=330)

    searchBtn = Button(
        root,
        text=" Search ",
        foreground="black",
        background="white",
        command=lambda:searchPubID(view, searchVar),
        font=(myFont, 9),
    )
    searchBtn.place(relx=0.66, rely=0.188)

    refreshBtn = Button(
        root,
        text=" Refresh ",
        foreground="black",
        background="white",
        command=lambda:refreshDisplay_pub(searchVar, view),
        font=(myFont, 9),
    )
    refreshBtn.place(relx=0.72, rely=0.188)

    Label(
        root,
        font=(myFont, 15),
        text="Sort By : ",
        background="#1A371B",
        foreground="white",
    ).place(relx=0.09, rely=0.652)
    

    cursor.execute(
        "SELECT * FROM publisher_details"
    )
    set = cursor.fetchall()

    view = ttk.Treeview(root, selectmode="browse")
    view.place(relx=0.08, rely=0.25)
    view["columns"] = ("1", "2", "3")
    view["show"] = "headings"
    view.column("1", width=50)
    view.column("2", width=180)
    view.column("3", width=115)
    view.heading("1", text="ID")
    view.heading("2", text="Name")
    view.heading("3", text="Email")


    for i in set:  # type: ignore
        view.insert(
            "", "end", values=(i[0], i[1], i[2])
        )

    idBtn = Button(root, text = "Publisher ID", command=lambda:sortPublisher(view, "id", "ASC"), font=(myFont, 10))
    idBtn.place(relx=0.19, rely=0.657)

    nameBtn = Button(root, text = "Name", command = lambda:sortPublisher(view, "name", "ASC"), font=(myFont, 10))
    nameBtn.place(relx=0.29, rely=0.657)

    emailBtn = Button(root, text = "Email", command = lambda:sortPublisher(view, "email", "ASC"), font=(myFont, 10))
    emailBtn.place(relx=0.39, rely=0.657)


    backBtn = Button(
        root,
        text=" Back ",
        foreground="black",
        background="white",
        command=lambda: adminMenuPage(root),
        font=(myFont, 10),
    )
    backBtn.place(relx=0.01, rely=0.02)

