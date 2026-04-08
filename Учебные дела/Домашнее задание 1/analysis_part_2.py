import pandas as pd
pd.set_option('display.max_columns', None)
# Часть 2
# -- 1 --
# Загрузка данных из csv файла
df = pd.read_csv('players_data-2024_2025.csv')

part1 = df.iloc[:50].copy()
part2 = df.iloc[50:].copy()

part1 = part1.drop(columns=['xG'])

# ...

part1.to_csv('part1.csv', index=False)
part2.to_csv('part2.csv', index=False)




