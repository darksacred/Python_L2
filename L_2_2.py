el = input("Введите значения: ").split()

for i in range(0, len(el)-1, 2):
    el[i], el[i+1] = el[i+1], el[i]
print(el)
