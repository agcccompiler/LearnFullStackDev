#! /opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
# 将仓库 '/Users/jinchengguo/LearnWebDev' 推送到 GitHub
import os

git_repository = os.path.abspath('.')


os.chdir(git_repository)
os.system('git add .')
os.system('git commit -m "auto commit"')
os.system('git push')

