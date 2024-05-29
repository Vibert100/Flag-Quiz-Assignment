from tkinter import *
import random
from PIL import Image, ImageTk

main = Tk()

Score = 0

#Dictionary that makes it easy to add options and images associated to a specific question
Flag_Quiz = {
    "Question 1": ["Australia","New Zealand","Greece","Sweden",0,"Australian_Flag.png"],
    "Question 2": ["Italy","China","Spain","Egypt",2,"Australian_Flag.png"],
    "Question 3": ["France","Vietnam","Turkey","Pakistan",2,"Australian_Flag.png"]
    #More questions will be added later, there are only 2 right now so that I can test the next question function later
}


Quiz = list(Flag_Quiz.items())
#Randomises the order the questions appear in
random.shuffle(Quiz)
#Called when the start button pressed, starts the quiz
def Start_Quiz():
    #Removes all widgets on the screen
    for i in main.winfo_children():
        i.pack_forget()
    
    Flags.pack()

    #Packs all options
    for buttons in Button_Options:
        buttons.pack(anchor=W)

    Question_Generator()


#Checks if the button clicked is the correct answer
def Check_Answer(i):
    global Score
    if i == Quiz[0][1][4]:
        Score = Score + 1
        print("Correct answer")
    else:
        print("Incorrect answer")
    #Removes first question from quiz, prevent repetition
    Quiz.pop(0)
    Question_Generator()

def Question_Generator():
    #Checks if there are questions remaining
    if len(Quiz) > 0:
        Question, Choices = Quiz[0]
        Quiz_Question.set(Question)
        Answer = Choices[Choices[4]]
        Choices = Choices[0:3]
        Choices.append(Choices.index(Answer))
        Question, Choices = Quiz[0]
        #Updates the names of the buttons
        for i, Choice in enumerate(Choices[0:4]):
            Button_Options[i]["text"] = Choice
        Flag_images = Flag_Quiz[Question][5]
        Flag = Image.open(Flag_images)
        Flag = Flag.resize((300,200))
        Tk_Flag = ImageTk.PhotoImage(Flag)
        Flags.config(image=Tk_Flag)
        Flags.image = Tk_Flag
    else:
        for i in main.winfo_children():
            i.pack_forget()
        Play_Again_Button.pack()

def Play_Again():
    global Quiz
    Play_Again_Button.pack_forget()
    Quiz = list(Flag_Quiz.items())
    random.shuffle(Quiz)
    Start_Quiz()



#Allows the buttons to be created later
Flags = Label(main)
Button_Options = [Button(main, command=lambda i=i: Check_Answer(i)) for i in range(4)]
Play_Again_Button = Button(main, text="Play again", command=Play_Again)

Quiz_Question = StringVar()


Quiz_title = Label(main, text="Flag Quiz")
Start_Button = Button(main, text="Start Button", command=Start_Quiz)
Quiz_title.pack()
Start_Button.pack()
main.mainloop()