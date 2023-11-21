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
        
        self.tasks: deque[str]= deque()  # 创建一个空的任务双端队列
        pass
    
    
    def process_next_task(self) -> str:
        if self.tasks:
            next_task:str = self.tasks.popleft()  # 获取并删除队列的第一个任务
            return next_task
        else:
            print("没有待处理的任务")
    
    def update_chat_message(self):
        # self.chat_messages = get_chat_messages(self.group_id)
        pass
    
    # 从消息中寻找任务
    def find_task(self , chat_messages:list[tuple] = []):
        chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        message_id_pivot = self.current_chat_message_id
        for message in chat_messages:
            action = chat_keyword_handler.search(message[1])
            if action:
                if message_id_pivot == message[2] :
                    # 清空任务队列
                    self.tasks.clear()
                    break
                
                result:str = ChatActionFunctionFactory.get_action_function(action)(message)
                self.tasks.append(result)
                self.current_chat_message_id = message[2]

        pass
    
    pass 


class GroupManager:
    def __init__(self, group_list: list[GroupChatManager]):
        self.group_list = group_list
        pass
    
    pass 



def test():
    group_chat = GroupChatManager(group_id="测试群", robot_name=config.robot_name, actions=[ChatActionsEnum.WORK_ORDER_CREATE])
    messages = [('Panda', '@机器人名 创建工单', '4211805484920'), ('Panda', '@机器人名 创建工单123123', '4211805484920')]
    group_chat.find_task(messages)
    print("tasks ",group_chat.tasks )
    pass

if __name__ == "__main__":
    test()
    pass