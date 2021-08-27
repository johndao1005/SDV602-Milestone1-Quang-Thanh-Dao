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
import menu


def window(windowname,datatype,nextDES,previousDES):
            """Creating database  Screen Window     
            Args:
                datatype (string ): name of the data is present in for the current DES
            """
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
            def changeWindow(current,next):
                current.destroy()
                next()
            windowname = Toplevel()
            windowname.title("White shark tracking")
            windowname.iconbitmap("./src/wireshark.ico")
            label = Label(windowname, text= f"White shark {datatype} data")
            windowname.geometry("800x600")
            img = ImageTk.PhotoImage(Image.open(f"./data/{datatype}.png"))
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
                            command=lambda:changeWindow(windowname,nextDES)
                            ).pack(pady=5)
            button = Button(windowname,
                            text="Previous",
                            command=lambda:changeWindow(windowname,previousDES)
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
                            text="upload Data",
                            command=lambda:uploadData()
                            ).pack(pady=5)
            button = Button(windowname,
                            text="Update data",
                            command=lambda:update()
                            ).pack(pady=5)
            windowname.mainloop()
            