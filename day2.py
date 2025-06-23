# 30 Days of Python Project Challenge
# ===================================

# Week 1: Fundamentals & Basics
# -----------------------------
# Day 2  – Number Analyzer: Take input, check even/odd, prime, or multiple.

def analyzer():
    user = int(input("Enter a number"))

    # checking even/odd
    if user % 2 == 0:
        print(f"{user} is even")
    else:
        print(f"{user} is odd")
    
    # prime number
    if user <= 1:
        print(user,"not a prime number")
    elif user == 2:
        print(f"{user} is prime number.")
    elif user % 2 == 0:
        print(f"{user} is not prime number.")
    else:
        is_prime = True
        for i in range(3, int(user ** 0.5) + 1, 2):
            if user % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f"{user} is prime number")
        else:
            print(f"{user} is not prime number") 

analyzer()

    