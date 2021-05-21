# -*- coding: utf-8 -*-

digit = int(input('Введите целое четырехзначное число: '))

first = digit // 1000
second = digit // 100 % 10
third = digit // 10 % 10
fourth = digit % 10

maxDigit = max(first, second, third, fourth)

print('У числа', digit, 'максимальная цифра равна', maxDigit)