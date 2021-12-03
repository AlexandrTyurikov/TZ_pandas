import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('AAVE_USD.csv')
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%dT')
df.plot(x='date', y='USD price')
plt.show()