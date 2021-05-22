# -*- coding: utf-8 -*-

number = float(input('Введите вещественное число: '))

if number > 0:
    print('Число', number, 'положительное')
elif number < 0:
    print('Число', number, 'отрицательное')
else:
    print('Ноль')
