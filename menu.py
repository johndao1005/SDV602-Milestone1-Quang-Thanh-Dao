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
import application, DES,setup


class window(Tk):
    def __init__(self,name="user"):
        """start an instance of the application which present the menu for user to interact with the database and import the
        user login details from database

        Args:
            name (string): username
        """
        self.user = name
        super().__init__()
        self.title(setup.app_name)
        self.iconbitmap(setup.icon)
        option3 = setup.pad20
        option1 = setup.pad10
        option2 = setup.pad5
        label = Label(self, text="Application Menu").grid(column=0,row=0,**option3)
        self.geometry("330x380")
        self.check = False
        # ANCHOR first label frame
        label = Label(self, text=f"Welcome {self.user},\n Please select one data explorer screen from below").grid(column=0,row=1,**option2)
        lf = ttk.LabelFrame(self, text ="Data View")
        lf.grid(column=0,row=2,**option3)
        DES_Btn = ttk.Button(lf,
                            text="Location",
                            command = lambda:self.DES1_window()
                            ).grid(column=0,row=3,**option1)
        DES2_Btn = ttk.Button(lf,
                            text="Gender",
                            command = lambda:self.DES2_window()
                            ).grid(column=1,row=3,**option1)
        DES3_Btn = ttk.Button(lf,
                            text="Feature",
                            command = lambda:self.DES3_window()
                            ).grid(column=2,row=3,**option1)
        # ANCHOR second label frame
        lf2 = ttk.LabelFrame(self, text ="Actions")
        lf2.grid(column=0,row=4,**option3)
        upload_Btn = ttk.Button(lf2,
                            text="Upload Data",
                            command=lambda:self.open_upload()
                            ).grid(column=0,row=4,**option1)
        signout_Btn = ttk.Button(lf2,
                            text="Chat box",
                            command = lambda:self.signout()
                            ).grid(column=1,row=4,**option1)
        signout_Btn = ttk.Button(lf2,
                            text="Sign out",
                            command = lambda:self.signout()
                            ).grid(column=2,row=4,**option1)
        quit_Btn = ttk.Button(self,
                            text="Quit",
                            command = lambda:self.destroy()
                            ).grid(column=0,row=5,**option1,sticky=SE)
        self.DES1 = Toplevel()
        self.DES1.withdraw()
        self.DES2 = Toplevel()
        self.DES2.withdraw()
        self.DES3 = Toplevel()
        self.DES3.withdraw() 
    
    #ANCHOR creating 3 DES
    def DES1_window(self):
        if "location" not in des_check:
            print(des_check)
            des_check.add("location")
            DES.window(self.DES1,'location',self.DES2_window,self.DES3_window)
            print(des_check)
    def DES2_window(self):
        if "gender" not in des_check:
            des_check.add("gender")
            DES.window(self.DES2,'gender',self.DES3_window,self.DES1_window)
            print(des_check)
    def DES3_window(self):
        if "feature" not in des_check:
            des_check.add("feature")
            DES.window(self.DES3,'feature',self.DES1_window,self.DES2_window)
            print(des_check)
    def DES_window(self,datatype):
        if datatype not in des_check:
            des_check.add(datatype)
            DES.window(self.DES1,datatype,self.DES2_window,self.DES3_window)
        pass
    
    def upload_window(self,user="user"):
        self.upload = Toplevel()
        self.upload.title(setup.app_name)
        self.upload.iconbitmap(setup.icon)
        option2 = setup.pad10
        option1 = setup.pad5
        label = Label(self.upload, text="New Data").grid(column=0,row=0,**option2)
        self.upload.geometry("440x320")
        self.upload.protocol("WM_DELETE_WINDOW",self.close_upload)
        label = Label(self.upload, text=f"Thank you {user}, please fill the details below for new entry.\n We can use your current location or you can manual input your coordinate").grid(column=0,row=1,**option1)
        gender = StringVar()
        feature = StringVar()
        note = StringVar()
        locationX = StringVar()
        locationY = StringVar()
        # Creating entry box
        lf = ttk.LabelFrame(self.upload,text ="Insert data below")
        lf.grid(column=0,row=2,**option2)
        label = ttk.Label(lf, text="Gender").grid(column=0,row=3,**option1)
        username_entry = ttk.Entry(lf,text="Gender", textvariable=gender).grid(column=1,row=3,**option1)
        label = ttk.Label(lf, text="feature").grid(column=2,row=3,**option1)
        password_entry = ttk.Entry(lf, textvariable=feature).grid(column=3,row=3,**option1)
        label = ttk.Label(lf, text="LocationX").grid(column=0,row=4,**option1)
        email_entry = ttk.Entry(lf, textvariable=locationX).grid(column=1,row=4,**option1)
        label = ttk.Label(lf, text="LocationY").grid(column=2,row=4,**option1)
        email_entry = ttk.Entry(lf, textvariable=locationY).grid(column=3,row=4,**option1)
        label = ttk.Label(lf, text="Note").grid(column=0,row=6,**option1)
        confirmpassword_entry = ttk.Entry(lf, textvariable=note).grid(column=1,row=6,**option1)
        self.upload_Btn = ttk.Button(lf, text="Upload",
                        command=lambda: self.upload_data()).grid(column=0,row=8,**option2,columnspan=4)
        cancel_Btn = ttk.Button(self.upload, text="Cancel",
                        command=lambda: self.close_upload()).grid(column=0,row=9,**option2,sticky=SE)
        print(self)
        self.upload.mainloop()
    
    def open_upload(self):
        if self.check ==False:
            self.check=True
            self.upload_window(self.user)

    def update(self):
            """Function to receive the new data and open popup message to confirm the action as well as close the current DES window
            """
            # Take new data into from spreadsheet 
            showinfo(
                title = "Update data",
                message = "The data has been updated, please close all DES"
            )   
    def upload_data(self):
        pass
    
    def close_DES(self,data):
        #des_check.discard(data)
        print("hi")
    def close_upload(self):
        self.check = False
        self.upload.destroy()
    
    def signout(self):
        """Sign out function which destroy self, DES and return to log in window

        """
        self.destroy()
        application.App()
des_check =set()
if __name__ == "__main__":
    new_menu = window()
    new_menu.mainloop()
    
