import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/home/saksham/Downloads/matches.csv')
print("Q1) - The total number of matches in 2008 : " + str(len(df.loc[df['season'] == 2008])))
max = df['city'].value_counts().idxmax()
print("Q2)- The city with most matches is : " + max)
min = df['city'].value_counts().idxmin()
print("Q2) - The city with least matches is : " + min)
value_counts = df['city'].value_counts()
print("Q3) - Total count of matches city wise :-")
for value, count in value_counts.items():
    print(f"{value}: {count}")
maxT = df['toss_winner'].value_counts().idxmax()
print("Q4)- The team with most toss wins is : " + maxT)
minT = df['toss_winner'].value_counts().idxmin()
print("Q4) - The team with least toss wins is : " + minT)
'''
question 5
'''
value1_counts = df['result'].value_counts()
print("Q6) - Total count of matches :-")
for value1, count1 in value1_counts.items():
    if value1 != "no result":
      print(f"{value1}: {count1}")
print("Q7)- Team names where match resulted in a tie :- ")
print(df.loc[df['result'] == "tie", ['team1', 'team2']])
