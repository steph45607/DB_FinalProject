# Import module 
from tkinter import *
from tkinter import OptionMenu
import tkinter.font as font
from main import *
from methods import *

#to make as popup, change the entire code to a function, 
#the publisherpage Tk() tinggal ganti ke publisherpage =  Toplevel(*insert name of bottom window*)
publisherpage = Tk()

# Adjust size 
publisherpage.geometry("1000x600")
publisherpage.resizable(False, False)
publisherpage.title("BookStack LMS") 
# Add image file
background = PhotoImage(file = "images/backgroundMenu.png")

myFont = font.Font(family='Helvetica')
myColor = "#1A371B"

# Show image using label
backgroundlabel = Label(publisherpage, image = background, background="white" )
backgroundlabel.place(x = -1, y = -1)

Label(publisherpage, font=('Helvetica Bold',23), text = " Add Author Details ", background=myColor, foreground='white').place(relx=0.38, rely=0.1)


#publisherID input
publisherIDVar=StringVar()
Label(publisherpage, font=(myFont,15), text = "Publisher ID  : ", background=myColor, foreground="white").place(relx=0.17, rely=0.18)
id= Entry(publisherpage, textvariable = publisherIDVar, font = (myFont,13,'normal'),)
id.place(relx=0.30, rely=0.205,  width=500, anchor=W)

#name Input
nameVar=StringVar()
Label(publisherpage, font=(myFont,15), text = "Name           : ", background=myColor, foreground="white").place(relx=0.17, rely=0.23)
name= Entry(publisherpage, textvariable = nameVar, font = (myFont,13,'normal'),)
name.place(relx=0.30, rely=0.255,  width=500, anchor=W)

#email name  Input
emailVar=StringVar()
Label(publisherpage, font=(myFont,15), text = "Email           : ", background=myColor, foreground="white").place(relx=0.17, rely=0.28)
email= Entry(publisherpage, textvariable = emailVar, font = (myFont,13,'normal'),)
email.place(relx=0.30, rely=0.305,  width=500, anchor=W)

createButton = Button(publisherpage,text = ' Create ', foreground=myColor, background='white', font=(myFont, 15))
createButton.place(relx=0.30, rely = 0.34)


backButton = Button(publisherpage,text = 'Back', foreground=myColor, background='white', font=(myFont, 10), borderwidth=0)
backButton.place(relx=0.01, rely = 0.02)


publisherpage.mainloop()