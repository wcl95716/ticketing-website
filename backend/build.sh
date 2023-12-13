#!/bin/bash

# 定义源脚本和目标 EXE 文件路径
src_script="./my_start.py"
dest_exe="./my_start.exe"

# 执行 pyinstaller 命令
pyinstaller --onefile "$src_script"

# 复制生成的 EXE 文件
cp "./dist/$(basename "$src_script" .py).exe" "$dest_exe"

# 输出成功消息
echo "Build and copy completed: $dest_exe"
