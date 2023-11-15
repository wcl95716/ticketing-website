
# 停止先前的程序
stop:
	-lsof -t -i :8001 | xargs kill -9

# 启动新程序
start:
	nohup python src/main.py > output.log &


install:
	conda env list | grep ticketing-website || conda create --name ticketing-website python=3.9
	python -m pip install --upgrade pip
	pip install --ignore-installed -r requirements.txt

checkout:
	conda activate ticketing-website

delete_env:
	conda remove -n ticketing-website --all

# 默认目标，停止先前的程序，然后启动新程序
all: install stop start