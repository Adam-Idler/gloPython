balls = int(input('—колько м€чей желаете приобрести? '))
rubles = int(input('—колько рублей стоит один м€ч? '))
kopeck = int(input('—колько копеек стоит этот же м€ч? '))

rubles_from_kopecks = kopeck * balls // 100  # —колько рублей получитс€ из суммы копеек
kopeck = kopeck * balls % 100  #  оличество копеек делаем меньше 100

rubles = rubles * balls + rubles_from_kopecks # ќбщее количество рублей

print('«а', balls, 'м€ча/ей нужно заплатить', rubles, 'рублей и', kopeck, 'копеек')