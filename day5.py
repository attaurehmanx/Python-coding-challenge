# 30 Days of Python Project Challenge
# ===================================

# Week 1: Fundamentals & Basics
# -----------------------------
# Day 5  – Guess the Number Game: Random number + user attempts.
import random 
print("Guess the Number Game")

def number_guessing():
    attempt = 0
    num = random.randint(1, 99)

    try:
        while True:
            user_guess = int(input("Guess the number:"))
            attempt += 1
            if user_guess < num:
                print("your guess is low")
            elif user_guess> num:
                print("your guess is high")
            else:
                print("you predict the right number. congratulation!")
                break
    except ValueError:
        print("Invalid input. Input must be number")
    
number_guessing()