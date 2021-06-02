# -*- coding: utf-8 -*-

number = int(input('Введите натуральное число: '))

i = 1

while (i <= number):
    if (i >= 2 and i <= 8 or
        i >= 128 and i <= 256 or
        i >= 1024 and i <= 2048):
        
            i += 1
            continue

    print(i)
    i += 1