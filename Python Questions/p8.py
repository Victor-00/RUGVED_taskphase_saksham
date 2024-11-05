'''
Write a python program to divide a given string into equal parts
containing n(user input) characters of same sequence.
'''


s = input("Enter the string: ")
n = int(input("Enter the value of n: "))
if len(s) % n != 0:
    print("The string cannot be evenly divided")
    exit(0)
p = [s[i:i + n] for i in range(0, len(s), n)]

print("Divided string into equal parts:")
for j in p:
    print(j)
