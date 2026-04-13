import pandas as pd
# pd.set_option('display.max_columns', None)

# Часть 1

# -- 2 --
# Загрузка данных из csv файла
df = pd.read_csv('players_data-2024_2025.csv')
df = df[['Rk', 'Player', 'Nation', 'Pos', 'Squad', 'Born', 'Min', 'MP', 'Comp', 'Starts', 'Gls', 'Ast', 'G+A', 'xG', 'xAG']]

# Вывод первых 5 строк
print("=== Первые 5 строк ===")
print(df.head())
# Вывод последних 5 строк
print("\n=== Последние 5 строк ===")
print(df.tail())

# -- 3 --
# Общая информация о датасете
print("\n=== Информация о датасете ===")
df.info()

# Проверка пропусков
print("\n=== Количество пропусков по столбцам")
print(df.isnull().sum())

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

# Проверка на выбросы
print("\n=== Проверка на выбросы ===")
print(df.describe())

# Новые поля

def pos_to_role(pos):
    roles = pos.split(',')
    pos_role = {'GK': 'Вратарь',
                'DF': 'Защитник',
                'MF': 'Полузащитник',
                'FW': 'Нападающий'}
    return ' '.join([pos_role[role] for role in roles])

df['goal_per_90'] = df['Gls'] * 90 / df['Min'].replace(0, float('nan'))
df['xG_difference'] = df['Gls'] - df['xG']
df['Pos'] = df['Pos'].apply(pos_to_role)

print("\n=== Датасет с новыми параметрами ===")
print(df[['Player', 'Pos', 'Min', 'Gls', 'xG', 'goal_per_90', 'xG_difference']].tail(20))
