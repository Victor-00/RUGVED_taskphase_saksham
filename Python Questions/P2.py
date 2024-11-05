'''
Write a python program to sort a string alphabetically and print the
count of each character.
    '''

s = input("Enter the string : ")
ss = sorted(s)

for i in range(len(ss)):
    print(ss[i] + " : " + str(i))
