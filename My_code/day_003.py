#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File Name:day_003.py
@Author:xiaojinshui
@Created Time:2020-08-21 14:15:18
@Description:
'''


'''
example 2
    百分制成绩转换为等级制成绩,
    如果输入的成绩在90分以上(含90分)输出A；80分-90分(不含90分)输出B；
        70分-80分(不含80分)输出C；60分-70分(不含70分)输出D；60分以下输出E
'''
def conver2grade(score):
    grades = {
        range(90, 101): 'A',
        range(80, 90) : 'B',
        range(70, 80) : 'C',
        range(60, 70) : 'D',
        range(0,  60) : 'E',
    }
    for k, v in grades.items():
        if score in k:
            grade = v
            break
    else:
        grade = None

    return grade


print(conver2grade(81), conver2grade(67), conver2grade(47))


'''
example 3
    输入三条边长,如果能构成三角形就计算周长和面积
'''
def x(a, b, c):
    p = (a + b + c) / 2

    if (a2 := p * (p-a) * (p-b) * (p-c)) > 0:
        return 2*p, a2**0.5
    else:
        return None, None


a, b, c = 3, 4, 5
print(x(a, b, c))
