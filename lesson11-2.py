# -*- coding: utf-8 -*-

path_list = str(input('Введите корректный путь до файла: ')).split('\\')

print(*path_list, sep='\n')