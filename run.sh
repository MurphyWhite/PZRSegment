#!/bin/bash

# 获取当前脚本所在的目录
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# 切换到脚本所在的目录
cd "$SCRIPT_DIR"

# 运行 main.py
echo "准备运行, 请将需要分词的语句放入txt文件，并放入origin文件夹中，按回车键继续"
read -r
python3 main.py
echo "运行完成"