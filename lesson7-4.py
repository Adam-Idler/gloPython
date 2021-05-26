# -*- coding: utf-8 -*-

range1 = int(input())
range2 = int(input())

if range2 < range1:
    range2, range1 = range1, range2

for i in range(range1, range2 + 1, 2):
    print(i)