enru = {'one': 'один', 'two': 'два', 'three': 'три'}
ruen = {}
for key in enru:
    for value in enru[key]:
        ruen[key] = value

print(ruen)

for key, value in enru.items():
    ruen[value] = key