# -*- coding: utf-8 -*-

count = int(input('Введите число строк: '))
bank = []

for i in range(count):
    string = str(input('Введите строку: '))
    bank.append(string)

request = str(input('Что желаете найти? '))

for value in bank:
    for val in value.split():
        if val.lower() == request.lower():
            print(value)
