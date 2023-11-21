
import re


# 创建一个字典，使用ChatKeyWords作为键，分配相应的值
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory, ChatActionsEnum
from models.wechat_bot.types.chat_command_handler import ChatCommandHandler


robot_name = "机器人名"


tianyi = ChatCommandHandler(robot_name=robot_name , actions=[ChatActionsEnum.WORK_ORDER_CREATE])


# tianyi_chat_keywords_dict = {
#     ChatActionsEnum.CREATE_WORK_ORDER:  action_create_work_order,
#     ChatActionsEnum.TEST: action_other
# }


