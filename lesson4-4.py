# -*- coding: utf-8 -*-

balls = int(input('Сколько мячей желаете приобрести? '))
rubles = int(input('Сколько рублей стоит один мяч? '))
kopeck = int(input('Сколько копеек стоит этот же мяч? '))

rubles_from_kopecks = kopeck * balls // 100  # Сколько рублей получится из суммы копеек
kopeck = kopeck * balls % 100  # Количество копеек делаем меньше 100

rubles = rubles * balls + rubles_from_kopecks  # Общее количество рублей

print('За', balls, 'мяча/ей нужно заплатить', rubles, 'рублей и', kopeck, 'копеек')