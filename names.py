import csv

with open("names.csv",'r') as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

        
import pandas as pd
df = pd.read_csv("names.csv")
print(df)