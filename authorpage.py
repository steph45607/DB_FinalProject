# Import module 
from tkinter import *
from tkinter import OptionMenu
import tkinter.font as font
from main import *
from methods import *

#to make as popup, change the entire code to a function, 
#the authorpage Tk() tinggal ganti ke authorpage =  Toplevel(*insert name of bottom window*)
authorpage = Tk()

# Adjust size 
authorpage.geometry("1000x600")
authorpage.resizable(False, False)
authorpage.title("BookStack LMS") 
# Add image file
background = PhotoImage(file = "images/backgroundMenu.png")

myFont = font.Font(family='Helvetica')
myColor = "#1A371B"

# Show image using label
backgroundlabel = Label(authorpage, image = background, background="white" )
backgroundlabel.place(x = -1, y = -1)

Label(authorpage, font=('Helvetica Bold',23), text = " Add Author Details ", background=myColor, foreground='white').place(relx=0.38, rely=0.1)


#authorID input
authorIDVar=StringVar()
Label(authorpage, font=(myFont,15), text = "Author ID  : ", background=myColor, foreground="white").place(relx=0.17, rely=0.18)
id= Entry(authorpage, textvariable = authorIDVar, font = (myFont,13,'normal'),)
id.place(relx=0.28, rely=0.205,  width=500, anchor=W)

#first name Input
fnameVar=StringVar()
Label(authorpage, font=(myFont,15), text = "First Name: ", background=myColor, foreground="white").place(relx=0.17, rely=0.23)
fname= Entry(authorpage, textvariable = fnameVar, font = (myFont,13,'normal'),)
fname.place(relx=0.28, rely=0.255,  width=500, anchor=W)

#last name  Input
lnameVar=StringVar()
Label(authorpage, font=(myFont,15), text = "Last Name: ", background=myColor, foreground="white").place(relx=0.17, rely=0.28)
lname= Entry(authorpage, textvariable = lnameVar, font = (myFont,13,'normal'),)
lname.place(relx=0.28, rely=0.305,  width=500, anchor=W)


createButton = Button(authorpage,text = ' Create ', foreground=myColor, background='white', font=(myFont, 15))
createButton.place(relx=0.28, rely = 0.34)


backButton = Button(authorpage,text = 'Back', foreground=myColor, background='white', font=(myFont, 10), borderwidth=0)
backButton.place(relx=0.01, rely = 0.02)


authorpage.mainloop()