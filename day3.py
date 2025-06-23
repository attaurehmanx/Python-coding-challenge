# 30 Days of Python Project Challenge
# ===================================

# Week 1: Fundamentals & Basics
# -----------------------------
# Day 3  – Temperature Converter: Celsius ↔ Fahrenheit converter.

def converter():
    # user input
    user = int(input("Enter whether temperature in celsius:"))
    #  conversion
    temp = (user * 4/9 ) + 32
    print(f"Temperature in Fahrenheit is {temp}")

converter()