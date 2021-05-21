# -*- coding: utf-8 -*-

digitOne = int(input('Введите первое целое число: '))
digitTwo = int(input('Введите второе целое число: '))

print(digitOne, 'умноженное на', digitTwo, 'равно', digitOne * digitTwo)
print(digitOne, 'деленное на', digitTwo, 'равно', digitOne / digitTwo)
print(digitOne, 'нацело деленное на', digitTwo, 'равно', digitOne // digitTwo)
print('Остаток от деления', digitOne, 'на', digitTwo, 'равен', digitOne % digitTwo)
print(digitOne, 'в степени', digitTwo, 'равно', digitOne ** digitTwo)