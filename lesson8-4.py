# -*- coding: utf-8 -*-

number = int(input('Введите число n (n >= 10): '))

max = -100000000
min = 100000000

while number != 0:
    digit = number % 10
    if digit > max:
        max = digit
    if digit < min:
        min = digit
    number //= 10

print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)