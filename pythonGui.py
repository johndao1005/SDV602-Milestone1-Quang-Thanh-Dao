import tkinter as tk # import python
import windowsLayouts as layout # storing all the layout for the application

# window = tk.Tk()
# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# label = tk.Label(
#     text="Hello, Tkinter", #available color blue, red ,yellow can use hexadecimal for color
#     fg="white",  # Set the text color to white
#     bg="black",  # Set the background color to black
#     width = 20 , # the size of window
#     height = 10
# )
# button = tk.Button(
#     text="Click me!",
#     width= 6,
#     height= 1,
#     bg="blue",
#     fg="yellow",
# )
# label.pack()
# button.pack()
# entry.pack()
# login = entry.get()
# location = entry.insert(0,'12.213123')


# txtbox = tk.Text()
# txtbox.pack()
# frame =tk.Frame()
# frame.pack()
# window.mainloop()

# ANCHOR working frame which is best to organise the the element within the window
window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

frame_a.pack()
frame_b.pack()

window.mainloop()

#window.destroy()
# def make_window(content,choice1,choice2):
#     layout =[[sg.Text(content)],[sg.Button(choice1),sg.Button(choice2)]]
#     return sg.Window('Light house', layout, finalize=True)

# window0,window1,window2= sg.Window("Light house",[[sg.Text("Welcome to my game")],[sg.Button("Start"),sg.Button("Exit")]],finalize=True),None,None

# def lightHouseGUI():
#     while True:
#         window, event, values = sg.read_all_windows()
#         if event == sg.WINDOW_CLOSED or event == 'Quit' or event == 'Exit'or event=="Restart":
#             window.close()
#             if window == window2:       # if closing win 2, mark as closed
#                 window2 = None
#             elif window == window0:     # if closing win 1, exit program
#                 break
#         if event == "Start" or event == "Restart":
#             window1= make_window("Welcome To the lighthouse,\n You just wake up to find yourself in a cold room with nothing\nbut darkness around, outside only the sound of the ocean and cold gale while you \nlying on the, cold dirty floor. Suddenly loud noise can be hear outside. Looking out the window,\nyou saw a dark shadow with claw climb up the light house.\nWhat do you want to do?",'Jump out the window','Try to escape')
#         elif event == "Jump out the window":
#             window1.close()
#             window2 = make_window("You jump out the window and try to grab the Monster to die with you. \nWhen both of you are falling, you remove the mask to see yourself with a happy smile. The monster whisper in your ear: \n'Wear the mask if you want something new'\nDo you want to wear the mask?","Wear the mask","Just die")
#         elif event == "Try to escape":
#             window1.close()
#             window2 = make_window("Looking at the door tightly locked door. What would you do?","Look for key","Ram the door")
#         elif event == "Ram the door":
#             window2.close()
#             window1 = make_window("You dislocate your shouder and try to look for key instead. but the monster catch up\nSo you die. Too bad.","Restart","Quit")
#         elif event == "Look for key":
#             window2.close()
#             window1 =make_window("Lucky the key is in your pocket somehow. You unlock the door and want to go down the stair but the stair is broken. What do you do?", \
#                     "Find a Rope","Jump down")
#         elif event == "Find a Rope":
#             window1.close() 
#             window2 = make_window("Running back you facing the monster. there is a sword nearby\nWould you take the sword and fight for your last chance?","Fight","Beg for Mercy")
#         elif event == "Fight":
#             window2.close()
#             window1 =make_window("Taking the sword and fight for your life. Surpisingly, you seem to know\nThe monster movement like yourself and you win after stabing it heart. Upon\ncoming closer and remove the mask, you saw your face smiling in relieve. \nLooking at the mask, look like it is pulling you over. What would you do?", "Wear the mask","Stab yourself")
#         elif event == "Beg for Mercy":
#             window2.close()
#             window1 =make_window("Too scared from looking at the monster. You begged for your life. Seem like u didnt watch much\nscary movie, why begging then you will die anyway num num. Dont need to say much, You die", \
#                     "Restart","Quit")
#         elif event =="Stab yourself":
#             window1.close()
#             window2 =make_window(".Waking up in your room feeling unreal but relieved. Suddenly, you Feel tired and want to go back to sleep.\nWould you sleep again?\n*Note: This is the closest thing of winning this game. Be proud", \
#                     "Restart","Quit")
#         elif event == "Jump down":
#             window1.close() 
#             window2 = make_window("you over jump and hurt your leg. The Monster catch up quickly and you die. lol ",\
#             "Restart","Quit")
#         elif event == "Just die":
#             window2.close()
#             window1 =make_window("You die, pretty sad, want to start again?", "Restart","Quit")
#         elif event == "Wear the mask":
#             window2.close()
#             window1=make_window("The Monster is inside you and you are the monster, You will keep hunting yourself till you die","Restart","Quit")
# if __name__== "__main__":
#     lightHouseGUI()
    
