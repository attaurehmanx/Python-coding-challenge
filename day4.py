# 30 Days of Python Project Challenge
# ===================================

# Week 1: Fundamentals & Basics
# -----------------------------
# Day 4  – Simple Calculator: Functions for +, −, ×, ÷ operations.

# function for operation
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def divi(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error, Zero can not be divisible.")
    

# interface for choosing operation
def calc():
    print("CLI base calculator")
    print("operation, +, -, *, /")

    try:
        num1 = int(input("Enter a first number."))
        operat = input("Enter a operation.")
        num2 = int(input("Enter a second number."))

        if operat == "+":
            result = add(num1, num2)
        elif operat == "-":
            result = sub(num1, num2)
        elif operat == "*":
            result = mul(num1, num2)
        elif operat == "/":
            result = divi(num1, num2)
        else:
            print("Invalid operation")

        print("result", result)
    except ValueError:
        print("Invalid value. please enter a numeric value")

calc()
        
