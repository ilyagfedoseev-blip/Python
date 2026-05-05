x = [1, 2, 2, 3, 5, 1, 13, 21, 34, 55, 89]
for i in x:
    if x.count(i) > 1:
        x.remove(i)
print(x)
