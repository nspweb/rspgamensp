from operator import truediv
import random

print ("WELLCOME TO SCISSORS, ROCK, PAPER GAME")
print ("======================================")
print ("please choose one of them :")
print ("1. scissors")
print ("2. rock")
print ("3. paper")
print ("===========================\n")

while truediv :
    y = int(input("enter ur choice = "))
    com = random.choice (["scissors", "rock", "paper"])
    if y  == 1:
      print ("ur choice is scissors")
      print ("computer choice is",com)
      if com == "scissors":
        print ("~~ draw ~~\n")
      if com == "rock":
         print ("TT you lose TT\n")
      if com == "paper":
         print ("^^ you win ^^\n")

    if y == 2:
      print ("ur choice is rock")
      print ("computer choice is",com)
      if com == "scissors":
        print ("^^ you win ^^\n")
      if com == "rock":
         print ("~~ draw ~~\n")
      if com == "paper":
         print ("TT you lose TT\n")

    if y == 3:
      print ("ur choice is paper")
      print ("computer choice is",com)
      if com == "scissors":
        print ("TT you lose TT\n")
      if com == "rock":
         print ("^^ you win ^^\n")
      if com == "paper":
         print ("~~ draw ~~\n")

    if y > 3:
       print ("sorry, your choice is not in the list\n")