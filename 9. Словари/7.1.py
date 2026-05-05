def f(word):
    points = {1: 'АВЕИНОРСТ',
              2: 'ДКЛМПУ',
              3: 'БГЁЬЯ',
              4: 'ЙЫ',
              5: 'ЖЗХЦЧ',
              8: 'ШЭЮ',
              10: 'ФЩЪ'}
    count = 0
    for key in points:
        for c in word:
            if c in points[key]:
                count += key
    return count
print(f('ТУТ'))