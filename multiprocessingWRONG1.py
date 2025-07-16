#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 错误示例（无主模块保护）：
from multiprocessing import Pool

def task(x):
    return x * x

# 以下代码会被子进程重复执行！
pool = Pool(4)  # 子进程初始化时又会执行此行，导致递归创建新进程池
results = pool.map(task, [1, 2, 3])
