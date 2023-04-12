import tkinter as tk
from tkinter import ttk
#import ttkbootstrap as ttk # adds more styling options

# create window
game = tk.Tk()
game.title("Demo")
game.geometry("800x500") # widthxheight

def difficulty():
    # title
    title_label = ttk.Label(master = game, text = "Choose your Difficulty level", font = "Calibri 24 bold") # font = "font fontsize"
    title_label.pack()

    main_level_frame = ttk.Frame(master = game)
    main_level_frame.pack()

    # difficulty descriptions
    # easy
    level_frame = ttk.Frame(master = main_level_frame, background = 'blue')
    button1 = tk.Button(
        master = level_frame,
        text = "EASY",
        height = 3,
        width = 5,
        font=('Calibri', 15, 'bold')) # add command to go to hard lvl

    description = ttk.Label(
        master = level_frame, 
        text = "- Guess a 5 letter word\n- Unlimited amount of tries")


    button1.pack(side = "left")
    description.pack(side = "left")
    level_frame.pack()

    #default
    level_frame = ttk.Frame(master = main_level_frame, background = 'red')
    button = tk.Button(
        master = level_frame,
        text = "DEFAULT",
        height = 3,
        width = 5,
        font=('Calibri', 15, 'bold')) # add command to go to hard lvl

    description = ttk.Label(
        master = level_frame, 
        text = "- Guess a 5 letter word\n- Complete within 5 tries")

    button.pack(side = "left")
    description.pack(side = "left")
    level_frame.pack()

    # hard
    level_frame = ttk.Frame(master = main_level_frame, background = 'blue')
    button = tk.Button(
        master = level_frame,
        text = "HARD",
        height = 3,
        width = 5,
        font=('Calibri', 15, 'bold')) # add command to go to hard lvl

    description = ttk.Label(
        master = level_frame, 
        text = "- Guess a 7 (or more) letter word\n- Complete within 5 tries")


    button.pack(side = "left")
    description.pack(side = "left")
    level_frame.pack()

difficulty()



# run 
game.mainloop()

