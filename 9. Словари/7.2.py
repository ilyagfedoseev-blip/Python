s = "Сергей: Карандаш-3; Андрей: Тетрадь-5; Юлия: Линейка-1; Сергей: Ручка-2; Юлия: Книга-4; Сергей: Карандаш-2"
result = {}
for item in s.split(";"):
    name, purchase = item.strip().split(": ")
    product, quantity = purchase.split("-")
    quantity = int(quantity)
    if name not in result:
        result[name] = {}
    if product not in result[name]:
        result[name][product] = 0
    result[name][product] += quantity
print(result["Сергей"])
