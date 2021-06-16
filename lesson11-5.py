# -*- coding: utf-8 -*-

numbers = str(input('Введите строку из натуральных чисел: ')).split()
numbers_list = []

for val in numbers:
    if numbers.count(val) == 1:
        numbers_list.append(val)

print(*numbers_list)