#! /opt/anaconda3/bin/python3
# -*- coding: utf-8 -*-
# 将仓库 '/Users/jinchengguo/LearnWebDev' 推送到 GitHub
import os

# 获取当前目录作为 git 仓库路径
git_repository = os.path.abspath('.')

# 进入仓库目录
os.chdir(git_repository)


os.system('git add .')
os.system('git commit -m "auto commit"')
os.system('git push')

