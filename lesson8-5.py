# -*- coding: utf-8 -*-

number = int(input('Введите элемент последовательности: '))

pol_col = 0
otr_col = 0

while number != 0:
    if number > 0:
        pol_col += 1
    elif number < 0:
        otr_col += 1
    number = int(input('Введите элемент последовательности: '))

print('Произведение количества положительных цифра на отрицательные: ', pol_col * otr_col)