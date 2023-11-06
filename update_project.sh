#!/bin/bash

# 获取脚本文件的目录
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 进入你的项目目录
cd "$script_dir"

# 检查是否提供了分支名称作为参数
if [ $# -eq 0 ]; then
  echo "请提供要切换到的分支名称作为参数。"
  exit 1
fi
# 提取第一个参数作为分支名称
branch_name="$1"
# 切换到指定分支
git checkout "$branch_name"


# 执行 git pull 命令以更新代码
git pull
