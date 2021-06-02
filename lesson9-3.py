# -*- coding: utf-8 -*-

number = int(input('Введите число: '))

flag = 0

while (number > 0):
    digit = number % 10
    
    if digit == 1:
        flag = 1
        
    number //= 10

if flag != 0:
    print('YES')
else:
    print('NO')