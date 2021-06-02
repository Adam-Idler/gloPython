# -*- coding: utf-8 -*-

number = int(input('Введите число: '))
count = 0

for i in range(1, number + 1):
    
    digit = i % 10

    if digit == 5:
        count += 1

    i //= 10

print(count)