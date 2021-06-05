# -*- coding: utf-8 -*-

chr1 = str(input('Введите первый символ: '))
chr2 = str(input('Введите второй символ: '))

if chr1 > chr2:
    chr1, chr2 = chr2, chr1

for i in range(ord(chr1), ord(chr2) + 1):
    print(chr(i))
