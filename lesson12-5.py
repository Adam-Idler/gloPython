# -*- coding: utf-8 -*-

def stardate(date):
    date_array = date.split('.')
    return int(date_array[0]) * int(date_array[1]) == int(date_array[2][2:4])

user_date = str(input('Введите дату в формате ДД.ММ.ГГГГ: '))
print(stardate(user_date))
