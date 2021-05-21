digit = int(input('Введите целое трехзначное число: '))

first = digit // 100
second = digit % 100 // 10
third = digit % 10

sum = first + second + third
mult = first * second * third

print('Сумма цифр числа', digit, 'равна', sum)

print('Произведение цифр числа', digit, 'равно', mult)