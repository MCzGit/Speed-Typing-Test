# Importing the modules
from english_words import get_english_words_set
from tkinter import *
from tkinter import messagebox
from timeit import default_timer as timer  
import random

#Declare variables that will be used often.
BG = "#F6F1F1"
FONT = ("Trebuchet MS", 25, "bold")
FONTCOLOR = "#19A7CE"
FONTCOLOR2 = "#146C94"

#Create the window, adding size, title, and background color.
root = Tk()
root.geometry('1000x600')
root.title('Speed Typing Test')
root.config(bg="#F6F1F1")


#Declare variables that will be used to for functionality.
words = list(get_english_words_set(['web2']))
score = 0
missed = -1
time = 60

#Created the function timeLIMIT() that references the variables mentioned above.
def timeLIMIT():
    global time, score, missed

    #If time is greater than 0, subtract by 1 and display it on the timer label.
    if time > 0:
        time -= 1
        timer.configure(text=time)
        #The after function calls back the timeLIMIT function after a delay of 1000 milliseconds.
        timer.after(1000, timeLIMIT)
    
    #If time has reached 0, display the "Time's Up" label, and the label which displays the user's final results.
    else:
        startlabel.configure(text="Time's Up!", fg='red')
        final_result  = Label(root,text='', bg=BG, highlightbackground=BG, font=FONT,fg=FONTCOLOR2)
        final_result.place(x=300,y=260)
        final_result.configure(text=f'Hit = {score} | Miss = {missed} | Total Score = {score - missed}')
        

#Created the function typingTEST that takes event as an input argument.
def typingTEST(event):
    global score, missed
    
    #If time is equal to 60, launch the timeLIMIT function.
    if time == 60:
        timeLIMIT()

    #Change the startlabel to display Test Started
    startlabel.configure(text='Test Started!', fg=FONTCOLOR2)
    startlabel.place(x=400, y=50)
    #Change the runTEST label to display new instructions.
    runTEST.configure(text='Hit Enter After Typing The Word')
    runTEST.place(x=320, y=450)

    #Get the word typed in the userINPUT using the get() function.
    #Check if it is equal to the word displayed on the screen.
    if userINPUT.get() == nextWORD['text']:
        #If the userINPUT is equal to the word displayed, increase the user's score by 1 
        #Display the new score on the scoreboard label.
        score += 1
        scoreboard.configure(text=score)

    #If the userINPUT does not match the word displayed, increase the missed variable by 1.
    else:
        missed += 1
    
    
    #Reshuffle the words in the word list and display the first element.
    random.shuffle(words)
    nextWORD.configure(text=words[0])
    #Use the delete function from the zero to the end of the index on the userINPUT widget to clear the content.
    userINPUT.delete(0, END)

#Created the labels for startlabel, nextWORD, scoreLABEL, scoreboard, timerLABEL, timer, and runTEST using the Labels widget from Tkinter.
#Set the location of the labels by using the place() method and setting the X,Y coordinates.
startlabel = Label(root, text="Speed Typing Test", bg=BG, highlightbackground=BG, font=("Trebuchet MS", 30, "bold"), fg=FONTCOLOR)
startlabel.place(x=375, y=50)

nextWORD = Label(root, text=" ", font=("Trebuchet MS", 45), bg=BG, highlightbackground=BG, fg=FONTCOLOR)
nextWORD.place(x=400, y=240)

scoreLABEL = Label(root, text="Your Score:", bg=BG, highlightbackground=BG, font=FONT, fg=FONTCOLOR)
scoreLABEL.place(x=110,y=100)

scoreboard = Label(root, text=score, bg=BG, highlightbackground=BG, font=FONT, fg='green')
scoreboard.place(x=160, y=150)

timerLABEL = Label(root, text="Time Left:", bg=BG, highlightbackground=BG, font=FONT, fg=FONTCOLOR)
timerLABEL.place(x=700, y=100)

timer = Label(root, text=time, bg=BG, highlightbackground=BG, font=FONT,fg='red')
timer.place(x=750, y=180)

runTEST = Label(root, text="Press Enter to Begin the Test", bg=BG, highlightbackground=BG, font=FONT, fg=FONTCOLOR2)
runTEST.place(x=345, y=450)

#Created the Entry widget that will accept the input provided by the user.
#Set the location of the Entry widget by using the place() method and setting the X,Y coordinates.
userINPUT = Entry(root, font=FONT, bd=10, justify='center')
userINPUT.place(x=350, y=330)
#Used the focus_set() function to activate the Entry box for input.
userINPUT.focus_set()

#Used the bind function so the "Enter" key will be activated while the app is running.
#The bind function accepts <Return> as a string and typingTEST() function as parameters.
root.bind('<Return>', typingTEST)
#The mainloop function runs the application until the window is closed.
root.mainloop()