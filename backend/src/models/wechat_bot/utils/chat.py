import datetime
import os

import poai
import porobot as porobot
import schedule
import hashlib

from PyOfficeRobot.core.WeChatType import WeChat
from PyOfficeRobot.lib.decorator_utils.instruction_url import instruction

from utils import local_logger


wx = WeChat()

import PyOfficeRobot



def get_group_list () -> list[str]:
    group_list = wx.GetSessionList()  # 获取会话列表
    local_logger.logger.info(f" group_list {group_list}")
    return group_list
    pass

def get_chat_messages(who:str) -> list:
    group_list = wx.GetSessionList()  # 获取会话列表
    wx.ChatWith(who)  # 打开`who`聊天窗口
    return wx.GetAllMessage # 获取所有消息
    pass 

def send_message(who:str, message):
    # local_logger.logger.info(who , message)
    PyOfficeRobot.chat.send_message(who=who, message=message)
    pass 


def get_hash_value(my_tuple:tuple) -> str:
    first_two_elements = my_tuple[:2]
    string_representation = ''.join(map(str, first_two_elements))
    hash_object = hashlib.sha256(string_representation.encode())
    hash_value = hash_object.hexdigest()
    return hash_value
    pass





