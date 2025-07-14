#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
import os

current_path = os.path.abspath('.')
sub_dir = "JustForFun"
file_name = "Fun.py"

dir_path = os.path.join(current_path, sub_dir)
full_path = os.path.join(current_path, sub_dir, file_name)

if not os.path.exists(dir_path):
    os.mkdir(dir_path)

if not os.path.exists(full_path):
    with open(full_path, 'w', encoding='utf-8') as f:
        pass

# 在 fun.py 文件中写入一些代码（本次要求用 sys.argv）
with open(full_path, 'w', encoding='utf-8') as f:
    f.write("#!/usr/bin/env python3\n")
    f.write("# -*- coding: utf-8 -*-\n")
    f.write("import sys\n")
    f.write("def say_hello():\n")
    f.write("    args = sys.argv\n")
    f.write("    if len(args) == 1:\n")
    f.write("        print('Hello from Fun.py!')\n")
    f.write("    elif len(args) == 2:\n")
    f.write("        print(f'Hello, {args[1]} from Fun.py!')\n")
    f.write("    else:\n")
    f.write("        print('Too many arguments!')\n")
    f.write("\n")
    f.write("if __name__ == '__main__':\n")
    f.write("    say_hello()\n")

# 运行 fun.py 文件，并传递命令行参数（如果有）
import sys
argv_str = ""
if len(sys.argv) > 1:
    # 拼接所有参数，注意第一个参数是脚本名，需要跳过
    argv_str = " " + " ".join([f'"{arg}"' for arg in sys.argv[1:]])
status_code = os.system(f'python "{full_path}"{argv_str}')
print(f"子进程返回状态码: {status_code}")