"""
Import all the functions of tkinter library to support the process of building application such as:
Tk(): create main window
Toplevel(): create child window
Button(): create button with name and function or command attach
windownametroy(): windownametroy the current window
withdraw(): hide the current window
Label(): can be used to display text, image
Entry(): can be used to create text box

"""
from tkinter import *
from PIL import ImageTk, Image
from tkinter.messagebox import showinfo
from tkinter import ttk
import setup,menu



if __name__ == "__main__":
    app = window("root","gender",2,3)
    
