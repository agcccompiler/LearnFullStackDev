#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process, Queue
import time

# 使用队列进行进程间通信
result_queue = Queue()

# 函数1: 计算阶乘
def calculate_factorial(n, queue):
    print(f"[阶乘进程] 开始计算 {n}!")
    result = 1
    for i in range(1, n+1):
        result *= i
        time.sleep(0.1)  # 模拟计算时间
    queue.put(("阶乘", n, result))
    print(f"[阶乘进程] 完成: {n}! = {result}")

# 函数2: 生成斐波那契数列
def generate_fibonacci(n, queue):
    print(f"[斐波那契进程] 生成前 {n} 项")
    a, b = 0, 1
    sequence = []
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
        time.sleep(0.05)
    queue.put(("斐波那契", n, sequence))
    print(f"[斐波那契进程] 完成: 前{n}项 = {sequence}")

# 函数3: 检查素数
def check_prime(n, queue):
    print(f"[素数进程] 检查 {n} 是否为素数")
    if n < 2:
        is_prime = False
    else:
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
            time.sleep(0.01)
    queue.put(("素数", n, is_prime))
    print(f"[素数进程] 完成: {n} 是素数? {is_prime}")

if __name__ == '__main__':
    processes = [
        Process(target=calculate_factorial, args=(5, result_queue)),
        Process(target=generate_fibonacci, args=(8, result_queue)),
        Process(target=check_prime, args=(17, result_queue))
    ]
    
    print("主进程启动子进程...")
    start_time = time.time()
    
    # 启动所有子进程
    for p in processes:
        p.start()
    
    # 等待所有子进程完成
    for p in processes:
        p.join()
    
    # 从队列获取结果
    results = []
    while not result_queue.empty():
        results.append(result_queue.get())
    
    # 显示结果
    print("\n===== 所有任务完成 =====")
    print(f"总耗时: {time.time()-start_time:.2f}秒")
    for task_type, input_val, result in results:
        print(f"{task_type}({input_val}) → {result}")
