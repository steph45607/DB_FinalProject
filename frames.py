# from tkinter import *
# from tkinter import Toplevel, Button, TOP, IntVar, StringVar, Label, Text, W, CENTER, OptionMenu, PhotoImage, font
from tkinter import *
import tkinter.font as font
from main import *
from methods import *
import ttk

# Colors
offWhite = "#FAF9F6"
back = "#CFA3F2"
# myFont = font.Font(family="Helvetica")

# To clean the root window, used to change between frames
def cleanPage(root):
    """
    Method to clean the window
    """
    for widget in root.winfo_children(): # To know the widgets used in that page
        widget.destroy() # To delete all the widgets with iteration

# Destroy the window 
def close_win(root):
    root.destroy()

def invalidPopup(root):
    invalidpop = Toplevel(root)
    invalidpop.geometry("400x200")
    invalidpop.resizable(False, False)
    invalidpop.configure(bg="white")
    invalidpop.title("Login Failed")
        
    Label(invalidpop, font=(myFont,15), text = "Invalid username or password !", background="white", foreground="black").place(relx=0.15, rely=0.27)
    Label(invalidpop, font=(myFont,15), text = "Try again later. ", background="white", foreground="black").place(relx=0.15, rely=0.4)
        
    def close():
        invalidpop.destroy()

    backButton = backButton = Button(invalidpop,text = '  OK  ', command = close, foreground="white", background='#2C602E', font=(myFont, 15))
    backButton.place(relx=0.4, rely = 0.6)

def landingPage(root):
    cleanPage(root)
    # Add image file
    global background
    background = PhotoImage(file = "images/backgroundLandingPage.png")
    global logo
    logo = PhotoImage(file = "images/logo.png" )
    global qr
    qr = PhotoImage(file="images/qr.png")        
    # Show image using label
    backgroundlabel = Label(root, image = background, background="white" )
    backgroundlabel.place(x = 0, y = 0)

    logolabel = Label(root, image = logo)
    logolabel.place(relx=0.143, rely = 0.38)

    userButton = Button(root, font=(myFont,18), command= lambda:loginUser(root), text = "  User  ", background="#2C602E", foreground="white")
    userButton.place(relx=0.18, rely = 0.6)

    adminButton = Button(root, font=(myFont,18), command= lambda:loginAdmin(root), text = " Admin ", background="#2C602E", foreground="white")
    adminButton.place(relx=0.29, rely = 0.6)

    textWelcome = Label(root, font=(myFont,18), text="Welcome to BookStack", bg="#1A371B", foreground='white')
    textWelcome.place(relx=0.63, rely=0.22)

    textIntro1 = Label(root, font=(myFont, 10), text="BookStack is an application made as the final project ", bg="#1A371B", foreground='white')
    textIntro1.place(relx=0.63, rely=0.31)

    textIntro2 = Label(root, font=(myFont, 10), text="of Maria Clarin, Rachel Anastasia Wijaya, and Stephanie", bg="#1A371B", foreground='white')
    textIntro2.place(relx=0.63, rely=0.34)

    textIntro3 = Label(root, font=(myFont, 10), text="Staniswinata for Database Technology.", bg="#1A371B", foreground='white')
    textIntro3.place(relx=0.63, rely=0.37)

    textIntro4 = Label(root, font=(myFont, 10), text="It is designed to manage library logs and documentation ", bg="#1A371B", foreground='white')
    textIntro4.place(relx=0.63, rely=0.45)

    textIntro5 = Label(root, font=(myFont, 10), text="systems", bg="#1A371B", foreground='white')
    textIntro5.place(relx=0.63, rely=0.48)

    qrlabel = Label(root, image = qr, background="#1A371B")
    qrlabel.place(relx =0.618, rely=0.54)

    textIntro6 = Label(root, font=(myFont, 10), text="Visit our GitHub Repository for this project ", bg="#1A371B", foreground='white')
    textIntro6.place(relx=0.701, rely=0.56)

    textIntro7 = Label(root, font=(myFont, 10), text="by scanning the QR Code!", bg="#1A371B", foreground='white')
    textIntro7.place(relx=0.701, rely=0.59)
    
