'''
Write a python function to encrypt a string using Ceasar’s Cipher
'''

def cc(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char  
    return encrypted_text

text = input("Enter the string : ")
shift = int(input("Enter the shift : "))
result = cc(text,shift)
print(result)
