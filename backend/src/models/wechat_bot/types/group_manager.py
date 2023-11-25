import time
# import keyboard
import sys
sys.path.append("./src")

from utils import local_logger


from models.wechat_bot.utils.chat import get_chat_messages, send_message 



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
        self.group_manager_list:list[GroupChatManager] = []
        for group_id in self.group_list:
            group = GroupChatManager(group_id=group_id)
            self.group_manager_list.append(group)
        self.robot_name = robot_name
        self.actions = actions
        self.is_init = False
        self.group_init_send_message()
        pass
    
    def group_init_send_message(self,group_id,tasks):
        for task in tasks:
            send_message(group_id,"机器人已启动")
            pass 
        pass
    
    def fix_group_task(self,group_id,tasks):
        for task in tasks:
            local_logger.logger.info(f" fix tasks {task}")
            task_result = task[0](task[1],task[2])
            send_message(group_id,task_result[1])
            pass 
        pass
    
    def process_group_tasks(self ):
        chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        for group in self.group_manager_list:
            group_id = group.group_id
            local_logger.logger.info(f"处理群聊 {group_id}")
            # chat_messages = []
            chat_messages = get_chat_messages(group_id)
            tasks:[] = group.find_task(chat_keyword_handler,chat_messages)
            local_logger.logger.info(f" find tasks {tasks}")
            if self.is_init:
                self.fix_group_task(group_id,tasks)
        self.is_init = True
        pass
    
    pass 

stop_requested = False  # 全局停止标志

def test_group_manager():
    group_list = ["测试4群", "测试3群"]
    # group_list = ["测试2群"]
    group_manager = GroupManager(group_list)

    # 启动一个单独的线程来监听停止按钮
    # keyboard_thread = keyboard.Listener(on_press=on_key_press)
    # keyboard_thread.start()

    global stop_requested  # 引用全局停止标志
    while not stop_requested:  # 循环直到停止标志为True
        print("开始处理群聊任务")
        try:
            group_manager.process_group_tasks()
        except Exception as e:
            local_logger.logger.info(f"处理群聊任务时发生错误：{str(e)}")
        time.sleep(1)

def on_key_press(keyboard_event):
    global stop_requested  # 引用全局停止标志
    if keyboard_event.name == '2':
        stop_requested = True  # 请求停止


if __name__ == "__main__":
    print("开始处理群聊任务")
    test_group_manager()
    pass