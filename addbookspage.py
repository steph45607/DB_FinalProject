# Import module 
from tkinter import *
from tkinter import OptionMenu
import tkinter.font as font
from main import *
from methods import *

# Create object 
addbooks = Tk()

# Adjust size 
addbooks.geometry("1000x600")
addbooks.resizable(False, False)
addbooks.title("BookStack LMS") 
# Add image file
background = PhotoImage(file = "images/backgroundAddBooks.png")

myFont = font.Font(family='Helvetica')
myColor = "#1A371B"

# Show image using label
backgroundlabel = Label(addbooks, image = background, background="white" )
backgroundlabel.place(x = -1, y = -1)

Label(addbooks, font=('Helvetica Bold',23), text = " Add Book Details ", background=myColor, foreground='white').place(relx=0.38, rely=0.1)


#bookID input
bookIDVar=StringVar()
Label(addbooks, font=(myFont,15), text = "Book ID   : ", background=myColor, foreground="white").place(relx=0.17, rely=0.18)
id= Entry(addbooks, textvariable = bookIDVar, font = (myFont,13,'normal'),)
id.place(relx=0.28, rely=0.205,  width=500, anchor=W)

#title Input
titleVar=StringVar()
Label(addbooks, font=(myFont,15), text = "Title         : ", background=myColor, foreground="white").place(relx=0.17, rely=0.23)
title= Entry(addbooks, textvariable = titleVar, font = (myFont,13,'normal'),)
title.place(relx=0.28, rely=0.255,  width=500, anchor=W)

#Author input
author_name = StringVar()
author_list = dropDown("author_details") 
Label(addbooks, font=(myFont,15), text = "Author      : ", background=myColor, foreground="white").place(relx=0.17, rely=0.29)
author_dropdown = OptionMenu(addbooks, author_name, *author_list).place(relx = 0.28, rely=0.31, width=500, anchor=W)

#publisher input
pub = StringVar()
pub_list = dropDown("publisher_details")
Label(addbooks, font=(myFont,15), text = "Publisher  : ", background=myColor, foreground="white").place(relx=0.17, rely=0.35)
pub_dropdown = OptionMenu(addbooks, pub, *pub_list).place(relx=0.28, rely=0.370, width=500, anchor=W)

#isbn input
isbnVar =StringVar()
Label(addbooks, font=(myFont,15), text = "ISBN        : ", background=myColor, foreground="white").place(relx=0.17, rely=0.405)
isbn= Entry(addbooks, textvariable = isbnVar, font = (myFont,13,'normal'),)
isbn.place(relx=0.28, rely=0.425,  width=500, anchor=W)

#group input
group = StringVar()
group_list = dropDown("group_details")
Label(addbooks, font=(myFont,15), text = "Group      : ", background=myColor, foreground="white").place(relx=0.17, rely=0.455)
group_dropdown = OptionMenu(addbooks, group, *group_list).place(relx=0.28, rely=0.48, width=500, anchor=W)

#status input
status = StringVar()
status_list = dropDown("status_details")
Label(addbooks, font=(myFont,15), text = "Status      : ", background=myColor, foreground="white").place(relx=0.17, rely=0.515)
status_dropdown = OptionMenu(addbooks, status, *status_list).place(relx=0.28, rely=0.540, width = 500, anchor=W)

#damages input
damages = StringVar()
damages_list = dropDown("damages_details")
Label(addbooks, font=(myFont,15), text = "Damages : ", background=myColor, foreground="white").place(relx=0.17, rely=0.57)
damages_dropdown = OptionMenu(addbooks, damages, *damages_list).place(relx=0.28, rely=0.6, width=500, anchor=W)

subButton = Button(addbooks,text = ' Submit ', command =lambda:print(pub.get()), foreground=myColor, background='white', font=(myFont, 15))
subButton.place(relx=0.28, rely = 0.64)

#i cant fnd the command for the display button but here it is tinggal nambahin the command
displayButton = Button(addbooks,text = ' Display ', foreground=myColor, background='white', font=(myFont, 15) )
displayButton.place(relx=0.375, rely = 0.64)

backButton = backButton = Button(addbooks,text = 'Back', foreground=myColor, background='white', font=(myFont, 10), borderwidth=0)
backButton.place(relx=0.01, rely = 0.02)

# #havent added any commands, but this button to return to prev page
# backButton = backButton = Button(addbooks,text = '  Back  ', foreground=myColor, background='white', font=(myFont, 15))
# backButton.place(relx=0.475, rely = 0.64)

addbooks.mainloop()