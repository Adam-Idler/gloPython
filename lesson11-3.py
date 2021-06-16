# -*- coding: utf-8 -*-


ip_list = str(input('Введите ip-адрес: ')).split('.')

flag = 0

for val in ip_list:
    if int(val) > 255 or int(val) < 0 or len(ip_list) != 4:
        flag = 1

if flag != 0:
    print('NO')
else:
    print('YES')