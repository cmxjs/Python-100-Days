#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File Name:day_001.py
@Author:xiaojinshui
@Created Time:2020-08-21 13:39:55
@Description:
'''
import turtle


turtle.pensize(4)
turtle.pencolor('blue')

for _ in range(8):
    turtle.forward(100)
    turtle.right(45)

turtle.mainloop()
