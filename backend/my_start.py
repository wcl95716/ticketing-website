import tkinter as tk
import subprocess
import os

class LauncherApp:
    def __init__(self, root):
        self.root = root
        root.title("Python启动器")

        # 获取屏幕的宽度和高度
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # 设置窗口大小
        root.geometry("400x200")

        # 将窗口放置在右上角
        x_position = 0
        y_position = 0
        root.geometry("+{}+{}".format(x_position, y_position))

        # 创建启动按钮
        self.start_button = tk.Button(root, text="启动", command=self.start_process, width=20, height=2)
        self.start_button.pack(pady=20)

        # 创建结束按钮
        self.stop_button = tk.Button(root, text="结束", command=self.stop_all_processes, width=20, height=2)
        self.stop_button.pack()

        self.processes = []  # 存储已启动的子进程

        # 窗口置顶
        root.attributes("-topmost", True)

        # 捕获关闭窗口事件
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def start_process(self):
        if self.processes:
            print("还有其他进程在运行中")
        else:
            process = subprocess.Popen(["python", "src/models/wechat_bot/api/main.py"])
            self.processes.append(process)

    def stop_all_processes(self):
        for process in self.processes:
            if process.poll() is None:
                process.terminate()
        self.processes.clear()
        print("所有进程已终止")

    def on_closing(self):
        # 关闭窗口时终止所有进程
        self.stop_all_processes()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = LauncherApp(root)
    root.mainloop()
