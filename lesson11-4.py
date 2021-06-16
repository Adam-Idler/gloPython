# -*- coding: utf-8 -*-

numbers = str(input('Введите строку из натуральных чисел: ')).split()

pairs_number = 0

for value in numbers:
    pairs_number += numbers.count(value) - 1


print(pairs_number // 2)