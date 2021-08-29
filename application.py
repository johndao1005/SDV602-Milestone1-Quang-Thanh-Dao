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
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import menu , setup

class App(Tk):
    def __init__(self):
        """Start an instance of login screen which allow user to sign up with top level window or login directly
        When users login, the class would open to menu which is another class which handle the data view, update, delete while
        destroy the current login to prevent multiple login.
        """
        super().__init__()
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        options = setup.pad10
        option2 = setup.pad5
        self.resizable(0, 0)
        label = Label(self, text="Login").grid(column=0,row=0,sticky=N,**options,columnspan=3)
        self.geometry("280x250")
        self.check = False
    
        # ANCHOR data input
        lf = Frame(
        self,
        ).grid(column=0, row=0, padx=10, pady=0)
        password = StringVar()
        username = StringVar()
        label = ttk.Label(lf, text="Username").grid(column=0,row=1,**options,ipadx=5, ipady=5)
        username_entry = Entry(lf, textvariable=username).grid(column=1,row=1,**options,columnspan=2)
        label = ttk.Label(lf, text="Password").grid(column=0,row=2,**options,ipadx=5, ipady=5)
        password_entry = Entry(lf, textvariable=password, show="*").grid(column=1,row=2,**options,columnspan=2)
        
        # ANCHOR Buttons for main window
        button_frame = ttk.Frame(
        self,
        ).grid(column=1, row=1, padx=10, pady=10)
        login_btn = ttk.Button(button_frame,
                           text="Login",
                           command=lambda: self.login(username,password)
                           ).grid(column=1,row=3,**option2)
        signup_btn = ttk.Button(button_frame,
                            text="Sign Up",
                            command=lambda: self.call_signup()
                            ).grid(column=2,row=3,**option2)
        quit_btn = ttk.Button(self,
                          text="Quit",
                          command=lambda: self.destroy()
                          ).grid(column=2,row=4,**options)
        
    def call_signup(self):
        """The function check for any instance of signup and only create a sign up window if there is none
        """
        if self.check == False:
            self.signup_window()
            
    def signup_window(self):
            """This function is used to create a sign up window to complete sign up action
            """
            self.check = True
            self.signup = Tk()
            self.signup.title(setup.app_name)
            self.signup.iconbitmap(setup.icon)
            options = {'padx': 10, 'pady': 5}
            label = Label(self.signup, text="Sign up").grid(column=0,row=0,**options,columnspan=2)
            self.signup.geometry("310x360")
            self.signup.protocol("WM_DELETE_WINDOW",self.closeSignup)
            #Create placeholder to store data
            username = StringVar()
            password = StringVar()
            confirmPassword = StringVar()
            email = StringVar()
            lf = ttk.LabelFrame(self.signup, text= "Login details")
            lf.grid(column=0,row=1, padx=20, pady=20)
            label = ttk.Label(lf,text="Username").grid(column=0,row=3,**options)
            username_entry = ttk.Entry(lf,textvariable= username).grid(column=1,row=3,**options)
            username_check = ttk.Label(lf,text="").grid(column=1,row=4)
            label = ttk.Label(lf,text="Pass word").grid(column=0,row=5,**options)
            password_entry = ttk.Entry(lf,textvariable=password).grid(column=1,row=5,**options)
            password_check = ttk.Label(lf,text="").grid(column=1,row=6)
            label = ttk.Label(lf,text="Confirm Password").grid(column=0,row=7,**options)
            confirmpassword_entry = ttk.Entry(lf,textvariable= confirmPassword).grid(column=1,row=7,**options)
            confirm_password_check = ttk.Label(lf,text="").grid(column=1,row=8)
            label = ttk.Label(lf,text="Email").grid(column=0,row=9,**options)
            email_entry = ttk.Entry(lf,textvariable=email).grid(column=1,row=9,**options)
            email_check = ttk.Label(lf,text="").grid(column=1,row=10)
            button = ttk.Button(lf,
                            text="Sign Up",
                            command=lambda:self.makeUser(username, password, confirmPassword,email)
                            ).grid(column=0,row=11,**options,columnspan=2)
            button = ttk.Button(self.signup,
                            text="Cancel",
                            command=lambda:self.closeSignup()
                            ).grid(column=0,row=3,**options,sticky=SE)
            self.signup.mainloop()

    def closeSignup(self):
        """This function make sure that the window is closed and allow to create new instance of Sign up window
        """
        self.check = False
        self.signup.destroy()
    
    def makeUser(self,name,pw,pw2,email):
        """Checking input is valid and not already exist in the current database before creating new user instance

        Args:
            name (string): username taken from user input, need to be more than 2 characters and less than 20 characters
            pw (string):  password taken from user input, need to be more than 8 character and less than 20 characters
            pw2 (string): confirm password, need to be identical with password input
            email (string): email from user, need to have @ and valid email name
        """
        pass
    
    def login(self,name,pw=""):
        """Function to check the if username and password is correct then destroy the login window
        and open the main menu to allow users interact with the application

        Args:
            name (string): username from user input
            pw (string): password from user input
        """
        
        self.destroy()
        menu.window(name)

def create_menu():
    app = App()
    app.mainloop()  
    print(type(app))
if __name__ == "__main__":
    create_menu()