from tkinter import *
from PIL import Image, ImageTk
from random import randint

### DISCLAIMER : THIS PROGRAM WAS FOLLOWING BY YOUTUBE.
### I'M JUST LEARN AND FOLLOW THE PROGRAM (ONE  BY ONE) AND IT'S BECOME LIKE THIS

#main window
root = Tk ()
root.title("SCISSORS - ROCK - PAPER GAME")
root.configure(background="#333333")

#picture
scissors_img = ImageTk.PhotoImage(Image.open("scissors-com.png"))
rock_img = ImageTk.PhotoImage(Image.open("rock-com.png"))
paper_img = ImageTk.PhotoImage(Image.open("paper-com.png"))
scissors_img_comp = ImageTk.PhotoImage(Image.open("scissors-user.png"))
rock_img_comp = ImageTk.PhotoImage(Image.open("rock-user.png"))
paper_img_comp = ImageTk.PhotoImage(Image.open("paper-user.png"))

#insert picture
user_label = Label(root,image=scissors_img,bg="#333333")
comp_label = Label(root,image=scissors_img_comp,bg="#333333")
comp_label.grid(row=1,column=0)
user_label.grid(row=1,column=4)

#scores
playerScore = Label(root,text=0,font=100,bg="#333333",fg="white")
computerScore = Label(root,text=0,font=100,bg="#333333",fg="white")
computerScore.grid(row=1, column=1)
playerScore.grid(row=1, column=3)

#indocators
user_indicator = Label(root,font=50,text="USER",bg="#333333",fg="white")
comp_indicator = Label(root,font=50,text="COMPUTER",bg="#333333",fg="white")
user_indicator.grid(row=0,column=3)
comp_indicator.grid(row=0,column=1)

#messages
msg = Label(root,font=50,bg="#333333",fg="white")
msg.grid(row=3,column=2)

#update messages
def updateMessage(x):
    msg['text'] = x

#update user score
def updateUserScore():
    score = int(computerScore["text"])
    score += 1
    computerScore["text"] = str(score)

#update computer score
def updateCompScore():
    score = int(playerScore["text"])
    score += 1
    playerScore["text"] = str(score)

#check winner
def chechWin(player,computer):
    if player == computer:
        updateMessage("DRAW")
    elif player == "scissors":
        if computer == "rock":
            updateMessage("SORRY YOU LOST")
            updateUserScore()
        else:
            updateMessage("YEAY YOU WIN")
            updateCompScore()
    elif player == "rock":
        if computer == "paper":
            updateMessage("SORRY YOU LOST")
            updateUserScore()
        else:
            updateMessage("YEAY YOU WIN")
            updateCompScore()
    elif player == "paper":
        if computer == "scissors":
            updateMessage("SORRY YOU LOST")
            updateUserScore()
        else:
            updateMessage("YEAY YOU WIN")
            updateCompScore()
    else:
        pass

#update choices
choices = ["scissors", "rock", "paper"]
def updateChoice(x):

#for computer
    compChoice = choices[randint(0,2)]
    if compChoice == "scissors":
        comp_label.configure(image=scissors_img_comp)
    elif compChoice == "rock":
        comp_label.configure(image=rock_img_comp)
    else:
        comp_label.configure(image=paper_img_comp)

#for user
    if x == "scissors":
        user_label.configure(image=scissors_img)
    elif x == "rock":
        user_label.configure(image=rock_img)
    else:
        user_label.configure(image=paper_img)

    chechWin(x,compChoice)

#buttons
scissors = Button(root,width=20,height=2,text="SCISSORS",bg="#FF5733",fg="white",command=lambda:updateChoice("scissors")).grid(row=2, column=1)
rock = Button(root,width=20,height=2,text="ROCK",bg="#3FFF33",fg="white",command=lambda:updateChoice("rock")).grid(row=2, column=2)
paper = Button(root,width=20,height=2,text="PAPER",bg="#3377FF",fg="white",command=lambda:updateChoice("paper")).grid(row=2, column=3)

root.mainloop ()