# Import module 
from tkinter import *
import tkinter.font as font
  
# Create object 
root = Tk()
  
# Adjust size 
root.geometry("1000x600")

root.title("BookStack LMS") 

# Add image file
background = PhotoImage(file = "images/backgroundLandingPage.png")
logo = PhotoImage(file = "images/logo.png" )
qr = PhotoImage(file="images/qr.png")

myFont = font.Font(family='Helvetica')

# Show image using label
backgroundlabel = Label(root, image = background, background="white" )
backgroundlabel.place(x = 0, y = 0)

logolabel = Label(root, image = logo)
logolabel.place(relx=0.143, rely = 0.38)

# frameButton = Frame(root)
# frameButton.pack(pady=10, side=LEFT )

userButton = Button(root, font=(myFont,18), text = "  User  ", background="#2C602E", foreground="white")
userButton.place(relx=0.18, rely = 0.6)

adminButton = Button(root, font=(myFont,18), text = " Admin ", background="#2C602E", foreground="white")
adminButton.place(relx=0.29, rely = 0.6)

frameright = Frame(root)
frameright.pack(pady=10, side=LEFT )

# T = Text(root, height = 5, width = 52)
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


# root.create_line(100,200,200,35, fill="green", width=5)
# # Create Frame
# frame1 = Frame(root)
# frame1.pack(pady = 20 )
  
# # Add buttons
# button1 = Button(frame1,text="Exit")
# button1.pack(pady=20)
  
# button2 = Button( frame1, text = "Start")
# button2.pack(pady = 20)
  
# button3 = Button( frame1, text = "Reset")
# button3.pack(pady = 20)
  
# Execute tkinter
root.mainloop()