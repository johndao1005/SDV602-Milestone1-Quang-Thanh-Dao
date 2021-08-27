"""
Import all the functions of tkinter library to support the process of building application such as:
Tk(): create main window
Toplevel(): create child window
Button(): create button with name and function or command attach
destroy(): destroy the current window
withdraw(): hide the current window
Label(): can be used to display text, image
Entry(): can be used to create text box

"""
from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo
import application

def window():
        """Creating Sign up window to Add new User as well as make sure the User is not already in the database
        """
        signup = Toplevel()
        signup.title("White shark tracking")
        signup.iconbitmap("./src/wireshark.ico")
        label = Label(signup, text="Sign up")
        signup.geometry("300x400")
        label.pack(pady=20)
        username = StringVar()
        password = StringVar()
        confirmPassword = StringVar()
        email = StringVar()
        #Creating entry box
        label = Label(signup,text="Username").pack()
        username_entry = Entry(signup,textvariable= username).pack(pady=10)
        label = Label(signup,text="Pass word").pack()
        password_entry = Entry(signup,textvariable=password,show="*").pack(pady=10)
        label = Label(signup,text="Email").pack()
        email_entry = Entry(signup,textvariable=confirmPassword,show="*").pack(pady=10)
        label = Label(signup,text="Confirm Password").pack()
        confirmpassword_entry = Entry(signup,textvariable= email).pack(pady=10)
        def makeUser():
            """check the username and password if existed
                after create user then 
            """
            
            pass
        button = Button(signup,
                        text="Sign Up",
                        command=lambda:makeUser()
                        ).pack(pady=5)
        button = Button(signup,
                        text="Cancel",
                        command=lambda:signup.destroy()
                        ).pack(pady=5)
        signup.mainloop()
    