num = int(input("Enter the credit card number"))
sum1 = 0
sum2 = 0
for i in range(len(str(num))-2,-1,-2):
    d = 2*int((str(num)[i]))
    if (int(d) > 9):
        sum1 = sum1 + d // 10 + d % 10
    else:    
        sum1 = sum1 + int(d)   
for i in range(len(str(num))-1,-1,-2):
    sum2 = sum2 + int((str(num)[i]))
sum = sum1 + sum2           
if (sum % 10 == 0):
      print("The number is valid")
else:
    print("The number is not valid")      
       
    
    
