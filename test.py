#!/opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
import os

current_path = os.path.abspath('.')
sub_dir = "JustForFun"
file_name = "Fun.py"

dir_path = os.path.join(current_path, sub_dir)
full_path = os.path.join(current_path, sub_dir, file_name)

if os.path.exists(full_path):
    pass
else: 
    os.mkdir(full_path)
