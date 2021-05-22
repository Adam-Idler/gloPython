# -*- coding: utf-8 -*-

ticket = int(input('Введите номер билета(шестизначное число): '))

first = ticket // 100000
second = ticket // 10000 % 10
third = ticket // 1000 % 100 % 10

sum1 = first + second + third

fourth = ticket % 1000 // 100
fith = ticket % 100 // 10
sixth = ticket % 10

sum2 = fourth + fith + sixth

if sum1 == sum2:
    print('Поздравляю! Ваш билет', ticket, '- счастливый!')
else:
    print('К сожалению, билет', ticket, 'не счастливый. Оплачивайте проезд!')