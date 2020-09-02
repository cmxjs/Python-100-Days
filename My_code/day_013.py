#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File Name: day_013.py
@Author: xiaojinshui
@Created Time: 2020-09-02 10:53:22
@Description: 并发编程 >>> 多进程，多线程, 异步I/O
'''


'''
多进程 : multiprocessing
'''
from multiprocessing import Process, Queue
from os import getpid
from random import randint
from time import sleep, time


def download_task(filename):
    print(f'启动下载进程，进程号[{getpid()}]')
    print(f'开始下载 {filename} ...')
    time_to_download = randint(1, 1)
    sleep(time_to_download)
    print(f'{filename} 下载完成! 耗费了{time_to_download}秒\n')


def process_down():
    start = time()
    down_list = ['Python从入门到住院.pdf', 'Python从入门到放弃.pdf']
    tasks = [Process(target=download_task, args=(i,)) for i in down_list]

    for task in tasks:
        task.start()  # 启动进程

    for task in tasks:
        task.join()  # 等待进程执行结束

    print(f'总共耗费了{time() - start :.2f}秒\n')


process_down()


'''
多线程 : threading
'''
# demo1
from threading import Thread


def thread_down():
    start = time()
    down_list = ['Python从入门到住院.pdf', 'Python从入门到放弃.pdf']
    tasks = [Thread(target=download_task, args=(i,)) for i in down_list]

    for task in tasks:
        task.start()  # 启动进程

    for task in tasks:
        task.join()  # 等待进程执行结束

    print(f'总共耗费了{time() - start :.2f}秒\n')


thread_down()


# demo2
class DownloadTask(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print(f'开始下载 {self._filename} ...')
        time_to_download = randint(1, 1)
        sleep(time_to_download)
        print(f'{self._filename} 下载完成! 耗费了{time_to_download}秒\n')


def thread_down():
    start = time()
    down_list = ['Python从入门到住院.pdf', 'Python从入门到放弃.pdf']
    tasks = [DownloadTask(i) for i in down_list]

    for task in tasks:
        task.start()  # 启动进程

    for task in tasks:
        task.join()  # 等待进程执行结束

    print(f'总共耗费了{time() - start :.2f}秒\n')


thread_down()


'''
使用多进程 multiprocessing 计算和, calc sum
'''
from time import time, sleep
from multiprocessing import Process, Queue


def create_list(n, split):
    li = []
    start = 0
    steps = int(n / split)

    for i in range(split + 1):
        if i == split:
            li.append(range(start, n))
        else:
            li.append(range(start, start+steps))
            start += steps

    return li


def add(ran):
    global sub_sum
    sub_sum.put(sum(ran))


def main():
    start = time()
    global sub_sum
    sub_sum = Queue()
    li = create_list(100000001, 6)
    tasks = [Process(target=add, args=(i,)) for i in li]

    for task in tasks:
        task.start()
    for task in tasks:
        task.join()

    total_sum = 0
    while not sub_sum.empty():
        total_sum += sub_sum.get()
    else:
        print(total_sum)
        print(f'总共耗费了{time() - start :.2f}秒\n')


main()
