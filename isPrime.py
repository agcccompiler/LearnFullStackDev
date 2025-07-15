#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, cpu_count
import time
import random

def is_prime(n):
    """判断一个数是否为素数"""
    # 增加一个大循环，模拟重任务
    for _ in range(10**8):
        pass
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_prime(number):
    result = is_prime(number)
    # 为了减少输出干扰，可以注释掉下面这行
    # print(f"{number} 是素数: {result}")

if __name__ == '__main__':
    # 生成100个接近10万亿的大随机奇数
    numbers = [random.randrange(10**15, 10**15 + 10000, 2) for _ in range(3)]

    # 单进程计算
    print("单进程计算：")
    start_single = time.time()
    for num in numbers:
        check_prime(num)
    print(f"单进程耗时: {time.time() - start_single:.2f} 秒\n")

    # 多进程计算
    print("多进程计算：")
    processes = []
    start_multi = time.time()
    for num in numbers:
        p = Process(target=check_prime, args=(num,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(f"多进程耗时: {time.time() - start_multi:.2f} 秒")