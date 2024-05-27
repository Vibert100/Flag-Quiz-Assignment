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
    global Score
    if i == list(Flag_Quiz.items())[0][1][4]:
        Score = Score + 1
        print("Correct answer")
        Next_Question()
    else:
        print("Incorrect answer")
        Next_Question()
    #Removes first question from quiz, prevent repetition
    Flag_Quiz.pop(0)



def Next_Question():
    print("filler")

#Generates questions
def Question_Generator():
    #Gets first key from the dictionary
    Question = list(Flag_Quiz.keys())[0]

    #Creates 4 buttons
    for i in range(4):
        Buttons = Flag_Quiz[Question][i]
        Button_Options = Button(main, text=Buttons, command=lambda i=i:Check_Answer(i))
        Button_Options.pack(anchor=W)

Quiz_title = Label(main, text="Flag Quiz")
Start_Button = Button(main, text="Start Button", command=Start_Quiz)
Quiz_title.pack()
Start_Button.pack()
main.mainloop()