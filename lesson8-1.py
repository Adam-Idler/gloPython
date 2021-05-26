# -*- coding: utf-8 -*-

number = int(input('Введите натуральное число: '))
counter = 0

while number != 0:
    if number % 2 == 0:
        counter += 1
    number /= 2

print('Число делится на 2 без отстака', i, 'раз(а)')