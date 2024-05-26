from tkinter import *
import random
from PIL import Image, ImageTk

main = Tk()

Score = 0

#Dictionary that makes it easy to add options and images associated to a specific question
Flag_Quiz = {
    "Question 1": ["Australia","New Zealand","Greece","Sweden",0,"Australian_Flag.jpeg"],
    "Question 2": ["Italy","China","Spain","Egypt",2,"Spanish_Flag.jpeg"]
    #More questions will be added later, there are only 2 right now so that I can test the next question function later
}



#Called when the start button pressed, starts the quiz
def Start_Quiz():
    for i in main.winfo_children():
        i.pack_forget()
    
    Question_Generator()

#Checks if the button clicked is the correct answer
def Check_Answer(i):
    #
    if i == list(Flag_Quiz.items())[0][1][4]:
        print("Correct answer")

#Generates questions
def Question_Generator():
    #Creates 4 buttons
    for i in range(4):
        Button_Options = Button(main, text="test", command=lambda i=i:Check_Answer(i))
        Button_Options.pack(anchor=W)

Quiz_title = Label(main, text="Flag Quiz")
Start_Button = Button(main, text="Start Button", command=Start_Quiz)
Quiz_title.pack()
Start_Button.pack()
main.mainloop()