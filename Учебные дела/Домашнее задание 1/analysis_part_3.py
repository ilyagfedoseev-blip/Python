import pandas as pd

# Часть 3

# Загрузка данных из csv файла
df = pd.read_csv('players_data-2024_2025.csv')
df = df[['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Born', 'Min', 'MP', 'Comp', 'Starts', 'Gls', 'Ast', 'G+A', 'xG', 'xAG']]

# Очистка
df['Born'] = df['Born'].fillna(0).astype(int)
df['Min'] = df['Min'].fillna(0)
df['MP'] = df['MP'].fillna(0)
df['Starts'] = df['Starts'].fillna(0)
df['Gls'] = df['Gls'].fillna(0)
df['Ast'] = df['Ast'].fillna(0)
df['G+A'] = df['G+A'].fillna(0)
df['xG'] = df['xG'].fillna(0)
df['xAG'] = df['xAG'].fillna(0)

# Проверка гипотез
# Гипотеза 1: Игроки, чаще выходящие в стартовом составе, играют больше минут
median_starts = df['Starts'].median()
high_starts = df[df['Starts'] > median_starts]
low_starts = df[df['Starts'] <= median_starts]


