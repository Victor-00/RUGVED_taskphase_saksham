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
