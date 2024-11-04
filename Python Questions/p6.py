def rev(s):
    ls = s[::-1]
    return ls
def ana(s,ls):
    if s == ls:
        return "The string is an anagram"
    else:
        return "The string is not an anagram"

s = input("Enter a string: ")
R = rev(s)
result = ana(s,R)
print(result)
