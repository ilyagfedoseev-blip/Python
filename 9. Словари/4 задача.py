city = {'Санкт-Петербург': 'Невский проспект'}
while True:
    line = input('Введите город: ').strip()
    if line == 'стоп':
        break
    if line in city:
        print(city[line])
    else:
        street = input('Введите улицу: ').strip()
        city[line] = street
