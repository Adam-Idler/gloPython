# -*- coding: utf-8 -*-

email = str(input('Введите e-mail: '))

if '@' in email and '.' in email:
    print('Электронный адрес корректный')
else:
    print('Электронный адрес некорректен')