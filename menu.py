from tkinter import *
import tkinter as tk
# from PIL import ImageTk,Image
# import numpy as np
# import matplotlib.pyplot as plt
from tkinter.messagebox import showinfo

# create function to create short hand for pop up message
def createPopup(title, message):
    """Creating pop up message to indicate the status of application such as error or such success

    Args:
        title (string): Name of the message to display
        message (string): Content of the message such as what is the error or what action is completely
    """
    showinfo(
                title = title,
                message =message
            )

# create function to create button faster
def createButton(windowName,buttonName,buttonFunction):
    """Short cut for creating button by only specifiy the charactistics

    Args:
        windowName (variable): the name of the window the button will apply to example root, menu, signup
        buttonName (string): Text display inside the button which will need to explain the function of the buttonName
        buttonFunction (function name): function will be trigger when click the button
    """
    button = Button(windowName,text=buttonName,
                    #image=download_icon, # can be used to add picture
                    #compound = tk.Left # can be used to make the text and picture inline
                    command=lambda:buttonFunction()).pack(pady=20)

#create function to make window faster
def createWindow(windowName,windowLabel,windowsize):
    """Short cut to create a window different from pop up window and can add other characterictes

    Args:
        windowName (varible): follow the window= Tk() which specific which window we working on
        windowLabel (string): the name of the window rememer this is different from the top level tittle
        windowsize (string): geometry data of window include the size as well as location if specific
    """
    windowName.title("white shark tagging log")
    windowName.iconbitmap()# need ico icond
    label = Label(windowName, text=windowLabel) #adding font to improve styling, example font=("Helvetica", 14), adding side to choose which size it will
    windowName.geometry(windowsize)
    label.pack(pady=20)
    #adding picture to window 
    #     photo = tk.PhotoImage(file="./assets/python.png")
    # image_label = ttk.Label(
    #     root,
    #     image=photo,
    #     padding=5
    # )
    # image_label.pack()
    #
    
    
#ANCHOR
def login():
    """
    Starting the login windowCheck if user and password is match and correct
    """
    createWindow(root,"Login","400x300")
    # root.title("White shark tagging log")
    # root.iconbitmap()
    # label = Label()
    # root.geometry("400x200")
    # def graph():
    #     house_price = np.random.normal(2000,25000, 5000)
    #     plt.hist(house_price,50)
    #     plt.show()
    
    password = tk.StringVar()
    username = tk.StringVar()
    username_entry = Entry(root,textvariable= username).pack(pady=10)
    password_entry = Entry(root,textvariable=password,show="*").pack(pady=10)
    
    #ANCHOR
    def signUpWindow():
        """Creating Sign up window to Add new User as well as make sure the User is not already in the database
        """
        signup = Toplevel()
        createWindow(signup,"Signup","300x250")
        username = tk.StringVar
        password = tk.StringVar
        username_entry = Entry(signup,textvariable= username).pack(pady=10)
        password_entry = Entry(signup,textvariable=password,show="*").pack(pady=10)
        def makeUser():
            """check the username and password if existed
                after create user then 
            """
            
            pass
        createButton(signup,"Sign Up",makeUser)
        signup.mainloop()
    
    
    #ANCHOR
    def menuWindow():
        """Present the options for users after login and will create the branch from here
        """
        root.withdraw()
        menu = Tk()
        createWindow(menu,"Menu","350x300")

        def changeWindow(show,hide):
            show.deiconify()
            hide.withdraw()
        # Anchor pop 
        def insertData():
            newData = Toplevel()
            
            # data for storage
            
            # data entry fields
            
            # valuate data entry
            
            # add data to database and create popup
            createPopup("Upload Complete","The data is saved to the database.")
            pass
            
        
            # house_price = np.random.normal(2000,25000, 5000)
            # plt.hist(house_price,50)
            # plt.show()
        #ANCHOR creating 3 DES including chat box
        def DESWindow(datatype):
            DES = Toplevel()
            createWindow(DES,"Data Display Screen","600x600")
            def update():
                # Take new data into from spreadsheet 
                createPopup("Update complete", "The data is is refreshed.")
                pass
            # Storing new data
            input,chatLog = tk.StringVar()
            #chat box creating and function
            chatBox = tk.Label(DES,
                                background='light gray', width=20,
                                textvariable=chatLog,
                                anchor="w").pack()
            entry = Entry(DES,textvariable=input).pack()
            def chat():
                pass
            #Other functions
            #Creating buttons for DES
            createButton(DES,"Send",chat)
            createButton(DES,"Insert Data",insertData)
            createButton(DES,"Insert Datay",insertData)
            createButton(DES,"Update Data",update)
        
        createButton(menu,"Insert Data",insertData)
        Location_DES = Button(menu,text="Location",command = lambda:DESWindow("location")).pack(pady=10)
        Gender_DES = Button(menu,text="Gender",command = lambda:DESWindow("Gender")).pack(pady=10)
        Feature_DES = Button(menu,text="Feature",command = lambda:DESWindow("Feature")).pack(pady=10)
        Signout = Button(menu,text="Sign out",command = lambda:changeWindow(root,menu)).pack(pady=10)
        menu.mainloop() 
    # pack the 2 button
    createButton(root,"Sign Up",signUpWindow)
    createButton(root,"Login",menuWindow)
    root.mainloop()

if __name__ == "__main__":
    root = Tk()
    login()