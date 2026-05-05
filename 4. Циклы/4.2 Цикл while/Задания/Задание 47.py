number = int(input("Введите целое число: "))
x = 0
while number > 0:
    x += number % 10
    number = number // 10
print("Сумма цифр = %d" % (x))
