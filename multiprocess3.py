#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process

def child_task():
    child_var = "子进程数据"
    print(f"子进程: {child_var} (id={id(child_var)})")

if __name__ == '__main__':
    main_var = "主进程数据"
    print(f"主进程初始: {main_var} (id={id(main_var)})")
    
    p = Process(target=child_task)
    p.start()
    p.join()
    
    # 尝试访问子进程变量（会报错）
    try:
        print(child_var)  # NameError: name 'child_var' is not defined
    except NameError:
        print("主进程无法访问子进程变量")
    
    print(f"主进程结束: {main_var} (id={id(main_var)})")
