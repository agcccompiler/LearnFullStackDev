#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Pool
import time, os

def square(x):
    time.sleep(0.5)  # 模拟耗时操作
    return x * x
def initialization():
    print(f"initializing process {os.getpid()}")

if __name__ == '__main__':
    # 创建包含4个工作进程的池
    with Pool(processes=os.cpu_count(), initializer=initialization, initargs=()) as pool:
        start = time.time()
        # 同步map（阻塞主进程）
        results = pool.map(square, range(10))
        print("Ordered results:", results)
        
        # 异步map（非阻塞）
        async_result = pool.map_async(square, range(10))
        print("Do other work while waiting...")
        print(f"for example, calculating 5*5 = {5*5}")
        print("Async results:", async_result.get())  # 获取结果时阻塞
        
        # 按完成顺序获取结果
        for res in pool.imap_unordered(square, range(10)):
            print("Unordered:", res)
        
        end = time.time()
        print(f"start time:{start}")
        print(f"end time: {end}")
        print(f"total time: {end - start}")