def loginAdmin(root):
    cleanPage(root)
    root.title("Enter Admin Login Credentials")

    usernameVar=StringVar()
    passwordVar=StringVar()

    def adminCheck():
        username=usernameVar.get()
        password=passwordVar.get()

        if username == "marracste" and password=="dbtech123":
            print("The name is : " + username)
            print("The password is : " + password)
        else:
            invalidPopup(root)

    Label(root, font=(myFont,15), text = "Username : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.3)
    usernameInput = Entry(root,textvariable = usernameVar, font=(myFont,13,'normal'))
    usernameInput.place(relx=0.35, rely=0.32,  width=270)

    Label(root, font=(myFont,15), text = "Password : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.45)
    passwordInput= Entry(root, textvariable = passwordVar, font = (myFont,13,'normal'), show = '*')
    passwordInput.place(relx=0.35, rely=0.47,  width=270)

    loginButton = Button(root,text = 'Login', command = adminCheck, foreground="#2C602E", background='white', font=(myFont, 15))
    loginButton.place(relx=0.35, rely = 0.6)

    backButton = backButton = Button(root,text = 'Back', command = lambda:landingPage(root), foreground="#2C602E", background='white', font=(myFont, 10))
    backButton.place(relx=0.01, rely = 0.02)

def loginUser(root):
    cleanPage(root)
    root.title("Enter User Login Credentials")

    usernameVar=StringVar()
    passwordVar=StringVar()

    def userCheck():
        username=usernameVar.get()
        password=passwordVar.get()

        if username == "IamUser" and password=="hello123":
            print("The name is : " + username)
            print("The password is : " + password)
        else:
            invalidPopup(root)
    Label(root, font=(myFont,15), text = "Username : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.3)
    usernameInput = Entry(root,textvariable = usernameVar, font=(myFont,13,'normal'))
    usernameInput.place(relx=0.35, rely=0.32,  width=270)

    Label(root, font=(myFont,15), text = "Password : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.45)
    passwordInput= Entry(root, textvariable = passwordVar, font = (myFont,13,'normal'), show = '*')
    passwordInput.place(relx=0.35, rely=0.47,  width=270)

    loginButton = Button(root,text = 'Login', command = userCheck, foreground="#2C602E", background='white', font=(myFont, 15))
    loginButton.place(relx=0.35, rely = 0.6)

    backButton = backButton = Button(root,text = 'Back', command = lambda:landingPage(root), foreground="#2C602E", background='white', font=(myFont, 10), borderwidth=0)
    backButton.place(relx=0.01, rely = 0.02)

def menuPage(root):
    cleanPage(root)

    title = Label(root, text = "Welcome to Menu", font=("Roboto", 30), bg = back, fg = offWhite)
    title.place(relx=.5, rely=.15, anchor=CENTER)

    transactionBtn = Button(root, text = "Transaction List")
    transactionBtn.place(relx=.35, rely=.3, anchor=CENTER)

    bookBtn = Button(root, text = "Book List")
    bookBtn.place(relx=.65, rely=.3, anchor=CENTER)

    addTransactionBtn = Button(root, text = "Add Transaction")
    addTransactionBtn.place(relx=.35, rely=.35, anchor=CENTER)

    addBookBtn = Button(root, text = "Add Books", command=lambda:addBooksNew(root))
    addBookBtn.place(relx=.65, rely=.35, anchor=CENTER)

    exitBtn = Button(root, text = "Exit / Change Account", command=lambda:landingPage(root))
    exitBtn.place(relx=.9, rely=.05, anchor=CENTER)

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

    submit = Button(popup, text="Submit", command=lambda:add_three(popup, table, value1, value2, value3))
    submit.place(relx=.9, rely=.5, anchor=CENTER)

def popup_two(root, text1, text2, table):
    
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

    submit = Button(popup, text="Submit", command=lambda:add_two(popup, table, value1, value2))
    submit.place(relx=.9, rely=.5, anchor=CENTER)

def addBooks(root):
    cleanPage(root)

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
    group_dropdown = ttk.Combobox(root)
    group_dropdown['values'] = group_list
    # group_dropdown['state'] = 'normal'
    # group_dropdown = OptionMenu(root, group, *group_list)
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
    # submitBtn = Button(root, image = btnPic, command=lambda:print(pub.get()), borderwidth=0, compound = TOP)
    submitBtn = Button(root, image = btnPic, command=lambda: upload(root, id, title, author_name,pub, isbn, group, status, damages), borderwidth=0, compound = TOP)
    submitBtn.place(relx=.9, rely=.85, anchor=CENTER)

    displayBtn = Button(root, text = "Display", borderwidth=0, compound=TOP)
    displayBtn.place(relx=.9, rely=.95)

    backBtn = Button(root, text = "Back to menu", command=lambda:menuPage(root))
    backBtn.place(relx=.1, rely=.05, anchor=CENTER)

def addBooksNew(root):
    global background
    background = PhotoImage(file = "images/backgroundAddBooks.png")

    myFont = font.Font(family='Helvetica')
    myColor = "#1A371B"

    # Show image using label
    backgroundlabel = Label(root, image = background, background="white" )
    backgroundlabel.place(x = -1, y = -1)

    Label(root, font=('Helvetica Bold',23), text = " Add Book Details ", background=myColor, foreground='white').place(relx=0.38, rely=0.1)


    #bookID input
    bookIDVar=StringVar()
    Label(root, font=(myFont,15), text = "Book ID   : ", background=myColor, foreground="white").place(relx=0.17, rely=0.18)
    id= Entry(root, textvariable = bookIDVar, font = (myFont,13,'normal'),)
    id.place(relx=0.28, rely=0.205,  width=500, anchor=W)

    #title Input
    titleVar=StringVar()
    Label(root, font=(myFont,15), text = "Title         : ", background=myColor, foreground="white").place(relx=0.17, rely=0.23)
    title= Entry(root, textvariable = titleVar, font = (myFont,13,'normal'),)
    title.place(relx=0.28, rely=0.255,  width=500, anchor=W)

    #Author input
    author_name = StringVar()
    author_list = dropDown("author_details") 
    Label(root, font=(myFont,15), text = "Author      : ", background=myColor, foreground="white").place(relx=0.17, rely=0.29)
    author_dropdown = OptionMenu(root, author_name, *author_list).place(relx = 0.28, rely=0.31, width=500, anchor=W)

    #publisher input
    pub = StringVar()
    pub_list = dropDown("publisher_details")
    Label(root, font=(myFont,15), text = "Publisher  : ", background=myColor, foreground="white").place(relx=0.17, rely=0.35)
    pub_dropdown = OptionMenu(root, pub, *pub_list).place(relx=0.28, rely=0.370, width=500, anchor=W)

    #isbn input
    isbnVar =StringVar()
    Label(root, font=(myFont,15), text = "ISBN        : ", background=myColor, foreground="white").place(relx=0.17, rely=0.405)
    isbn= Entry(root, textvariable = isbnVar, font = (myFont,13,'normal'),)
    isbn.place(relx=0.28, rely=0.425,  width=500, anchor=W)

    #group input
    group = StringVar()
    group_list = dropDown("group_details")
    Label(root, font=(myFont,15), text = "Group      : ", background=myColor, foreground="white").place(relx=0.17, rely=0.455)
    group_dropdown = OptionMenu(root, group, *group_list).place(relx=0.28, rely=0.48, width=500, anchor=W)

    #status input
    status = StringVar()
    status_list = dropDown("status_details")
    Label(root, font=(myFont,15), text = "Status      : ", background=myColor, foreground="white").place(relx=0.17, rely=0.515)
    status_dropdown = OptionMenu(root, status, *status_list).place(relx=0.28, rely=0.540, width = 500, anchor=W)

    #damages input
    damages = StringVar()
    damages_list = dropDown("damages_details")
    Label(root, font=(myFont,15), text = "Damages : ", background=myColor, foreground="white").place(relx=0.17, rely=0.57)
    damages_dropdown = OptionMenu(root, damages, *damages_list).place(relx=0.28, rely=0.6, width=500, anchor=W)

    subButton = Button(root,text = ' Submit ', command =lambda:upload(root, id, title, author_name,pub, isbn, group, status, damages), foreground=myColor, background='white', font=(myFont, 15))
    subButton.place(relx=0.28, rely = 0.64)

    #i cant fnd the command for the display button but here it is tinggal nambahin the command
    displayButton = Button(root,text = ' Display ', foreground=myColor, background='white', font=(myFont, 15) )
    displayButton.place(relx=0.375, rely = 0.64)

    #havent added any commands, but this button to return to prev page
    backButton = backButton = Button(root,text = '  Back  ', foreground=myColor, background='white', font=(myFont, 15))
    backButton.place(relx=0.475, rely = 0.64)