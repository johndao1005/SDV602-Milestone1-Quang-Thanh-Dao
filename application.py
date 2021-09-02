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
from tkinter import ttk

#create function to make window faster
def createWindow(windowName,windowLabel,windowsize):
    """Short cut to create a window different from pop up window and can add other characterictes

    Args:
        windowName (varible): follow the window= Tk() which specific which window we working on
        windowLabel (string): the name of the window rememer this is different from the top level tittle
        windowsize (string): geometry data of window include the size as well as location if specific
    """
    windowName.title("White shark tracking")
    windowName.iconbitmap()# need ico icond
    label = Label(windowName, text=windowLabel) #adding font to improve styling, example font=("Helvetica", 14), adding side to choose which size it will
    windowName.geometry(windowsize)
    label.pack(pady=20)
    
#ANCHOR
def login():
    root = Tk()
    """
    Starting the login windowCheck if user and password is match and correct
    """
    createWindow(root,"Login","400x300")
    # root.title("White shark tagging log")
    # root.iconbitmap()
    # label = Label()
    # root.geometry("400x200")
        
    password = StringVar()
    username = StringVar()
    label = Label(root,text="Username").pack()
    username_entry = Entry(root,textvariable= username).pack(pady=5)
    label = Label(root,text="Password").pack()
    password_entry = Entry(root,textvariable=password,show="*").pack(pady=5)
    #ANCHOR
    def signUpWindow():
        """Creating Sign up window to Add new User as well as make sure the User is not already in the database
        """
        signup = Toplevel()
        createWindow(signup,"Signup","300x400")
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
    
    #ANCHOR
    def menuWindow():
        """Present the options for users after login
        """
        root.destroy()
        menu = Tk()
        createWindow(menu,"Menu","400x350")
        #ANCHOR
        def DESControl(string):
            """Control all DES at once in order to destroy, withdraw or open them all

            Args:
                string (string): action will be done on all DES ( destroy, withdraw or active)
            """
            try:
                if string == 'destroy':
                    DES1.destroy()
                    DES2.destroy()
                    DES3.destroy()
                elif string == 'withdraw':
                    DES1.withdraw()
                    DES2.withdraw()
                    DES3.withdraw()
                elif string == 'active':
                    # DES1Window()
                    # DES2Window()
                    # DES3Window()
                    pass
            except:
                pass 
        def insertData():
            """Function to insert new data into
            """
            insert = Toplevel()
            createWindow(insert,"New Data","350x420")
            gender = StringVar()
            feature = StringVar()
            note = StringVar()
            locationX = StringVar()
            locationY = StringVar()
            #Creating entry box
            label = Label(insert,text="Gender").pack()
            username_entry = Entry(insert,textvariable= gender).pack(pady=5)
            label = Label(insert,text="feature").pack()
            password_entry = Entry(insert,textvariable=feature).pack(pady=5)
            label = Label(insert,text="Note").pack()
            confirmpassword_entry = Entry(insert,textvariable= note).pack(pady=5)
            label = Label(insert,text="Location").pack()
            email_entry = Entry(insert,textvariable=locationX).pack(pady=5)
            label = Label(insert,text="Location").pack()
            email_entry = Entry(insert,textvariable=locationY).pack(pady=5)
            # data for storage
            # data entry fields
            # valuate data entry
            # add data to database and create popup
            def uploadData():
                """Function to upload and check the data then close all the DES and return to menu
                """
                showinfo(
                    title ="Upload complete",
                    message = "The data has been updated, please reload all Data Explorer Screen"
                )
                DESControl('withdraw')
                insert.destroy()
                
            upload_Btn = Button(insert, text="Upload Data",command= lambda:uploadData()).pack(pady=5)
            cancel_Btn = Button(insert, text="Cancel",command= lambda:insert.destroy()).pack(pady =5)
            
        def update():
            """Function to receive the new data and open popup message to confirm the action as well as close the current DES window
            """
            # Take new data into from spreadsheet 
            showinfo(
                title = "Update data",
                message = "The data has been updated, please close all DES"
            )
        def chat():
            """Place holder for function to update the chat log when there are new chat message
            """
            pass
            #Other functions
            #data interaction
        def zoom():
            """Place holder for function to zoom into the data
            """
            pass
        def pan():
            """Place holder for function to zoom into the data
            """
            pass   
        def changeDES(current,next):
            current.destroy()
            next()
            
        #ANCHOR creating 3 DES including chat box
        def DESWindow(windowname,datatype,nextDES,prevDES):
            """Creating database  Screen Window     
            Args:
                datatype (string ): name of the data is present in for the current DES
            """
            windowname = Toplevel()
            windowname.title("White shark tracking")
            windowname.iconbitmap()
            windowname.geometry("900x1000")
            option1 ={"pady":10,"padx":10}
            label = Label(windowname, text=f"White shark {datatype} data").grid(column=0,row=0,**option1,columnspan=3)
            img = ImageTk.PhotoImage(Image.open(f"./data/{datatype}.png"))
            frame = ttk.Frame(windowname)
            frame.grid(column=0,row=2,**option1,columnspan=2,rowspan=2)
            panel = Label(frame, image = img,width = 500).grid(column=0,row=1,**option1,columnspan=2,rowspan=2)
            # Storing new data
            input = StringVar()
            chatLog = StringVar()
            # chat box creating and function
            frame1 = ttk.LabelFrame(windowname,text="Chat box",borderwidth=0)
            frame1.grid(column=2,row=2,**option1,)
            chatBox = ttk.Label(frame1,
                            background='light gray',
                            textvariable=chatLog,width = 40
                            ).grid(column=1,row=2,**option1,columnspan=2)
            entry = ttk.Entry(frame1, textvariable=input).grid(column=1,row=3,**option1)
            button = ttk.Button(frame1,
                            text="Send",
                            command=lambda: chat()
                            ).grid(column=2,row=3,**option1)
            # ANCHOR Buttons for windowname
            frame2 = ttk.LabelFrame(windowname,text="Chat box",borderwidth=0)
            frame2.grid(column=2,row=3,**option1,sticky=NSEW)
            button = ttk.Button(frame2,
                            text="Next",
                            command=lambda: changeWindow(windowname,nextDES)
                            ).grid(column=0,row=5,**option1)
            button = ttk.Button(frame2,
                            text="Previous",
                            command=lambda: changeWindow(windowname,prevDES)
                            ).grid(column=1,row=5,**option1)
            button = ttk.Button(frame2,
                            text="Zoom +",
                            command=lambda: zoom()
                            ).grid(column=1,row=6,**option1)
            button = ttk.Button(frame2,
                            text="Zoom -",
                            command=lambda: zoom()
                            ).grid(column=0,row=7,**option1)
            Location_windowname = ttk.Button(frame2,
                                text="Pan",
                                command=lambda: pan()
                                ).grid(column=1,row=7,**option1)
            
            # button = Button(windowname,
            #                 text="upload Data",
            #                 command=lambda: chat()
            #                 ).grid(column=0,row=0,**option1)
            button = ttk.Button(windowname,
                            text="Quit",
                            command=lambda: close_DES()
                            ).grid(column=2,row=8,**option1,sticky=SE)
            def chat():
                """Place holder for function to update the chat log when there are new chat message
                """
                pass
            
            def zoom():
                """Place holder for function to zoom into the data
                """
                pass
            def pan():
                """Place holder for function to zoom into the data
                """
                pass

            def changeWindow(current,new):
                """State the current window and next window

                Args:
                    current (variable): name of the current window to be closed_data
                    new (fucntion): name of the function to create the next window
                """
                current.destroy()
                new()
            def close_DES():
                """Function handle to destroy the window
                """
                windowname.destroy()
            windowname.protocol("WM_DELETE_WINDOW",close_DES)
            windowname.mainloop()
        def DES1Window():
            """Function for create first DES which present the locaiton information
            """
            DESWindow(DES1,'location',DES2Window,DES3Window)
        def DES2Window():
            """Function for create seoncd DES which present the locaiton information
            """
            DESWindow(DES2,'gender',DES3Window,DES1Window)
        def DES3Window():
            """Function for create third DES which present the locaiton information
            """
            DESWindow(DES3,'feature',DES1Window,DES2Window)
            
        def signout(para):
            """Sign out function which destroy menu, DES and return to log in window

            Args:
                para (which window change to): choose the window will be display after destroy everything
            """
            try:
                DESControl('destroy')
            except TclError as error:
                pass 
            if para == login:
                menu.destroy()
            para()
        #ANCHOR Buttons for menu
        insert_Btn = Button(menu,
                            text="Insert Data",
                            command=lambda:insertData()
                            ).pack(pady=5)
        DES_Btn = Button(menu,
                            text="Location",
                            command = lambda:DES1Window()
                            ).pack(pady=5)
        DES2_Btn = Button(menu,
                            text="Gender",
                            command = lambda:DES2Window()
                            ).pack(pady=5)
        DES3_Btn = Button(menu,
                            text="Feature",
                            command = lambda:DES3Window()
                            ).pack(pady=5)
        signout_Btn = Button(menu,
                            text="Sign out",
                            command = lambda:signout(login)
                            ).pack(pady=5)
        quit_Btn = Button(menu,
                            text="Quit",
                            command = lambda:menu.destroy()
                            ).pack(pady=5)
        DES1 = Toplevel()
        DES1.withdraw()
        DES2 = Toplevel()
        DES2.withdraw()
        DES3 = Toplevel()
        DES3.withdraw() 
        menu.mainloop()
    #ANCHOR Buttons for main window
    button = Button(root,
                    text="Login",
                    command=lambda:menuWindow()
                    ).pack(pady=5)
    button = Button(root,
                    text="Sign Up",
                    command=lambda:signUpWindow()
                    ).pack(pady=5)
    button = Button(root,
                    text="Quit",
                    command=lambda:root.destroy()
                    ).pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    login()