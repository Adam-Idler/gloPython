# -*- coding: utf-8 -*-

number = int(input())
counter = 0

while number != 0:
    digit = number % 10
    if digit == 5:
        counter += 1
    number //= 10

print('Цифра 5 в данном числе встречается', counter, 'раз(а)')