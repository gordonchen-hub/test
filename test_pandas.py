import pandas as pd
s = pd.read_csv('data.csv')
print(s.isnull().sum())
c.to_csv('0520-1.csv')