import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('AAVE_USD.csv')

df['date'] = pd.to_datetime(df.date).dt.date

# определение на сколько изменилась цена внутри дня от начала дня к макс значению
df = pd.DataFrame(df.groupby('date').max()['USD price'] / df.groupby('date').first()['USD price']).reset_index()

# определяем изменение цены на 10%
df = df[df['USD price'] > 1.1]

# вместо цены ставим 1 чтобы посчитать количество
df.loc[:, 'USD price'] = 1

# добавляем дни недели и групируем
df['date'] = pd.to_datetime(df.date)
df['day_w'] = df.date.dt.day_name()
df = df.groupby('day_w').sum().reset_index()

# сортировка по дям недели, для красоты
cats = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['day_w'] = pd.Categorical(df['day_w'], categories=cats, ordered=True)
df = df.sort_values('day_w')

# рисуем гистограмму
plt.bar(df['day_w'], df['USD price'])
plt.show()







