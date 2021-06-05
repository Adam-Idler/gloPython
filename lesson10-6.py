# -*- coding: utf-8 -*-

s = str(input('Введите строку: '))
result = ''

for c in s:
    if c.isdigit():
        result += c
        
print(result)