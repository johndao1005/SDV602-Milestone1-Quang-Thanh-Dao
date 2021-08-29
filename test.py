# # import tkinter as tk
# # import tkinter.scrolledtext as tkst
# # from tkinter import ttk
# # import logging
# # import time

# # def popupmsg(msg):
# #     popup = tk.Toplevel()
# #     popup.wm_title("!")
# #     label = ttk.Label(popup, text=msg)
# #     label.pack(side="top", fill="x", pady=10)
# #     b1 = ttk.Button(popup, text="Okay", command=popup.destroy)
# #     b1.pack()
# #     popup.mainloop()

# # def test1():
# #     root.logger.error("Test")

# # def toggle(self):
# #     t_btn = self.t_btn
# #     if t_btn.config('text')[-1] == 'Start':
# #         t_btn.config(text='Stop')

# #         def startloop():
# #             if root.flag:
# #                 now = time.strftime("%c")
# #                 root.logger.error(now)
# #                 root.after(30000, startloop)
# #             else:
# #                 root.flag = True
# #                 return
# #         startloop()
# #     else:
# #         t_btn.config(text='Start')
# #         root.logger.error("Loop stopped")
# #         root.flag = False


# # class TextHandler(logging.Handler):

# #     def __init__(self, text):
# #         # run the regular Handler __init__
# #         logging.Handler.__init__(self)
# #         # Store a reference to the Text it will log to
# #         self.text = text

# #     def emit(self, record):
# #         msg = self.format(record)

# #         def append():
# #             self.text.configure(state='normal')
# #             self.text.insert(tk.END, msg + '\n')
# #             self.text.configure(state='disabled')
# #             # Autoscroll to the bottom
# #             self.text.yview(tk.END)

# #         # This is necessary because we can't modify the Text from other threads
# #         self.text.after(0, append)

# #     def create(self):
# #         # Create textLogger
# #         topframe = tk.Frame(root)
# #         topframe.pack(side=tk.TOP)

# #         st = tkst.ScrolledText(topframe, bg="#00A09E", fg="white", state='disabled')
# #         st.configure(font='TkFixedFont')

# #         st.pack()

# #         self.text_handler = TextHandler(st)

# #         # Add the handler to logger
# #         root.logger = logging.getLogger()
# #         root.logger.addHandler(self.text_handler)

# #     def stop(self):
# #         root.flag = False

# #     def start(self):
# #         if root.flag:
# #             root.logger.error("error")
# #             root.after(1000, self.start)
# #         else:
# #             root.logger.error("Loop stopped")
# #             root.flag = True
# #             return

# #     def loop(self):
# #         self.start()

# # class HomePage(tk.Frame):

# #     def __init__(self, parent):
# #         tk.Frame.__init__(self, parent)

# #         container = tk.Frame(self)
# #         container.pack(side="top", fill="both", expand=True)
# #         container.grid_rowconfigure(0, weight=1)
# #         container.grid_columnconfigure(0, weight=1)

# #         self.menubar = tk.Menu(container)
# #         self.check = False ### new

# #         # Create taskbar/menu
# #         file = tk.Menu(self.menubar)
# #         file.add_command(label="Run", command=lambda: test1())
# #         file.add_command(label="Stop", command=lambda: test1())
# #         file.add_separator()
# #         file.add_command(label="Settings", command=self.call_settings) #### new, changed command to run the function
# #         file.add_separator()
# #         file.add_command(label="Quit", command=quit)
# #         self.menubar.add_cascade(label="File", menu=file)

# #         self.master.config(menu=self.menubar)

# #         #logger and main loop
# #         th = TextHandler("none")
# #         th.create()
# #         root.flag = True
# #         root.logger.error("Welcome to ShiptScraper!")

# #         bottomframe = tk.Frame(self)
# #         bottomframe.pack(side=tk.BOTTOM)

# #         topframe = tk.Frame(self)
# #         topframe.pack(side=tk.TOP)

# #         self.t_btn = tk.Button(text="Start", highlightbackground="#56B426", command=lambda: toggle(self))
# #         self.t_btn.pack(pady=5)
# #         self.exitButton = tk.Button(text="Exit", highlightbackground="#56B426", command=quit)
# #         self.exitButton.pack()
# #         root.setting = False

# #     ########## changed
# #     def call_settings(self):
# #         if self.check == False:
# #             self.settings_window()
# #     ##########

# #     def settings_window(self):
# #         self.check = True
# #         self.settingswin = tk.Toplevel()
# #         self.settingswin.wm_title("Settings") 
# #         self.settingswin.protocol('WM_DELETE_WINDOW', self.close_Toplevel) ##### new
# #         exitButton = tk.Button(self.settingswin, text="Exit", highlightbackground="#56B426", command=self.close_Toplevel)
# #         exitButton.pack()

# #     def close_Toplevel(self):
# #         # New, this runs when the Toplevel window closes, either by button or else
# #         self.check = False
# #         self.settingswin.destroy()

# # class Help(tk.Toplevel):

# #     def __init__(self, parent):
# #         tk.Toplevel.__init__(self, parent)
# #         self.wm_title("Help")
# #         exitButton = tk.Button(text="Exit", highlightbackground="#56B426", command=quit)
# #         exitButton.pack()

# # if __name__ == "__main__":
# #     root = tk.Tk()
# #     root.configure(background="#56B426")
# #     root.wm_title("ShiptScraper")
# #     app = HomePage(root)
# #     app.mainloop()
    
# import tkinter as tk
# from tkinter import ttk


# # root window
# root = tk.Tk()
# root.geometry('300x200')
# root.resizable(False, False)
# root.title('LabelFrame Demo')

# # label frame
# lf = ttk.LabelFrame(
#     root,
#     text='Alignment')

# lf.grid(column=0, row=0, padx=20, pady=20)

# alignment = tk.StringVar()

# # left radio button
# left_radio = ttk.Radiobutton(
#     lf,
#     text='Left',
#     value='left',
#     variable=alignment
# ).grid(column=0, row=0, ipadx=10, ipady=10)

# # center radio button
# center_radio = ttk.Radiobutton(
#     lf,
#     text='Center',
#     value='center',
#     variable=alignment
# ).grid(column=1, row=0, ipadx=10, ipady=10)

# # right alignment radiobutton
# right_radio = ttk.Radiobutton(
#     lf,
#     text='Right',
#     value='right',
#     variable=alignment
# ).grid(column=2, row=0, ipadx=10, ipady=10)

# root.mainloop()
import test2
test2.window.checkUser(test2.window,"nice")
print(test2.window().user)

