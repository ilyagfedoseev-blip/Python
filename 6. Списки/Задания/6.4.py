x = [24, 22, 51, 667, 43424]
y = []
for i in range(len(x) - 2):
    y.append((x[i] + x[i + 1] + x[i + 2]) / 3)
    print(y)



