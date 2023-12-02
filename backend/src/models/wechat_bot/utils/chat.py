import datetime
import os

import poai
import porobot as porobot
import schedule
import hashlib

from PyOfficeRobot.core.WeChatType import WeChat
from PyOfficeRobot.lib.decorator_utils.instruction_url import instruction

from utils import local_logger
from utils.download_file import download_file_to_folder


wx = WeChat()

import PyOfficeRobot


# def send_message(who: str, message: str) -> None:
#     """
#     给指定人，发送一条消息
#     :param who:
#     :param message:
#     :return:
#     """

#     # 获取会话列表
#     wx.GetSessionList()
#     wx.ChatWith(who)  # 打开`who`聊天窗口
#     # for i in range(10):
#     wx.SendMsg(message, who)  # 向`who`发送消息：你好~


def get_group_list () -> list[str]:
    RollTimes = 1
    def roll_to(RollTimes=RollTimes):
        for i in range(RollTimes):
            wx.SessionList.WheelUp(wheelTimes=3, waitTime=0.1 * i)
        return 0

    rollresult = roll_to()
    group_list = wx.GetSessionList()  # 获取会话列表
    local_logger.logger.info(f" group_list {group_list}")
    return group_list
    pass

def get_chat_messages(who:str) -> list:
    wx.ChatWith(who,RollTimes=0)  # 打开`who`聊天窗口
    return wx.GetAllMessage # 获取所有消息
    pass 

def send_message(who:str, message):
    # local_logger.logger.info(who , message)
    wx.GetSessionList()
    wx.ChatWith(who,RollTimes=0)  # 打开`who`聊天窗口
    # for i in range(10):
    wx.SendMsg(message, who)  # 向`who`发送消息：你好~
    pass 

def send_file_from_url(who:str , file_url:str):
    file_path = download_file_to_folder(file_url)
    """
    发送任意类型的文件
    :param who:
    :param file: 文件路径
    :return:
    """
    wx.ChatWith(who,RollTimes=0)  # 打开聊天窗口
    # wx.SendFiles(file)
    wx.test_SendFiles(filepath=file_path, who=who)  # 添加who参数：雷杰

    pass 


def get_hash_value(my_tuple:tuple) -> str:
    first_two_elements = my_tuple[:2]
    string_representation = ''.join(map(str, first_two_elements))
    hash_object = hashlib.sha256(string_representation.encode())
    hash_value = hash_object.hexdigest()
    return hash_value
    pass


def get_hash_value_ex(my_tuple:list[tuple]) -> str:
    str_tem = ""
    for item in my_tuple:
        first_two_elements = item[:2]
        string_representation = ''.join(map(str, first_two_elements))
        str_tem = str_tem + string_representation
        
    hash_object = hashlib.sha256(str_tem.encode())
    hash_value = hash_object.hexdigest()
    return hash_value
    pass



