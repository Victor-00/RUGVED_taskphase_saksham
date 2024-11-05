'''
Write a python function to perform selection sort on a given string.
'''

s = input("Enter The string: ")
ls = list(s)

for i in range(len(ls)):
    min = i
    for j in range(i,len(ls)):
        if ls[j] < ls[min]:
            min = j

    temp = ls[i]
    ls[i] = ls[min]
    ls[min] = temp
print(''.join(ls))
