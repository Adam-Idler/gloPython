# -*- coding: utf-8 -*-

def count_days_in_month(month):
    return [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1]

months = ['январе', 'феврале', 'марте', 'апреле', 'мае', 'июне',
          'июле', 'августе', 'сентябре', 'октябре', 'ноябре', 'декабре']

month = int(input('Введите номер месяца: '))
print(f'Количество дней в {months[month-1]}: {count_days_in_month(month)}')