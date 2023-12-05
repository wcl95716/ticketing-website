

from datetime import date
import datetime
from utils import local_logger


from models.wechat_bot.utils.chat import get_chat_messages, get_group_list, send_message 



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
        print("GroupManager init")
        print(f"robot_name={robot_name}")
        self.group_list = group_list
        self.group_manager_list:list[GroupChatManager] = []
        for group_id in self.group_list:
            group = GroupChatManager(group_id=group_id)
            self.group_manager_list.append(group)
        self.robot_name = robot_name
        self.actions = actions
        self.is_init = False
        
        pass
    
    
    def group_init_send_message(self,group:GroupChatManager):
        #for group in self.group_manager_list:
        if group.is_init == False:
            send_message(group.group_id,"机器人已启动 : " + date.today().strftime("%Y-%m-%d") )
            pass 
        pass
    
    def fix_group_task(self,group_id,tasks):
        for task in tasks:
            local_logger.logger.info(f" fix tasks {task}")
            task_result = task[0](task[1],task[2],task[3])
            send_message(group_id,task_result[1])
            pass 
        pass
    
    # def process_group_tasks(self,process_group_list:list[str] = [] ):
    #     chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
    #     local_logger.logger.info(f"process_group_tasks {process_group_list} ")
    #     for group in self.group_manager_list:

    #         # 如果不在处理的群聊列表中，则跳过
    #         if not any(prefix.startswith(group.group_id) for prefix in process_group_list):
    #             local_logger.logger.info(f"跳过群聊 {group.group_id}")
    #             continue
    #         # 初始化发送消息
    #         self.group_init_send_message(group=group)
            
    #         # true_prefix = next((prefix for prefix in process_group_list if prefix.startswith(group.group_id)), None)
            
    #         group_id = group.group_id
    #         local_logger.logger.info(f"处理群聊 {group_id}  ")
    #         # chat_messages = []
    #         chat_messages = get_chat_messages(group_id)
    #         tasks:[] = group.find_task(chat_keyword_handler,chat_messages)
    #         local_logger.logger.info(f" find tasks {tasks}")
    #         if self.is_init and group.is_init :
    #             self.fix_group_task(group.group_id,tasks)
    #         group.is_init = True
    #     self.is_init = True
    #     pass
    
    def process_one_group_tasks(self, process_group:str ):
        chat_keyword_handler = ChatCommandHandler(robot_name=self.robot_name, actions=self.actions)
        local_logger.logger.info(f"process_group_tasks {process_group} ")
        for group in self.group_manager_list:
            if process_group.startswith(group.group_id) == False:
                continue
            
            
            group_id = process_group
            if group.is_init == False:
                send_message(group.group_id,"机器人已启动 : " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),)
                group_id = group.group_id
                pass 

            chat_messages = get_chat_messages(group_id)
            local_logger.logger.info(f"处理群聊 {group_id}  ")
            tasks:[] = group.find_task(chat_keyword_handler,chat_messages)
            local_logger.logger.info(f" find tasks {tasks}")
            if self.is_init and group.is_init :
                self.fix_group_task(group.group_id,tasks)
            group.is_init = True
        self.is_init = True
        pass
    
    
    pass 

