#!/bin/bash

echo ""

# 获取脚本所在目录
ROOT_DIR="$(pwd)"

# 更新代码
git pull --no-rebase origin master

# 安装或升级依赖
#pip3 install --upgrade -r requirements.txt

echo "更新程序完成，请按下Press继续..."
read -r
