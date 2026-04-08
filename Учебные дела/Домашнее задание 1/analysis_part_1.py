import pandas as pd
pd.set_option('display.max_columns', None)
# Часть 1
# -- 2 --
# Загрузка данных из csv файла
df = pd.read_csv('players_data-2024_2025.csv')
df = df[['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Born', 'Min', 'MP', 'Comp', 'Starts', 'Gls', 'Ast', 'G+A', 'xG', 'xAG']]

# Вывод первых 5 строк
print(df.head())
# Вывод последних 5 строк
print(df.tail())

# -- 3 --
df.info()
# Очистка ?????????????

df['Born'] = df['Born'].fillna(0).astype(int)
# Новые поля

def pos_to_role(pos):
    roles = pos.split(',')
    pos_role = {'GK': 'Вратарь',
                'DF': 'Защитник',
                'MF': 'Полузащитник',
                'FW': 'Нападающий'}
    return ' '.join([pos_role[role] for role in roles])

df['goal_per_90'] = df['Gls'] / df['Min'] / 90
df['xG_difference'] = df['Gls'] - df['xG']
df['Pos'] = df['Pos'].apply(pos_to_role)

print(df.tail(20))


