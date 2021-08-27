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
import DES, menu , signup

#ANCHOR
class App(Tk):
    def __init__(self):
        super().__init__()
        """
        Starting the login windowCheck if user and password is match and correct
        """
        self.title("White shark tracking")
        self.iconbitmap("./src/wireshark.ico")
        label = Label(self, text="Login")
        self.geometry("400x300")
        label.pack(pady=20)
        #ANCHOR data input
        password = StringVar()
        self.username = StringVar()
        label = Label(self,text="Username").pack()
        username_entry = Entry(self,textvariable= self.username).pack(pady=5)
        label = Label(self,text="Password").pack()
        password_entry = Entry(self,textvariable=password,show="*").pack(pady=5)
        #ANCHOR Buttons for main window
        login_btn = Button(self,
                        text="Login",
                        command=lambda:self.login()
                        ).pack(pady=5)
        signup_btn = Button(self,
                        text="Sign Up",
                        command=lambda:signup.window()
                        ).pack(pady=5)
        quit_btn = Button(self,
                        text="Quit",
                        command=lambda:self.destroy()
                        ).pack(pady=5)
        self.mainloop()
    def login(self):
            menu.window()
            self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()