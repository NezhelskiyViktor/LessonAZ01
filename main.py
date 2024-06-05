import pandas as pd
import numpy as np
import os

df = pd.read_csv('dz.csv')
df.drop(7, axis=0, inplace=True)
df.fillna('Прочие', inplace=True)
print(df)
grouped = df.groupby('City')['Salary'].mean()
print(grouped)
df.to_csv('new_dz.csv', index=False)
