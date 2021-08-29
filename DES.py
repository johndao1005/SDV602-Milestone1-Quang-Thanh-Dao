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

def window(windowname, datatype, next, prev,positionX ,positionY):
        windowname = Toplevel()
        windowname.title(setup.app_name)
        windowname.iconbitmap(setup.icon)
        option1 = setup.pad20
        option2 = setup.pad10
        label = Label(windowname, text=f"White shark {datatype} data").grid(column=0,row=0,**option1,columnspan=3)
        windowname.geometry(f"800x600+{positionX}+{positionY}")
        
        # ANCHOR data display
        frame = ttk.Frame(windowname)
        frame.grid(column=0,row=1,**option1,columnspan=2)
        img = ImageTk.PhotoImage(Image.open(f"./src/{datatype}.png"))
        panel = Label(frame, text="Hello",width = 50).grid(column=0,row=1,**option1)
        # Storing new data
        input = StringVar()
        chatLog = StringVar()
        # chat box creating and function
        frame1 = ttk.LabelFrame(windowname,text="Chat box",borderwidth=0)
        frame1.grid(column=2,row=1,**option1,)
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
        frame2.grid(column=2,row=4,**option1,sticky=NSEW)
        button = ttk.Button(frame2,
                        text="Next",
                        command=lambda: changeWindow(windowname,next)
                        ).grid(column=0,row=5,**option1)
        button = ttk.Button(frame2,
                        text="Previous",
                        command=lambda: changeWindow(windowname,prev)
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
            current.destroy()
            next()
        def close_DES():
            windowname.destroy()
        windowname.protocol("WM_DELETE_WINDOW",close_DES)
        windowname.mainloop()


if __name__ == "__main__":
    app = window("root","gender",2,3)
    
