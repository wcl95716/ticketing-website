import sys

sys.path.append("./src")

from collections import deque
# import PyOfficeRobot
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory, ChatActionsEnum
from models.wechat_bot.types.chat_command_handler import ChatCommandHandler

# from models.wechat_bot.utils.chat import get_chat_messages

from models.wechat_bot.config import config

class GroupChatManager:
    
    def __init__ (self, group_id: str):
        self.group_id = group_id
        self.current_chat_message_id = 0
        pass
    

    # 从消息中寻找任务
    def find_task(self ,chat_keyword_handler:ChatCommandHandler, chat_messages:list[tuple] = [] ) -> []:
        # chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        message_id_pivot = self.current_chat_message_id
        result_task = []
        for message in chat_messages:
            action = chat_keyword_handler.search(message[1])
            if action:
                if message_id_pivot == message[2] :
                    # 清空任务队列
                    result_task.clear()
                    break
                
                result:str = ChatActionFunctionFactory.get_action_function(action)(self.group_id,message)
                result_task.append(result)
                self.current_chat_message_id = message[2]
                
        return result_task
        pass
    
    pass 



def test():
    print("test")
    group_chat = GroupChatManager(group_id="测试群1")
    messages = [('Panda', '@机器人名 创建工单', '4211805484920'), ('Panda', '@机器人名 创建工单123123', '4211805484920')]
    
    chat_keyword_handler = ChatCommandHandler(robot_name=config.robot_name, actions=[ChatActionsEnum.WORK_ORDER_CREATE])
    tasks = group_chat.find_task(chat_keyword_handler , messages)
    # print("tasks ",group_chat.tasks )
    
    for task in tasks:
        print("task : ",task)
    pass

if __name__ == "__main__":
    test()
    pass