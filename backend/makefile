# 停止先前的程序
stop:
	-lsof -t -i :8001 | xargs kill -9

# 启动新程序
start:
	nohup python src/main.py > output.log &

# 默认目标，停止先前的程序，然后启动新程序
all: stop start