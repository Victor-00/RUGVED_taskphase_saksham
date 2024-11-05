'''
Write a program to print the Fibonacci Sequence till n-values where n
is user input
'''


def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fib(i))
