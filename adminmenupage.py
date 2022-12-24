# Import module 
from tkinter import *
import tkinter.font as font
from main import *
from methods import *
from tkinter.messagebox import askyesno

# Create object 
adminmenu = Tk()

# Adjust size 
adminmenu.geometry("1000x600")
adminmenu.resizable(False, False)
adminmenu.title("BookStack LMS") 
# Add image file
background = PhotoImage(file = "images/backgroundMenu.png")

myFont = font.Font(family='Helvetica')
myColor = "#1A371B"

# Show image using label
backgroundlabel = Label(adminmenu, image = background, background="white" )
backgroundlabel.place(x = -1, y = -1)

#title for admin menu
Label(adminmenu, font=('Helvetica Bold',25), text = " Admin Menu ", background=myColor, foreground='white').place(relx=0.38, rely=0.1)

#view transaction btn
tranBtnPhoto = PhotoImage(file = "images/transactionlist.png").subsample(8,8)
transactionBtn = Button(adminmenu,text = 'View Transactions ', image=tranBtnPhoto, compound =LEFT, foreground='black', background='white', font=(myFont, 15))
transactionBtn.place(relx=0.23, rely=0.24,  width=240)

#add transaction btn
addTransBtnPhoto = PhotoImage(file = "images/addtransaction.png").subsample(8,8)
addTransactionBtn = Button(adminmenu,text = 'Add Transactions  ', image=addTransBtnPhoto, compound =LEFT, foreground='black', background='white', font=(myFont, 15))
addTransactionBtn.place(relx=0.23, rely=0.4,  width=240)

#view books btn
bookBtnPhoto = PhotoImage(file = "images/bookbtn.png").subsample(8,8)
bookBtn = Button(adminmenu,text = ' View Books  ', image=bookBtnPhoto, compound =LEFT, foreground='black', background='white', font=(myFont, 15))
bookBtn.place(relx=0.5, rely=0.24,  width=240)

#add books btn
addbookBtnPhoto = PhotoImage(file = "images/addbook.png").subsample(8,8)
addBookBtn = Button(adminmenu,text = ' Add Books  ', image=addbookBtnPhoto, compound =LEFT, foreground='black', background='white', font=(myFont, 15)) #command=lambda:addBooks(root)
addBookBtn.place(relx=0.5, rely=0.4,  width=240)

#confirmation popup message if want to log out
def confirm():
    answer = askyesno(title='Log out confirmation',
                    message='Are you sure that you want to log out?')
    if answer:
        adminmenu.destroy() #u can make this into like moving to the landing page-- ur prev command was #lambda:landingPage(root)

#log out button    
backBtn  = Button(adminmenu,text = ' Log Out ', foreground='black', background='white',command=confirm, font=(myFont, 13))
backBtn.place(relx=0.9, rely = 0.02)




adminmenu.mainloop()