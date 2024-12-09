import os.path
import random
import tkinter as tk
from tkinter import *





class Guessing_Game_Variables:
    def __init__(self,total_guesses,guesses_made,computer_number):
        self.total_guesses = total_guesses
        self.guesses_made = guesses_made
        self.computer_number = computer_number

    def __str__(self):
        return f'Total Guesses -----{self.total_guesses} Guesses Made -----{self.guesses_made} Computer Number-----{self.computer_number}'

Game_Variables = Guessing_Game_Variables(1,0,42)
number_submit = Entry

print(Game_Variables)

#Main Game Window Basics
Guessing_Game_Window = tk.Tk()#creates the main game window instance
Guessing_Game_Window.geometry('1000x145')#sets the main game window size
Guessing_Game_Window.title("Dylan's Guessing Game")#Gives the main game window it's title, which shows up in the upper-border of the window
Guessing_Game_Window.config(background='#19e39c')#Determines the window's background color

icon_path = "test_icon.png"
if os.path.exists(icon_path):

    icon = PhotoImage(file='test_icon.png')#converts png file into PhotoImage
    Guessing_Game_Window.iconphoto(True,icon)#sets the window border icon to the chosen PhotoImage
else:
    print(f'Error -- File to icon not found.')


#Main Game Window Functions
def set_up_window():
    #range variables
    range_high = 0
    range_low = 0

    game_start_b.destroy()
    game_end_b.config(font=("Courier",10))

    # Label for displaying messages
    message = Label(Guessing_Game_Window, width=100)
    message.config(font="Courier", text="Whats the biggest number we should use?", fg="Red")
    message.pack()

    #Entry place for numbers
    number_entry = Entry(Guessing_Game_Window, width=20)
    number_entry.pack()





    def store_high_number():

        nonlocal range_high
        range_high = int(number_entry.get())
        message.config(text=f"Great! The highest number we'll use is {range_high}! Now we need the lowest number.")
        submission_button.config(command=store_low_number)
        number_entry.delete(0,END)



    def store_low_number():

        nonlocal range_low
        range_low = int(number_entry.get())
        message.config(text=f"Fantastic! The number is somewhere between {range_low} and {range_high}!")
        number_entry.delete(0,END)
        Game_Variables.computer_number = random.randrange(range_low,range_high)
        Game_Variables.total_guesses = ((range_high-range_low)//10 + 1)
        print(Game_Variables)



        def guess():
            def start_new_game():
                Game_Variables.guesses_made = 0
                Game_Variables.total_guesses = 1
                message.config(font="Courier", text="Whats the biggest number we should use?", fg="Red")
                submission_button.config(text="Submit Number",command=store_high_number)
                print(Game_Variables)



            player_guess = int(number_entry.get())
            computer_number = Game_Variables.computer_number

            Game_Variables.guesses_made += 1
            Game_Variables.total_guesses -= 1

            number_entry.delete(0,END)

            if player_guess == computer_number and Game_Variables.guesses_made == 1:
                message.config(text="Oh Shit! Can you read my mind?!?!")
                submission_button.config(text="Start a new game.", command=start_new_game)


            elif player_guess == computer_number:
                message.config(text=f"Congrats! You got the number right in just {Game_Variables.guesses_made} guesses!")
                submission_button.config(text="Start a new game.",command=start_new_game)

            elif player_guess < computer_number:
                message.config(text=f"Sorry, that guess was too low! {Game_Variables.total_guesses} guesses left!")

            elif player_guess > computer_number:
                message.config(text=f"Sorry, that guess was too high! {Game_Variables.total_guesses} guesses left!")

            elif Game_Variables.total_guesses < 1:
                message.config(text=f"Sorry! You've run out of guesses! The number we picked was {Game_Variables.computer_number}! We hope you try again!")

            print(Game_Variables)

        submission_button.config(text="Take a guess!", command=guess)




    #Button for submitting input
    submission_button = Button(Guessing_Game_Window, width=20, text="Submit Number")
    submission_button.config(command=store_high_number)
    submission_button.pack()







#Game Window Buttons

    #Game Start Button
game_start_b = Button(Guessing_Game_Window,text="Start a number guessing game.",width=150)#instances the start game button, sets the text and button width
game_start_b.config(font=('Courier',30),fg="#000000",bg="#f2882c",activebackground="#753e0e",activeforeground="Purple")#sets various aesthetic components, including font, font color, background color, and active background color
game_start_b.config(command=set_up_window)#sets new game function
game_start_b.pack()

    #Exit Game Button
game_end_b = Button(Guessing_Game_Window,text="I'm finished playing!",width=150)#instantiates the exit button
game_end_b.config(font=("Courier",30),fg="#000000",bg="#f2882c",activebackground="#753e0e")#sets button aesthetics
game_end_b.config(command=Guessing_Game_Window.destroy)#sets end game button function
game_end_b.pack()



Guessing_Game_Window.mainloop()
