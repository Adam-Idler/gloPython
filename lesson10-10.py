# -*- coding: utf-8 -*-

s = str(input('Введите строку: '))
result = 1

for c in s.strip():
    if ord(c) == 32:
        result += 1

print(result)