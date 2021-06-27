# -*- coding: utf-8 -*-

def find_max(arr):
    return max(arr, key=lambda i: int(i))

list1 = str(input('Введите элементы первого списка через пробел: ')).split()
list2 = str(input('Введите элементы второго списка через пробел: ')).split()

max_list1 = int(find_max(list1))
max_list2 = int(find_max(list2))

print('Произведение максимальных элементов:', max_list1 * max_list2)
