from tkinter import *
import tkinter.font as font

import frames
global root

def main():
    # Window size variables
    width = 1000
    height = 600

    # Create tkinter root
    global root
    root = Tk()
    root.config(bg="#2C602E")
    root.title("Library Management System")
    global myFont
    myFont = font.Font(family="Helvetica")

    # Assign value of device screen size
    setW = root.winfo_screenwidth()
    setH = root.winfo_screenheight()

    # Set the padding so it will position window center
    padW = (setW//2)-(width//2)
    padH = (setH//2)-(height//2)

    # Set the window size and position
    root.geometry(f"{width}x{height}+{padW}+{padH}")
    root.resizable(False, False)

    # To fill in the window with widgets from frames.py
    frames.menuPage(root)

    # To run the window
    root.mainloop()


if __name__ == "__main__":
	main()
