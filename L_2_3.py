m = int(input('Введите число месяца: '))
ls = ['Зима', 'Весна', 'Лето', 'Осень']

if m in (1, 2, 12):
    print(f'По списку это: {ls[0]}')
elif m in (3, 4, 5):
    print(f'По списку это: {ls[1]}')
elif m in (6, 7, 8):
    print(f'По списку это: {ls[2]}')
elif m in (9, 10, 11):
    print(f'По списку это: {ls[3]}')
else:
    pass

#dict
lss = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима',
}

print(f'По словарю это: {lss[m]}')
