def f(lst):
    count = 1
    for i in range(len(lst) - 1):
        if lst[i] != lst[i + 1]:
            count += 1
    return count


x = [4, 6, 22, 24, 51]
print(f(x))
