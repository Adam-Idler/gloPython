# -*- coding: utf-8 -*-

number = int(input('Введите натуральное число: '))

i = 1
flag = 0

while (i < number):
    if (number % i == 0 and i != 1 and i != number):
        flag = 1
        
    i += 1

if (flag != 0):
    print('NO')
else:
    print('YES')