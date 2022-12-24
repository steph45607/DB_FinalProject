# Import module 
from tkinter import *
import tkinter.font as font

# Create object 
root = Tk()

# Adjust size 
root.geometry("1000x600")
root.resizable(False, False)
root.title("BookStack LMS") 
# Add image file
background = PhotoImage(file = "images/backgroundLandingPage.png")
logo = PhotoImage(file = 'images/logo.png' )
qr = PhotoImage(file="images/qr.png")

myFont = font.Font(family='Helvetica')

# Show image using label
backgroundlabel = Label(root, image = background, background="white" )
backgroundlabel.place(x = 0, y = 0)

logolabel = Label(root, image = logo)
logolabel.place(relx=0.143, rely = 0.38)


def loginPopupAdmin():
    top= Toplevel(root)
    top.geometry("600x300")
    top.resizable(False, False)
    top.configure(bg="#2C602E")
    top.title("Enter Admin Login Credentials")

    usernameVar=StringVar()
    passwordVar=StringVar()

    def invalidPopup():
        invalidpop = Toplevel(top)
        invalidpop.geometry("400x200")
        invalidpop.resizable(False, False)
        invalidpop.configure(bg="white")
        invalidpop.title("Login Failed")
        
        Label(invalidpop, font=(myFont,15), text = "Invalid username or password !", background="white", foreground="black").place(relx=0.15, rely=0.27)
        Label(invalidpop, font=(myFont,15), text = "Try again later. ", background="white", foreground="black").place(relx=0.15, rely=0.4)
        
        def close():
            invalidpop.destroy()

        backButton = backButton = Button(invalidpop,text = '  Ok  ', command = close, foreground="white", background='#2C602E', font=(myFont, 15))
        backButton.place(relx=0.4, rely = 0.6)

    def adminCheck():
        username=usernameVar.get()
        password=passwordVar.get()

        # print("The name is : " + username)
        # print("The password is : " + password)
        if username == "marracste" and password=="dbtech123":
            print("The name is : " + username)
            print("The password is : " + password)
        else:
            invalidPopup()
            # print("wrong username/password")

    Label(top, font=(myFont,15), text = "Username : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.3)
    usernameInput = Entry(top,textvariable = usernameVar, font=(myFont,13,'normal'))
    usernameInput.place(relx=0.35, rely=0.32,  width=270)

    Label(top, font=(myFont,15), text = "Password : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.45)
    passwordInput= Entry(top, textvariable = passwordVar, font = (myFont,13,'normal'), show = '*')
    passwordInput.place(relx=0.35, rely=0.47,  width=270)

    loginButton = Button(top,text = 'Login', command = adminCheck, foreground="#2C602E", background='white', font=(myFont, 15))
    loginButton.place(relx=0.35, rely = 0.6)

    def closeLogin():
        top.destroy()

    backButton = backButton = Button(top,text = 'Back', command = closeLogin, foreground="#2C602E", background='white', font=(myFont, 10))
    backButton.place(relx=0.01, rely = 0.02)


def loginPopupUser():
    top= Toplevel(root)
    top.geometry("600x300")
    top.resizable(False, False)
    top.configure(bg="#2C602E")
    top.title("Enter User Login Credentials")

    usernameVar=StringVar()
    passwordVar=StringVar()

    def invalidPopup():
        invalidpop = Toplevel(top)
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

    def userCheck():
        username=usernameVar.get()
        password=passwordVar.get()
        
        # print("The name is : " + username)
        # print("The password is : " + password)
        if username == "IamUser" and password=="hello123":
            print("The name is : " + username)
            print("The password is : " + password)
        else:
            invalidPopup()

    Label(top, font=(myFont,15), text = "Username : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.3)
    usernameInput = Entry(top,textvariable = usernameVar, font=(myFont,13,'normal'))
    usernameInput.place(relx=0.35, rely=0.32,  width=270)

    Label(top, font=(myFont,15), text = "Password : ", background="#2C602E", foreground="white").place(relx=0.17, rely=0.45)
    passwordInput= Entry(top, textvariable = passwordVar, font = (myFont,13,'normal'), show = '*')
    passwordInput.place(relx=0.35, rely=0.47,  width=270)

    loginButton = Button(top,text = 'Login', command = userCheck, foreground="#2C602E", background='white', font=(myFont, 15))
    loginButton.place(relx=0.35, rely = 0.6)

    def closeLogin():
        top.destroy()

    backButton = backButton = Button(top,text = 'Back', command = closeLogin, foreground="#2C602E", background='white', font=(myFont, 10), borderwidth=0)
    backButton.place(relx=0.01, rely = 0.02)

userButton = Button(root, font=(myFont,18), command= loginPopupUser, text = "  User  ", background="#2C602E", foreground="white")
userButton.place(relx=0.18, rely = 0.6)

adminButton = Button(root, font=(myFont,18), command= loginPopupAdmin, text = " Admin ", background="#2C602E", foreground="white")
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

root.mainloop()