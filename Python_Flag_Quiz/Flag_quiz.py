from tkinter import *
import random
from PIL import Image, ImageTk

main = Tk()

Score = 0

#Dictionary that makes it easy to add options and images associated to a specific question
Flag_Quiz_Options = {
    "Question 1": ["Australian_Flag.jpeg","Australia","New Zealand","Greece","Sweden"],
    "Question 2": ["Spanish_Flag.jpeg","Italy","China","Spain","Egypt"]
    #More questions will be added later, there are only 2 right now so that I can test the next question function later
}


def Start_Quiz():
    for i in main.winfo_children():
        i.pack_forget()


Quiz_title = Label(main, text="Flag Quiz")
Start_Button = Button(main, text="Start Button", command=Start_Quiz)
Quiz_title.pack()
Start_Button.pack()
main.mainloop()