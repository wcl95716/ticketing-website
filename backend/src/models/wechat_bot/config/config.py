
import re


# 创建一个字典，使用ChatKeyWords作为键，分配相应的值
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory, ChatActionsEnum
from models.wechat_bot.types.chat_command_handler import ChatCommandHandler
from models.wechat_bot.utils.chat import get_chat_messages, send_message


robot_name = "AI苏博蒂奇"


tianyi = ChatCommandHandler(robot_name=robot_name , actions=[ChatActionsEnum.WORK_ORDER_CREATE])


def update_robot_name():
    global robot_name
    send_name = "文件传输助手"
    send_message(who = send_name,  message="测试")
    
    chat_message  = get_chat_messages(who=send_name)
    last_message =  chat_message[-1]
    robot_name = last_message[0]
    pass
# tianyi_chat_keywords_dict = {
#     ChatActionsEnum.CREATE_WORK_ORDER:  action_create_work_order,
#     ChatActionsEnum.TEST: action_other
# }


