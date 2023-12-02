import sys
from models.wechat_bot.utils.chat import get_hash_value, get_hash_value_ex
sys.path.append("./src")
from utils import local_logger

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
        self.is_init = False
        pass
    

    # 从消息中寻找任务
    def find_task(self ,chat_keyword_handler:ChatCommandHandler, chat_messages:list[tuple] = [] ) -> []:
        # chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        message_id_pivot = self.current_chat_message_id
        local_logger.logger.info(f"message_id_pivot {self.group_id}  {message_id_pivot} ")
        # 使用切片获取最后十条消息，如果不够十条，就获取全部消息
        # 计算列表的长度
        num_messages = len(chat_messages)

        # 设置要取的最后十条消息的数量
        num_to_keep = 10
        last_ten_messages = chat_messages[-num_to_keep:] if num_messages >= num_to_keep else chat_messages

        result_task = []
        some_messages = []
        for message in last_ten_messages:
            some_messages.append(message)
            if len(some_messages) > 3:
                some_messages.pop(0)
            hash_value = get_hash_value(message)
            # hash_value = get_hash_value_ex(messages)
            local_logger.logger.info(f"chat_message {hash_value}  {message} ")   
            self.current_chat_message_id = hash_value
            if message_id_pivot == hash_value :
                # 清空任务队列
                result_task.clear()
                continue
                # break
            action = chat_keyword_handler.search(message[1])
            if action:
                result:callable = ChatActionFunctionFactory.get_action_function(action) #(self.group_id,message)
                result_task.append((result,self.group_id,message))
        local_logger.logger.info(f" current_chat_message_id = {self.current_chat_message_id} result_task= {result_task} ")
        
        return result_task
        pass
    
    pass 



def test():
    print("test")
    group_chat = GroupChatManager(group_id="测试群1")
    messages = [('Panda', '@AI苏博蒂奇创建工单', '4211805484920'), ('Panda', '@AI苏博蒂1奇 创建工单123123', '4211805484920')]
    
    chat_keyword_handler = ChatCommandHandler(robot_name=config.robot_name, actions=[ChatActionsEnum.WORK_ORDER_CREATE])
    tasks = group_chat.find_task(chat_keyword_handler , messages)
    # print("tasks ",group_chat.tasks )
    
    for task in tasks:
        print("task : ",task)
    pass

if __name__ == "__main__":
    test()
    pass