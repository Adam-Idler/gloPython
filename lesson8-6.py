# -*- coding: utf-8 -*-

number = int(input('Введите элемент последовательности: '))
sum = 0
col = 0

while number != 0:
    sum += number
    col += 1
    number = int(input('Введите элемент последовательности: '))
    
print('Среднее арифмитическое элементов: ', sum // col)