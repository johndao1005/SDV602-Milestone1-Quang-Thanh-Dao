"""
Import all the functions of tkinter library to support the process of building application

"""
from tkinter import *
from PIL import ImageTk,Image
from tkinter.messagebox import showinfo


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
        def DESWindow(windowname,datatype,nextDES,previousDES):
            """Creating database  Screen Window     

            Args:
                datatype (string ): name of the data is present in for the current DES
            """
            windowname = Toplevel()
            createWindow(windowname, f"White shark {datatype} data","800x600")
            
            img = ImageTk.PhotoImage(Image.open(datatype+".png"))
            panel = Label(master = windowname, image = img ,width =200,heigh = 500)
            panel.pack(side=LEFT)
            
            # Storing new data
            input = StringVar()
            chatLog = StringVar()
            #chat box creating and function
            chatLabel = Label(windowname,text = "Chat box").pack(side=LEFT)
            chatBox = Label(windowname,
                                background='light gray', width=20,height =30,
                                textvariable=chatLog,
                                compound = LEFT,
                                anchor="w").pack(side=LEFT)
            inputLabel = Label(windowname,text = "Input").pack(side=LEFT)
            entry = Entry(windowname,textvariable=input).pack(side=LEFT)
            #ANCHOR Buttons for DES
            button = Button(windowname,
                            text="Next",
                            command=lambda:changeDES(windowname,nextDES)
                            ).pack(pady=5)
            button = Button(windowname,
                            text="Previous",
                            command=lambda:changeDES(windowname,previousDES)
                            ).pack(pady=5)
            button = Button(windowname,
                            text="Zoom +",
                            command=lambda:zoom()
                            ).pack(pady=5)
            button = Button(windowname,
                            text="Zoom -",
                            command=lambda:zoom()
                            ).pack(pady=5)
            Location_DES = Button(windowname,
                                text="Pan",
                                command = lambda:pan()
                                ).pack(pady=5)
            button = Button(windowname,
                            text="Send",
                            command=lambda:chat()
                            ).pack(pady=5, side =['left'])
            button = Button(windowname,
                            text="Insert Data",
                            command=lambda:insertData()
                            ).pack(pady=5)
            button = Button(windowname,
                            text="Update data",
                            command=lambda:update()
                            ).pack(pady=5)
            windowname.mainloop()
            
        def DES1Window():
            DESWindow(DES1,'location',DES2Window,DES3Window)
        def DES2Window():
            DESWindow(DES2,'gender',DES3Window,DES1Window)
        def DES3Window():
            DESWindow(DES3,'feature',DES1Window,DES2Window)
            
        
            
        def signout(para):
            try:
                DESControl('destroy')
            except TclError as error:
                pass 
            if para == login:
                menu.destroy()
            para()
        #ANCHOR Buttons for menu
        full_Btn = Button(menu,
                            text="Full Data",
                            command=lambda:DESControl('active')
                            ).pack(pady=5)
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