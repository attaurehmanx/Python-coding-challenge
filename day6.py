# 30 Days of Python Project Challenge
# ===================================

# Week 1: Fundamentals & Basics
# -----------------------------
# Day 6  – Tip Calculator: Calculate bill tips and splits.

def tip_Calculator():
    # user input 
    amount = int(input("Enter the amount:"))
    tip_percen = int(input("Enter the percentage of tip:"))
    number_of_people = int(input("How many are you to splitting bill amount:"))
    # getting the number of tip 
    tip = (tip_percen / 100) * amount
    # total bill with tip 
    total_bill = tip + amount
    # dividing the money for individual person 
    splitting_bill = total_bill // number_of_people

    print(f"Tip is {tip}, Total bill with tip is {total_bill} and one person can pay {splitting_bill} money.")

tip_Calculator()