num = input("Enter a number: ")
stnum = str(num)
largest = stnum[0]
a=0
for i in range(len(stnum)):

    for j in range(len(stnum)):

      if largest < stnum[i]:
         largest = stnum[i]
         f=i



for i in range(1,f,1):
    if stnum[i]<=stnum[a]:
        print("The number is not a hill number")
        exit(0)
    a=a+1
a=f
for i in range(f+1,len(stnum),1):
    if stnum[i]>=stnum[a]:
        print("The number is not a hill number")
        exit(0)
    a=a+1
if stnum[0] == stnum[len(stnum)-1]:
    print("The number is a hill number")
else :
    print("The number is not a hill number")
