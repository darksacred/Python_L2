my_list = [7, 5, 3, 3, 2]
n = int(input('Введите новый результат: '))

for i, sl in enumerate(my_list, 1):

    if sl <= n:
        my_list.insert(i - 1, n)
        break
    elif n < min(my_list):
        my_list.append(n)
        break

print(f'Результат: {my_list}')
