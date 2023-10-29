# 导入 Flask 库和 render_template 函数
from flask import Flask, render_template

# 导入 SocketIO 库
from flask_socketio import SocketIO

# 创建 Flask 应用
app = Flask(__name__, template_folder="./")

# 创建 SocketIO 实例，并将应用传递给它
socketio = SocketIO(app)

# 存储聊天记录的列表
chat_history = []

# 定义根路径的路由
@app.route("/")
def home():
    # 渲染名为 "index.html" 的 HTML 模板并返回给用户
    return render_template("index.html")

# 定义处理客户端发送的 "message" 事件的函数
@socketio.on("message")
def handle_message(msg):
    print("Received message: " + msg)

    # 将新消息添加到聊天记录中
    chat_history.append(msg)

    # 保持聊天记录的长度，这里只保留最后的20条消息
    if len(chat_history) > 20:
        chat_history.pop(0)

    # 向所有连接的客户端广播消息
    socketio.emit("message", msg)

# 定义处理客户端连接事件的函数
@socketio.on("connect")
def handle_connect():
    print("User connected")

    # todo 应该进行一个通知， 通知某某某进入了聊天页面
    # 用户连接时发送聊天记录给他们
    # for msg in chat_history:
    #     socketio.emit("message", msg)

# 检查当前文件是否作为主程序运行
if __name__ == "__main__":
    # 启动 Flask-SocketIO 服务器，启用调试模式
    socketio.run(app, debug=True)
