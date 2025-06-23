# 30 Days of Python Project Challenge
# ===================================

# Week 1: Fundamentals & Basics
# -----------------------------
# Day 7  – Password Generator: Use random and string modules.

import random
import string

# user inputs
letter = int(input("How many letter you want Enter the length:"))
number = int(input("How many number you want Enter the length:"))
special = int(input("How many special character you want Enter the length:"))

# generate random letter 
char = ''.join(random.choice(string.ascii_letters) for _ in range(letter))
# generate random number
digit = ''.join(random.choice(string.digits) for _ in range(number))
# generate random special char
punctuation = ''.join(random.choice(string.punctuation) for _ in range(special))
# arranging in list 
ran_pass = [char, digit, punctuation]
# randomly shuffling the list 
random.shuffle(ran_pass)
# convert the list in string 
password = ''.join(ran_pass)

print("Generated password => ",password)

