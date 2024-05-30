from tkinter import *
import random
from PIL import Image, ImageTk

main = Tk()
main.title("Flag Quiz")
main.configure(bg="light blue")
main.geometry("300x450")
Score = 0
Question_Number = 0

#Dictionary that makes it easy to add options and images associated to a specific question
Flag_Quiz = {
    "Question 1": ["Australia","New Zealand","Greece","Sweden",0,"Flag_images/Australian_Flag.png"],
    "Question 2": ["Italy","China","Spain","Egypt",2,"Flag_images/Spanish_Flag.png"],
    "Question 3": ["France","Vietnam","Russia","Pakistan",2,"Flag_images/Russian_Flag.png"],
    "Question 4": ["Egypt","Germany","Iran","Russia",0,"Flag_images/Egyptian_Flag.png"],
    "Question 5": ["India","Vietnam","South korea","China",2,"Flag_images/South_Korean_Flag.png"],
    "Question 6": ["Thailand","Bangladesh","Ukraine","Canada",3,"Flag_images/Canadian_Flag.png"],
    "Question 7": ["Malaysia","Bangladesh","Nigeria","Columbia",1,"Flag_images/Bangladeshi_Flag.png"],
    "Question 8": ["Ireland","Italy","Greece","Indonesia",1,"Flag_images/Italian_Flag.png"],
    "Question 9": ["China","Vietnam","Poland","Columbia",1,"Flag_images/Vietnamese_Flag.png"],
    "Question 10": ["India","Turkey","Argentina","Iraq",0,"Flag_images/Indian_Flag.png"],
    "Question 11": ["United Kingdom","Austria","Greece","Morocco",2,"Flag_images/Greek_Flag.png"],
    "Question 12": ["Saudi Arabia","Qatar","Syria","Iran",0,"Flag_images/Saudi_Arabian_Flag.png"],
    "Question 13": ["Vietnam","China","Japan","Phillipines",1,"Flag_images/Chinese_Flag.png"],
    "Question 14": ["Nigeria","Chile","Mexico","South Africa",3,"Flag_images/South_African_Flag.png"],
    "Question 15": ["Brazil","United States","Mexico","Argentina",2,"Flag_images/Mexican_Flag.png"],
    "Question 16": ["Nigeria","Switzerland","Portugal","Jamaica",0,"Flag_images/Nigerian_Flag.png"],
    "Question 17": ["Norway","Finland","Denmark","Sweden",0,"Flag_images/Norwegian_Flag.png"],
    "Question 18": ["Norway","Finland","Denmark","Sweden",3,"Flag_images/Swedish_Flag.png"],
    "Question 19": ["Netherlands","Austria","Australia","Poland",0,"Flag_images/Dutch_Flag.png"],
    "Question 20": ["Ireland","Russia","India","Malaysia",0,"Flag_images/Dutch_Flag.png"],



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
    
    #Packs after the start button is pressed
    
    Score_Label.pack()
    Flags.pack()

    for buttons in Button_Options:
        buttons.pack(pady=3)

    Question_Number_Label.pack()

    Question_Generator()


#Checks if the button clicked is the correct answer
def Check_Answer(i):
    global Score
    global Question_Number
    if i == Quiz[0][1][4]:
        Score = Score + 1
        print("Correct answer")
        Correct_Label.pack()
    else:
        print("Incorrect answer")
        Incorrect_Label.pack()
        
    Question_Number = Question_Number + 1
    Score_Label.config(text="Score:" + str(Score))
    Question_Number_Label.config(text="Question:" + str(Question_Number) + "/20")
    #Removes first question from quiz, prevent repetition
    Quiz.pop(0)
    #After a 300 milisecond delay calls Question_Generator
    main.after(300, Question_Generator)

def Question_Generator():
    Correct_Label.pack_forget()
    Incorrect_Label.pack_forget()
    #Checks if there are questions remaining
    if len(Quiz) > 0:
        Question, Choices = Quiz[0]
        Quiz_Question.set(Question)
        Answer = Choices[Choices[4]]
        Choices = Choices[0:4]
        #Randomises the order of the choices
        random.shuffle(Choices)
        Quiz[0] = Question, Choices
        Choices.append(Choices.index(Answer))
        #Updates the names of the buttons
        for i, Choice in enumerate(Choices[0:4]):
            Button_Options[i]["text"] = Choice

        #Creates the flag associated with the question
        Flag_images = Flag_Quiz[Question][5]
        Flag = Image.open(Flag_images)
        Flag = Flag.resize((300,200))
        Tk_Flag = ImageTk.PhotoImage(Flag)
        Flags.config(image=Tk_Flag)
        Flags.image = Tk_Flag
    else:
        #Occurs when all questions are finished
        #Hides all widgets
        for i in main.winfo_children():
            i.pack_forget()
        #Updates the final score label
        Final_Score.config(text="Your score is " + str(Score) + "/20")
        Quiz_title.pack()
        Quiz_Image.pack()
        Final_Score.pack(pady=(0,50))
        Play_Again_Button.pack()


def Play_Again():
    #Allows the values to be global
    global Quiz
    global Score
    global Question_Number

    Score = 0
    Question_Number = 0
    #Resets the Score once play again is pressed
    Score_Label.config(text="Score:" + str(Score))

    Question_Number_Label.config(text="Question:" + str(Question_Number) + "/20")
    Play_Again_Button.pack_forget()
    Quiz = list(Flag_Quiz.items())
    random.shuffle(Quiz)
    Start_Quiz()

#Allows the buttons to be created later
Flags = Label(main)

Quiz_title = Label(main, text="Flag Quiz",
                   width="10", bg="light blue",
                   font=("arial", 24))
Quiz_title.pack()

UN_Image = Image.open("Flag_Images/United_Nation_Flag.png")
UN_Image = UN_Image.resize((300,200))
Tk_UN_Image = ImageTk.PhotoImage(UN_Image)

Quiz_Image = Label(main, image=Tk_UN_Image)
Quiz_Image.pack(pady=(0,50))

Start_Button = Button(main, text="Start",width="15",
                        font=("arial", 16), bg="#0047AB",
                        bd=0, fg="white", command=Start_Quiz)

Start_Button.pack()

Correct_Label = Label(main, text="Correct!",
                     width="10", bg="light blue",fg="Green",font=("arial", 14))

Incorrect_Label = Label(main, text="Incorrect!",
                     width="10", bg="light blue",fg="Red",font=("arial", 14))

Score_Label = Label(main, text="Score:"+ str(Score),
                     width="10", bg="light blue",font=("arial", 12))
                   
Button_Options = [Button(main, width="15",
                        font=("arial", 14), bg="#0047AB",
                        bd=0, fg="white",
                        command=lambda i=i: Check_Answer(i)) for i in range(4)]

Question_Number_Label = Label(main, text="Question:" + str(Question_Number) + "/20",
                     width="14", bg="light blue",font=("arial", 12))

Play_Again_Button = Button(main, text="Play again",
                        width="15",font=("arial", 14),
                        bg="#0047AB",bd=0, fg="white",
                        command=Play_Again)

Final_Score = Label(main, text="Your score is "+str(Score)+"/20",
                    bg="light blue",font=("arial", 12))

Quiz_Question = StringVar()

main.mainloop()