import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('players_data-2024_2025.csv')

df = df[['Pos', 'Gls', 'Ast']]

df['is_forward'] = df['Pos'].str.contains('FW', na=False)

colors = {True: 'Green', False: 'Red'}
plt.scatter(df['Gls'], df['Ast'], c=df['is_forward'].map(colors), alpha=0.5)

plt.xlabel('Голы')
plt.ylabel('Ассисты')
plt.show()