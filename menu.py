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
import application, DES

def window():
        """Present the options for users after login
        """
        menu = Tk()
        menu.title("White shark tracking")
        menu.iconbitmap("./src/wireshark.ico")
        label = Label(menu, text="Menu")
        menu.geometry("400x350")
        label.pack(pady=20)
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
        def UploadData():
            """Function to upload new data into
            """
            upload = Toplevel()
            upload.title("White shark tracking")
            upload.iconbitmap("./src/wireshark.ico")
            label = Label(upload, text="New Data")
            upload.geometry("350x420")
            label.pack(pady=20)
            gender = StringVar()
            feature = StringVar()
            note = StringVar()
            locationX = StringVar()
            locationY = StringVar()
            #Creating entry box
            label = Label(upload,text="Gender").pack()
            username_entry = Entry(upload,textvariable= gender).pack(pady=5)
            label = Label(upload,text="feature").pack()
            password_entry = Entry(upload,textvariable=feature).pack(pady=5)
            label = Label(upload,text="Note").pack()
            confirmpassword_entry = Entry(upload,textvariable= note).pack(pady=5)
            label = Label(upload,text="Location").pack()
            email_entry = Entry(upload,textvariable=locationX).pack(pady=5)
            label = Label(upload,text="Location").pack()
            email_entry = Entry(upload,textvariable=locationY).pack(pady=5)
            # data for storage
            # data entry fields
            # valuate data entry
            # add data to database and create popup
        def uploadData():
            """Function to upload and check the data then close all the DES and return to menu
            """
            upload = Toplevel()
            showinfo(
                title ="Upload complete",
                message = "The data has been updated, please reload all Data Explorer Screen"
            )
            DESControl('withdraw')
            upload.destroy()
                
            upload_Btn = Button(upload, text="Upload Data",command= lambda:uploadData()).pack(pady=5)
            cancel_Btn = Button(upload, text="Cancel",command= lambda:upload.destroy()).pack(pady =5)
            
        def update():
            """Function to receive the new data and open popup message to confirm the action as well as close the current DES window
            """
            # Take new data into from spreadsheet 
            showinfo(
                title = "Update data",
                message = "The data has been updated, please close all DES"
            )    
        #ANCHOR creating 3 DES including chat box
        
        def DES1Window():
            DES.window(DES1,'location',DES2Window,DES3Window)
        def DES2Window():
            DES.window(DES2,'gender',DES3Window,DES1Window)
        def DES3Window():
            DES.window(DES3,'feature',DES1Window,DES2Window)
            
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
        upload_Btn = Button(menu,
                            text="upload Data",
                            command=lambda:uploadData()
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