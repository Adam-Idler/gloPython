digit = int(input('Введите число не превыщающее 1 000 000 000: '))

first = digit % 1000 // 100
second = digit % 100 // 10
third = digit % 10

sum = first + second + third

print('У числа', digit, 'сумма последних трех цифр равна', sum)