import tkinter
from tkinter import *

#Global Variables
submission_space = 0


def store_submission():
    submission_space = submit.get()
    print(submission_space)

Guessing_Game_Window = Tk()
Guessing_Game_Window.geometry('500x500')
Guessing_Game_Window.title("Dylan's Guessing Game")
Guessing_Game_Window.config(background="Forest Green")
icon = PhotoImage(file='test_icon.png')
Guessing_Game_Window.iconphoto(True,icon)
#Submission Space
submit = tkinter.Entry(Guessing_Game_Window)
submit.pack()
#Submission Button
submit_button = Button(Guessing_Game_Window, text="Submit")
submit_button.config(command=store_submission)
submit_button.pack()



Guessing_Game_Window.mainloop()


