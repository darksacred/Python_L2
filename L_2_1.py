a = [1, 1.1, 's', False, [1, 2, 3], {1: '2', 3: '4'}]
i = 0

while i < len(a):
    print(f'{type(a[i])}')
    i += 1


a = [1, 1.1, 's', False, [1, 2, 3], {1: '2', 3: '4'}]

for i in a:
    print(str(type(i)).split("'")[1], end=' ')


