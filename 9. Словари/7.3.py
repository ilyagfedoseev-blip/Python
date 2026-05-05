line = 'Сергей: Карандаш-3; Андрей: Тетрадь-5; Юлия: Линейка-1; Сергей: Ручка-2; Юлия: Книга-4; Сергей: Карандаш-2'
buyers = {}
for buy in line.split(';'):
    name, good = buy.split(':')
    name_good, count = good.split('-')
    name = name.strip()
    good = good.strip()
    name_good = name_good.strip()
    count = int(count)
    if name in buyers:
        if name_good in buyers[name]:
            buyers[name][name_good] += count
        else:
            buyers[name][name_good] = count
    else:
        buyers[name] = {name_good: count}

print(buyers['Сергей'])