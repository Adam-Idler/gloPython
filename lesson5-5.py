# -*- coding: utf-8 -*-

from math import ceil

homework_col = int(input('Введите количество домашних заданий, которое нужно выполнить: '))
homework_pos = int(input('Сколько заданий Вы делаете в день? '))

if homework_col < 0 or homework_pos < 0:
    print('Дни не могут быть отрицательными!')
else:
    days_col = ceil(homework_col / homework_pos)
    
    print('Вы выполните все задания за', days_col, 'дней(ь/я)')

      