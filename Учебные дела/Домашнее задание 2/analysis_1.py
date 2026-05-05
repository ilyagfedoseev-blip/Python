import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('players_data-2024_2025.csv')

df = df[['Pos', 'Gls']]

df['is_forward'] = df['Pos'].str.contains('FW', na=False)

avg_goals = df.groupby('is_forward')['Gls'].mean()

plt.pie(
    avg_goals,
    labels=['Иной', 'Нападающий'],
    colors=['green', 'blue'],
    startangle=90,
    autopct=lambda p: f'{p:,.0f}%',
)

plt.legend()
plt.show()
