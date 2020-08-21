#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File Name:day_002.py
@Author:xiaojinshui
@Created Time:2020-08-21 13:55:47
@Description:
'''


'''
example 1:
    将华氏温度转换为摄氏温度
    华氏温度到摄氏温度的转换公式为:$C=(F - 32) \div 1.8$
'''
def F2C(F):
    C = (F - 32) / 1.8
    return C


C = F2C(100)
print(f'{C:.1f}')


'''
example 2:
    输入圆的半径计算计算周长和面积
'''
from math import pi
def calc(r):
    P = 2 * pi * r
    A = pi * r ** 2
    return P, A


P, A = calc(10)
print(f'{P:.2f}, {A:.2f}')


'''
example 3:
    输入年份判断是不是闰年
'''
x = lambda y : True if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0) else False

print(x(2000), x(2008))
