x = '21-06-2023'
y = x.split('-')
day = int(y[0])
month = int(y[1])
year = int(y[2])
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(sum(days[:month - 1]) + day)