import datetime
import os

import poai
import porobot as porobot
import schedule

from PyOfficeRobot.core.WeChatType import WeChat
from PyOfficeRobot.lib.decorator_utils.instruction_url import instruction

wx = WeChat()


# @act_info(ACT_TYPE.MESSAGE)
# @instruction
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


@instruction
def group_chat_by_keywords(who: str, keywords: str):
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



