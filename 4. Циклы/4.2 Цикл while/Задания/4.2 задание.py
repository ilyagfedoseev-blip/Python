def f(n):
    x = 0
    for i in range(1, n + 1):
        x += 1 / i
    return x

n = int(input("Введите натуральное число:"))

print(f(n))

