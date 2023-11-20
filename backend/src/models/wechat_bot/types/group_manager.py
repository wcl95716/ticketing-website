import sys

sys.path.append("./src")

from collections import deque
# import PyOfficeRobot
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory, ChatActionsEnum
from models.wechat_bot.types.chat_command_handler import ChatCommandHandler

# from models.wechat_bot.utils.chat import get_chat_messages

from models.wechat_bot.config import config

class GroupChatManager:
    
    def __init__ (self, group_id: str, robot_name: str, actions: []):
        self.group_id = group_id
        self.robot_name = robot_name
        self.actions = actions
        self.current_chat_message_id = 0
        
        self.chat_messages:list[tuple] = []
        self.tasks = deque()  # 创建一个空的任务双端队列
        pass
    
    def send_chat_message(self, message: str):
        # PyOfficeRobot.chat.send_message(who=self.group_id, message=message)
        pass
    
    def process_next_task(self):
        if self.tasks:
            next_task = self.tasks.popleft()  # 获取并删除队列的第一个任务
            # 执行任务的操作逻辑
            print(f"处理任务：{next_task}")
            self.send_chat_message(next_task)
        else:
            print("没有待处理的任务")
    
    def update_chat_message(self):
        # self.chat_messages = get_chat_messages(self.group_id)
        pass
    
    def find_task(self):
        chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        for message in self.chat_messages:
            action = chat_keyword_handler.search(message[1])
            if action:
                result = ChatActionFunctionFactory.get_action_function(action)(message)
                self.tasks.append((result,message))
        pass
    
    pass 


class GroupManager:
    
    def __init__(self, group_list: list[GroupChatManager]):
        self.group_list = group_list
        pass
    
    pass 



def test():
    group_chat = GroupChatManager(group_id="测试群", robot_name=config.robot_name, actions=[ChatActionsEnum.CREATE_WORK_ORDER])
    messages = [('Panda', '@机器人名 创建工单', '4211805484920'), ('Panda', '@机器人名 创建工单', '4211805484920')]
    group_chat.chat_messages = messages
    group_chat.find_task()
    print(group_chat.tasks )
    pass

if __name__ == "__main__":
    test()
    pass