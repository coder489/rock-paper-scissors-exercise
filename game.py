import random

#-------------------
#Welcome to my Rock-Paper-Scissors game...
#-------------------
#Please choose either 'rock', 'paper', or 'scissors': rock
#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!


#Print the header

print("-------------------")
print("Welcome to my Rock-Paper-Scissors game...")
print("-------------------")

#Receive the input

options = ["rock","paper","scissors"]
user_choice=input("Please choose either 'rock', 'paper' , or 'scissors' : ")

if user_choice in options:
    print("You chose: " + user_choice)
else:
    print("OOPS - INVALID SELECTION")
    exit()

computer_choice = random.choice(options)
print("The computer chose: " + computer_choice)

#Determine the winner

winner = ""

if user_choice == "rock" and computer_choice == "scissors":
    winner = "user"
elif user_choice == "rock" and computer_choice == "rock":
    winner = "both"
elif user_choice == "scissors" and computer_choice == "paper":
    winner = "user"
elif user_choice == "scissors" and computer_choice == "scissors":
    winner = "both"
elif user_choice == "paper" and computer_choice == "rock":
    winner = "user"
elif user_choice == "paper" and computer_choice == "paper":
    winner = "both"
else:
    winner = "computer"

#Print the results

print("-------------------")

if winner == "user":
    print("You Won!")
if winner == "computer":
    print("Oh, the computer won. It's ok.")
if winner == "both":
    print("You tied")

print("-------------------")
print("Thanks for playing. Please play again!")