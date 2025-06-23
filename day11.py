# Week 2: Data Structures & Control Flow
# --------------------------------------
# Day 11 – Rock, Paper, Scissors: Game using loops and random.

import random

choice = ["rock", "paper", "scissors"]
print("Rock, Paper, Scissors Choose one of them")
while True:
    user = input("Enter your choice: ").lower()

    if user == 'exit':
        break

    if user not in choice:
        print("Invalid value.Please choose Rock, Paper, Scissors Choose one of them")
        continue
    
    computer_choice = random.choice(choice)

    if user == computer_choice:
        print("it's a tie\n")
    elif( (user == 'rock' and computer_choice == 'scissor') or 
          (user == 'paper' and computer_choice == 'rock') or
          (user == 'scissors' and computer_choice == 'paper')):
          print("you win")
    
    else:
        print("computer win")
         