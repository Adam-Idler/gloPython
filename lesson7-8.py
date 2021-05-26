# -*- coding: utf-8 -*-

length = int(input('Сколько чисел будете вводить?\n'))

max = -100000000
min = 100000000

for i in range(1, length + 1):
    digit = int(input('Введите элемент последовательности: '))
    if digit > max:
        max = digit
    if digit < min:
        min = digit


print('Минимум равен:', min)
print('Максимум равен:', max)
