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

avg_min_high = high_starts['Min'].mean()
avg_min_low = low_starts['Min'].mean()

print("Гипотеза 1: Игроки, чаще выходящие в стартовом составе, играют больше минут")
print(f"Медиана числа выходов в стартовом составе: {median_starts}")
print(f"Среднее число минут у игроков часто играющих в стартовом составе: {avg_min_high}")
print(f"Среднее число минут у игроков редко играющих в стартовом составе: {avg_min_low}")
if avg_min_high > avg_min_low:
    print("Вывод: Гипотеза 1 подтверждена!")
else:
    print("Вывод: Гипотеза 1 опровергнута!")

# Гипотеза 2: Игроки с высоким xG забивают больше голов
median_xG = df['xG'].median()
high_xG = df[df['xG'] > median_xG]
low_xG = df[df['xG'] <= median_xG]

avg_gls_high = high_xG['Gls'].mean()
avg_gls_low = low_xG['Gls'].mean()

print("\nГипотеза 2: Игроки с высоким xG забивают больше голов")
print(f"Медиана xG: {median_xG}")
print(f"Среднее кол-во голов у игроков с высоким xG: {avg_gls_high}")
print(f"Среднее кол-во голов у игроков с низким xG: {avg_gls_low}")

if avg_gls_high > avg_gls_low:
    print("Вывод: Гипотеза 2 подтверждена!")
else:
    print("Вывод: Гипотеза 2 опровергнута!")

# Гипотеза 3: Игроки, сыгравшие больше минут, в среднем совершают больше результативных действий (G+A)
median_min = df['Min'].median()
high_min = df[df['Min'] > median_min]
low_min = df[df['Min'] <= median_min]

avg_ga_high = high_min['G+A'].mean()
avg_ga_low = low_min['G+A'].mean()

print("\nГипотеза 3: Игроки, сыгравшие больше минут, в среднем совершают больше результативных действий (G+A)")
print(f"Медиана минут: {median_min}")
print(f"Среднее G+A игроков сыгравшим больше минут: {avg_ga_high}")
print(f"Среднее G+A у игроков сыгравших меньше минут: {avg_ga_low}")

if avg_ga_high > avg_ga_low:
    print("Вывод: Гипотеза 3 подтверждена!")
else:
    print("Вывод: Гипотеза 3 опровергнута!")

# Особая метка ))))