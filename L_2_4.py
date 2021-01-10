sl = input('Введите предложение: ').split()

for i, esl in enumerate(sl, 1):
    print(f'{i} слово: {esl[:10]}')
