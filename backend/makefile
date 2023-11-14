# 停止先前的程序
stop:
    -pkill -f "python src/main.py"

# 启动新程序
start:
    nohup python src/main.py > output.log &

# 默认目标，停止先前的程序，然后启动新程序
all: stop start