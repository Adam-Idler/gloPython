# -*- coding: utf-8 -*-

def calculate_delivery_cost(count_products):
    return 100 + (count_products - 1) * 50

user_count_product = int(input('Введите количество товаров: '))

print(f'Цена за доставку: {calculate_delivery_cost(user_count_product)} руб.')