#  Fibonacci Series
# Take n as input and print the first n numbers in the Fibonacci sequence.
# 💡 Hint: Fibonacci series: 0, 1, 1, 2, 3, 5, 8, ...
# Each number is the sum of the previous two.


n = int(input("Enter a number: "))

a , b = 0 , 1

print("fabo series: ", end=" ")

for i in range(n):
    print(a , end=" ")
    a , b = b , a + b

print()