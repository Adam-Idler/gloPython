# -*- coding: utf-8 -*-

length = int(input('Сколько чисел будете вводить?\n'))

flag = 0

for i in range(1, length + 1):
    digit = int(input('Введите элемент последовательности: '))
    if digit % 2 == 0:
        flag = 1
        
if flag != 0:
    print('NO')
else:
    print('YES')