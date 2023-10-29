from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# 定义一个 WebSocket 事件，用于接收客户端发送的消息
@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    # 在接收到消息后，广播消息给所有连接的客户端
    emit('message', message, broadcast=True)

# 客户端连接时的处理
@socketio.on('connect')
def handle_connect():
    print('Client connected')

# 客户端断开连接时的处理
@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app, debug=True)
