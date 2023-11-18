#!/bin/bash
conda env list | grep ticketing-website || conda create --name ticketing-website python=3.9
eval "$(conda shell.bash hook)"
conda activate ticketing-website

# 你的其他命令
# 例如：
# python -m pip install --upgrade pip
# pip install -r requirements.txt
