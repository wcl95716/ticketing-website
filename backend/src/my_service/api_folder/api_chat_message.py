from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__, template_folder="./")
socketio = SocketIO(app)
namespace = "/module1"  # 定义命名空间

chat_history = []

@app.route("/")
def home():
    return render_template("index.html")

@socketio.on("message", namespace=namespace)
def handle_message(msg):
    print("Received message: " + msg)
    chat_history.append(msg)

    if len(chat_history) > 20:
        chat_history.pop(0)

    socketio.emit("message", msg, broadcast=True, namespace=namespace)

@socketio.on("connect", namespace=namespace)
def handle_connect():
    print("User connected")
    socketio.emit("message", "有人加入了群聊", broadcast=True, namespace=namespace)

@socketio.on("disconnect", namespace=namespace)
def handle_disconnect():
    print("User disconnected")
    socketio.emit("message", "有人退出了群聊", broadcast=True, namespace=namespace)

if __name__ == "__main__":
    socketio.run(app, debug=True)
