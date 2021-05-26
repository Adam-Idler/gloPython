# -*- coding: utf-8 -*-

number = int(input('Введите число: '))
numberCopy = number
sum = 0

while numberCopy != 0:
    digit = numberCopy % 10
    sum += digit
    numberCopy //= 10

if number % sum == 0:
    print('YES')
else:
    print('NO')
    