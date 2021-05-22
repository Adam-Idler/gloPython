# -*- coding: utf-8 -*-

pocket_number = int(input('Введите номер кармана: '))

if pocket_number < 0 or pocket_number > 36:
    print('Кармана под таким номером нет!')
    
else:
    if pocket_number >= 1 and pocket_number < 11:
        if pocket_number % 2 == 0:
            print('Карман черного цвета')
        else:
            print('Карман красного цвета')

    elif pocket_number >= 11 and pocket_number < 19:
        if pocket_number % 2 == 0:
            print('Карман красного цвета')
        else:
            print('Карман черного цвета')

    elif pocket_number >= 19 and pocket_number < 29:
        if pocket_number % 2 == 0:
            print('Карман черного цвета')
        else:
            print('Карман красного цвета')

    elif pocket_number >= 29 and pocket_number < 37:
        if pocket_number % 2 == 0:
            print('Карман красного цвета')
        else:
            print('Карман черного цвета')
            
    else:
        print('Карман зеленого цвета')
        
