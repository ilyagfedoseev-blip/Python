import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv('players_data-2024_2025.csv')

df = df[['Comp', 'Gls']]

grouped = df.groupby(['Comp'])['Gls'].mean().dropna()

print(grouped)