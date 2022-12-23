#Import the required library
from tkinter import *
import ttk

#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("750x250")

#Define a function to close the popup window
def close_win(top):
   top.destroy()
def insert_val(e):
   e.insert(0, "Hello World!")

#Define a function to open the Popup Dialogue
def popupwin():
   #Create a Toplevel window
   top= Toplevel(win)
   top.geometry("750x250")

   #Create an Entry Widget in the Toplevel window
   # entry= Entry(top, width= 25)
   # entry.pack()

   #Create a Button to print something in the Entry widget
   # Button(top,text= "Insert", command= lambda:insert_val(entry)).pack(pady= 5,side=TOP)
   #Create a Button Widget in the Toplevel Window
   # button= Button(top, text="Ok", command=lambda:close_win(top))
   # button.pack(pady=5, side= TOP)

   combo = ttk.Combobox(top)
   combo['values'] = ["Raymond","Maria","Rachel","Anya"]
   combo['state'] = 'normal'
   combo.place(relx=.5, rely=.5)
   combo.get()

   Button(top,text= "Insert", command= lambda:print(combo.get())).place(relx= .5,rely=.2)

   # print(combo.get())

#Create a Label
label= Label(win, text="Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
label.pack(pady=20)

#Create a Button
button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
win.mainloop()