# -*- coding: utf-8 -*-

def find_count_digits(number):
    return len(str(number))

number1 = int(input('Введите первое натуральное число: '))
number2 = int(input('Введите второе натуральное число: '))

number1_digits_count = find_count_digits(number1)
number2_digits_count = find_count_digits(number2)

print('Произведение разрядов:', number1_digits_count * number2_digits_count)
