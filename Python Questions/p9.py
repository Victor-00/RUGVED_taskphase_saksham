'''
Write a python function to encrypt a string using Ceasar’s Cipher
'''

a = "abcdefghijklmnopqrstuvwxyz"
r = ""

txt = input("Enter the string: ")
s = int(input("Enter the shift: "))

for c in txt:
    if c in a:
        r = r + a[(a.index(c) + s) % 26]
    else:
        r = r + c

print(r)