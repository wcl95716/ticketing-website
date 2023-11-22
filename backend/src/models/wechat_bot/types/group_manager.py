import time
# import keyboard

import sys 
sys.path.append("./src")


# from models.wechat_bot.utils.chat import get_chat_messages, send_message


from models.wechat_bot.types.group_chat_manager import GroupChatManager


from collections import deque
# import PyOfficeRobot
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory, ChatActionsEnum
from models.wechat_bot.types.chat_command_handler import ChatCommandHandler

# from models.wechat_bot.utils.chat import get_chat_messages

from models.wechat_bot.config import config


class GroupManager:
    def __init__(self, group_list: list[str] , robot_name:str = config.robot_name, actions:list[ChatActionsEnum] = [ChatActionsEnum.WORK_ORDER_CREATE] ):
        self.group_list = group_list
        self.robot_name = robot_name
        self.actions = actions
        pass
    
    def fix_group_task(self,group_id,tasks):
        for task in tasks:
            #send_message(group_id,task)
            pass 
        pass
    
    def process_group_tasks(self ):
        chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        for group_id in self.group_list:
            group = GroupChatManager(group_id=group_id)
            chat_messages = []
            # chat_messages = get_chat_messages(group.group_id)
            tasks:[] = group.find_task(chat_keyword_handler,chat_messages)
            self.fix_group_task(group_id,tasks)
        pass
    
    pass 

stop_requested = False  # 全局停止标志

def test_group_manager():
    group_list = ["测试4群", "测试2群", "测试3群"]
    group_manager = GroupManager(group_list)

    # 启动一个单独的线程来监听停止按钮
    # keyboard_thread = keyboard.Listener(on_press=on_key_press)
    # keyboard_thread.start()

    global stop_requested  # 引用全局停止标志
    while not stop_requested:  # 循环直到停止标志为True
        print("开始处理群聊任务")
        group_manager.process_group_tasks()
        time.sleep(1)

def on_key_press(keyboard_event):
    global stop_requested  # 引用全局停止标志
    if keyboard_event.name == '2':
        stop_requested = True  # 请求停止


if __name__ == "__main__":
    print("开始处理群聊任务")
    test_group_manager()
    pass