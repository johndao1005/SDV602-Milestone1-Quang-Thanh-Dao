# """
# Import all the functions of tkinter library to support the process of building application

# """
# from tkinter import *
# from PIL import ImageTk,Image
# from tkinter.messagebox import showinfo

# def changeWindow(show,hide):
#             """Changing between windows by state which window is present and which one is hidden

#             Args:
#                 show (variable): window want to show
#                 hide (variable): window need to hide
#             """
#             show.deiconify()
#             hide.withdraw()

# def createPopup(title, message):
#     """Creating pop up message to indicate the status of application such as error or such success

#     Args:
#         title (string): Name of the message to display
#         message (string): Content of the message such as what is the error or what action is completely
#     """
#     #other option showerror(title, message) 
#     #showwarrning(title, message)
#     showinfo(
#                 title = title,
#                 message =message
#             )
    

# #create function to make window faster
# def createWindow(windowName,windowLabel,windowsize):
#     """Short cut to create a window different from pop up window and can add other characterictes

#     Args:
#         windowName (varible): follow the window= Tk() which specific which window we working on
#         windowLabel (string): the name of the window rememer this is different from the top level tittle
#         windowsize (string): geometry data of window include the size as well as location if specific
#     """
#     windowName.title("white shark track")
#     windowName.iconbitmap()# need ico icond
#     label = Label(windowName, text=windowLabel) #adding font to improve styling, example font=("Helvetica", 14), adding side to choose which size it will
#     windowName.geometry(windowsize)
#     label.pack(pady=20)
#     #adding picture to window 
#     #     photo = tk.PhotoImage(file="./assets/python.png")
#     # image_label = ttk.Label(
#     #     root,
#     #     image=photo,
#     #     padding=5
#     # )
#     # image_label.pack()
#     #
    
# #ANCHOR
# def login():
#     root = Tk()
#     """
#     Starting the login windowCheck if user and password is match and correct
#     """
#     createWindow(root,"Login","400x300")
#     # root.title("White shark tagging log")
#     # root.iconbitmap()
#     # label = Label()
#     # root.geometry("400x200")

#     password = StringVar()
#     username = StringVar()
#     username_entry = Entry(root,textvariable= username).pack(pady=5)
#     password_entry = Entry(root,textvariable=password,show="*").pack(pady=5)
    
#     #ANCHOR
#     def signUpWindow():
#         """Creating Sign up window to Add new User as well as make sure the User is not already in the database
#         """
#         signup = Toplevel()
#         createWindow(signup,"Signup","300x250")
#         username = StringVar()
#         password = StringVar()
#         confirmPassword = StringVar()
#         email = StringVar()
#         #Creating entry box
#         username_entry = Entry(signup,textvariable= username).pack(pady=10)
#         password_entry = Entry(signup,textvariable=password,show="*").pack(pady=10)
#         confirmpassword_entry = Entry(signup,textvariable= username).pack(pady=10)
#         email_entry = Entry(signup,textvariable=password,show="*").pack(pady=10)
#         def makeUser():
#             """check the username and password if existed
#                 after create user then 
#             """
            
#             pass
#         button = Button(signup,
#                         text="Sign Up",
#                         command=lambda:makeUser()
#                         ).pack(pady=5)
#         button = Button(signup,
#                         text="Cancel",
#                         command=lambda:signup.destroy()
#                         ).pack(pady=5)
#         signup.mainloop()
    
#     #ANCHOR
#     def menuWindow():
#         """Present the options for users after login and will create the branch from here
#         """
#         root.destroy()
#         menu = Tk()
#         createWindow(menu,"Menu","350x300")
#         DES1 = Tk()
#         DES1.withdraw()
#         DES2 = Tk()
#         DES2.withdraw()
#         DES3 = Tk()
#         DES3.withdraw()
#         def insertData():
#             """Function to insert new data into
#             """
#             newData = Toplevel()
#             # data for storage
#             # data entry fields
#             # valuate data entry
#             # add data to database and create popup
#             createPopup("Upload Complete","The data is saved to the database.")
#             DES1.withdraw()
            
