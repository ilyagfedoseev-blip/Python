x = []
while True:
    y = input()
    if y == "стоп":
        break

    try:
        x.append(int(y))
    except:
        continue
x.sort()
print(x)