import pandas as pd
pd.set_option('display.max_columns', None)

# Часть 2

# -- 1 --
# Загрузка данных из csv файла
df = pd.read_csv('players_data-2024_2025.csv')

print(f"Исходный датасет: {df.shape}")

# Разделение на две части
part1 = df.iloc[:50].copy()
part2 = df.iloc[50:].copy()

# Удаление одной из колонок с числовым типом данных из первой части
part1 = part1.drop(columns=['xG'])

print(f"Первая часть part1.csv: {part1.shape}")
print(f"Первая часть part2.csv: {part2.shape}")

# Сохранение частей в отдельные файлы
part1.to_csv('part1.csv', index=False)
part2.to_csv('part2.csv', index=False)
print("Части сохранены в файлы part1.csv и part2.csv")

# Загрузка данных обратно из файлов
part1_df = pd.read_csv('part1.csv')
part2_df = pd.read_csv('part2.csv')
print(f"Загружено из part1.csv: {part1_df.shape}")
print(f"Загружено из part2.csv: {part2_df.shape}")

# Вертикальное объединение двух частей
concat_df = pd.concat([part1_df, part2_df])

# Сохранение результата
concat_df.to_csv('concat.csv', index=False)

print("=== Сравнение размерностей ===")
print(f"Исходный датасет: {df.shape}")
print(f"Объединённый датасет: {concat_df.shape}")
print(f"Пропуски после объединения в столбце xG: {concat_df['xG'].isnull().sum()}")