#             # house_price = np.random.normal(2000,25000, 5000)
#             # plt.hist(house_price,50)
#             # plt.show()
#         #ANCHOR creating 3 DES including chat box
#         def DES1Window(datatype):
#             DES1.deiconify()
#             """Creating database  Screen Window     

#             Args:
#                 datatype (string ): name of the data is present in for the current DES
#             """
            
#             createWindow(DES1,"Data Display Screen","800x600")
#             label = Label(DES1, text =f"White shark {datatype} data").pack()
#             def update():
#                 """Function to receive the new data and open popup message to confirm the action as well as close the current DES window
#                 """
#                 # Take new data into from spreadsheet 
#                 createPopup("Update complete", "The data is is refreshed.")
#                 DES1.withdraw()
#                 pass
#             img = ImageTk.PhotoImage(Image.open(f"./data/gender.png"))
#             panel = Label(DES1, image = img,width =300,heigh = 500)
#             panel.pack(side = LEFT)
#             # Storing new data
#             input = StringVar()
#             chatLog = StringVar()
#             #chat box creating and function
#             chatLabel = Label(DES,text = "Chat box").pack(side=LEFT)
#             chatBox = Label(DES,
#                                 background='light gray', width=20,height =30,
#                                 textvariable=chatLog,
#                                 compound = LEFT,
#                                 anchor="w").pack(side=LEFT)
#             inputLabel = Label(DES,text = "Input").pack(side=LEFT)
#             entry = Entry(DES,textvariable=input).pack(side=LEFT)
#             def chat():
#                 """Place holder for function to update the chat log when there are new chat message
#                 """
#                 pass
#             #Other functions
#             #data interaction
#             def zoom():
#                 """Place holder for function to zoom into the data
#                 """
#                 pass
#             def pan():
#                 """Place holder for function to zoom into the data
#                 """
#                 pass
#             #ANCHOR Buttons for DES
#             button = Button(DES,
#                             text="Zoom",
#                             command=lambda:zoom()
#                             ).pack(pady=5)
#             Location_DES = Button(DES,
#                                 text="Pan",
#                                 command = lambda:pan()
#                                 ).pack(pady=5)
#             button = Button(DES,
#                             text="Send",
#                             command=lambda:chat()
#                             ).pack(pady=5)
#             button = Button(DES,
#                             text="Insert Data",
#                             command=lambda:insertData()
#                             ).pack(pady=5)
#             button = Button(DES,
#                             text="Update data",
#                             command=lambda:update()
#                             ).pack(pady=5)
            
#             DES.mainloop()
#         #ANCHOR Buttons for menu
#         button = Button(menu,
#                             text="Insert Data",
#                             command=lambda:insertData()
#                             ).pack(pady=5)
#         Location_DES = Button(menu,
#                             text="Location",
#                             command = lambda:DESWindow("location")
#                             ).pack(pady=5)
#         Gender_DES = Button(menu,
#                             text="Gender",
#                             command = lambda:DESWindow("gender")
#                             ).pack(pady=5)
#         Feature_DES = Button(menu,
#                             text="Feature",
#                             command = lambda:DESWindow("feature")
#                             ).pack(pady=5)
#         Signout = Button(menu,
#                             text="Sign out",
#                             command = lambda:changeWindow(root,menu)
#                             ).pack(pady=5)
#         menu.mainloop() 
#     #ANCHOR Buttons for main window
#     button = Button(root,
#                     text="Sign Up",
#                     command=lambda:signUpWindow()
#                     ).pack(pady=5)
#     button = Button(root,
#                     text="Login",
#                     command=lambda:menuWindow()
#                     ).pack(pady=5)
#     root.mainloop()

# if __name__ == "__main__":
#     app = new App()Application
#     login()