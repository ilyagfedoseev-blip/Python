import pandas as pd
from matplotlib import pyplot as plt

def age_group(age):
    if pd.isna(age):
        return 'N/A'
    age = int(age)
    if age <= 18:
        return '17-18'
    elif 18 <= age <= 24:
        return '19-22'
    elif 24 <= age <= 26:
        return '23-26'
    elif 26 <= age <= 30:
        return '27-30'
    elif 31 <= age <= 34:
        return '31-34'
    elif age >= 35:
        return '35+'

df = pd.read_csv('players_data-2024_2025.csv')

df = df[['Pos', 'Gls', 'Age']]

df['is_forward'] = df['Pos'].str.contains('FW', na=False)

ages = ['17-18', '19-22', '23-26', '27-30', '31-34', '35+']

df['ages'] = df['Age'].apply(age_group)

forwards_by_age = df[df['is_forward'] == True].groupby('ages')['Gls'].mean().reindex(ages)
no_forwards_by_age = df[df['is_forward'] == False].groupby('ages')['Gls'].mean().reindex(ages)

plt.plot(ages, forwards_by_age, label='Нападающие')

plt.plot(ages, no_forwards_by_age, label='Не нападающие')

plt.xlabel('Возрастная группа')
plt.ylabel('Среднее кол-во голов')
plt.grid()
plt.legend()
plt.show()