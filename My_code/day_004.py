#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File Name: day_004.py
@Author: xiaojinshui
@Created Time: 2020-08-21 15:10:24
@Description: 
'''


'''
example 1
    输入一个正整数判断是不是素数.
    提示:素数指的是只能被1和自身整除的大于1的整数
'''
def prime_number(number: int):
    if number <= 1:
        return None

    for i in range(2, number):
        if number % i == 0:
            return False
    else:
        return True


for i in range(100):
    if prime_number(i):
        print(f'{i}  ', end='')
print('')


'''
example 2
    输入两个正整数,计算它们的最大公约数和最小公倍数
    提示:两个数的最大公约数是两个数的公共因子中最大的那个数
         两个数的最小公倍数则是能够同时被两个数整除的最小的那个数
'''
def calc(x, y):
    if x > y:
        x, y = y, x

    for i in range(x, 0, -1):
        if x % i == 0 and y % i == 0:
            return i, x*y/i


print(calc(9, 21))
