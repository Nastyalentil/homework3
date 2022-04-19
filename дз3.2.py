print('Вітаю!')
numberf = int(input('Введіть перше число: '))
numbers = int(input('Введіть друге число: '))
if numberf > numbers:
    print(numberf, '>', numbers)
elif numberf < numbers:
    print(numberf, '<', numbers)
else:
    print(numberf, '=', numbers)