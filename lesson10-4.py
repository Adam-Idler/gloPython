# -*- coding: utf-8 -*-

s = str(input('Введите символ: '))

if ord(s) >= 1040 and ord(s) <= 1071 or ord(s) >= 1072 and ord(s) <= 1103:
    print(s)
    
elif ord(s) >= 65 and ord(s) <= 90:
    print(s.lower())
    
elif ord(s) >= 97 and ord(s) <= 122:
    print(s.upper())