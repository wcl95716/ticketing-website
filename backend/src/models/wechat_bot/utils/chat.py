import datetime
import os

import poai
import porobot as porobot
import schedule

from PyOfficeRobot.core.WeChatType import WeChat
from PyOfficeRobot.lib.decorator_utils.instruction_url import instruction

wx = WeChat()



def get_chat_messages(who:str) -> list:
    wx.GetSessionList()  # 获取会话列表
    wx.ChatWith(who)  # 打开`who`聊天窗口
    return wx.GetAllMessage()  # 获取所有消息
    pass 

# def is_find_customer_service(messages , customer_service_names = []):
#     result = None
#     # 查看messages 中 是否有@客服 的消息
#     for message in messages:
#         # message[1] 为消息内容
#         # 查找 message[1] 中是否有 @customer_service_names 中的内容
#         print(message , customer_service_names)
#         if "客服回复" in message[1]:
#             result = None
#         for customer_service_name in customer_service_names:
#             if "@"+customer_service_name in message[1]:
#                 result = message
#     return result
#     pass 

def chat_find_task(keywords: dict , messages: list):
    result_tasks:[] = []
    for message in messages:
        for keyword, value in keywords.items():
            if value in message:
                result_tasks.append((message, keyword))
    pass 

def group_chat_by_keywords(who: str, keywords: dict):
    wx.GetSessionList()  # 获取会话列表
    wx.ChatWith(who)  # 打开`who`聊天窗口
    chat_messages =  wx.GetAllMessage()  # 获取所有消息
    temp_msg = ''

    try:
        friend_name, receive_msg = wx.GetAllMessage[-1][0], wx.GetAllMessage[-1][1]  # 获取朋友的名字、发送的信息
        if (friend_name == who) & (receive_msg != temp_msg) & (receive_msg in keywords.keys()):
            """
            条件：
            朋友名字正确:(friend_name == who)
            不是上次的对话:(receive_msg != temp_msg)
            对方内容在自己的预设里:(receive_msg in kv.keys())
            """

            temp_msg = receive_msg
            wx.SendMsg(keywords[receive_msg], who)  # 向`who`发送消息
    except:
        pass



