import json
import random
import string
from typing import List, Optional
from enum import Enum

from models.ticketing_system.types.enum_type import ChatPriority, MessageType


class ChatRecord:
    def __init__(self, 
                message_id: int, 
                ticket_id: int,
                sender: str,
                content: str,
                message_time: str,
                message_type: MessageType,
                file_id: str = None,
                file_url: str = None,
                chat_profile: ChatPriority = None, # 聊天级别
                avatar_url: dict = None # 用户信息 传入的
                ):
        self.message_id = message_id  # 消息ID
        self.ticket_id = ticket_id  # 关联的工单ID
        self.sender = sender  # 发送者
        self.content = content  # 消息内容
        self.message_time = message_time  # 消息时间
        self.message_type = message_type  # 消息类型
        self.file_id = file_id
        self.file_url = file_url # 文件 
        self.chat_profile = chat_profile if chat_profile != None  else ChatPriority.LOW # 聊天级别 如果为None 则为普通聊天
        self.avatar_url = avatar_url # 用户信息 传入的
        
        

    def to_json(self):
        # 将 MessageType 转换为字符串
        # 创建一个字典来表示对象
        data = {
            "message_id": self.message_id,
            "ticket_id": self.ticket_id,
            "sender": self.sender,
            "content": self.content,
            "message_time": self.message_time,
            "message_type": self.message_type.value,
            "file_id": self.file_id,
            "file_url": self.file_url,
            "chat_profile": self.chat_profile.value, # 聊天级别
            "avatar_url": self.avatar_url,
        }
        return data
    
    def to_json_str(self):
        return json.dumps(self.to_json(),ensure_ascii=False)
    
    @classmethod
    def from_json_str(cls, json_string):
        data = json.loads(json_string)
        return cls.from_json(data)
    
    @classmethod
    def from_json(cls, json_data):
        json_data["message_type"] = MessageType(json_data["message_type"])
        json_data["chat_profile"] = ChatPriority(json_data["chat_profile"])
        return cls(**json_data)

# 创建main 测试
def testChatMessage():
    chatMessage = ChatRecord(1, 2, "张三", "你好", "2021-10-28 10:00:00", MessageType.TEXT)
    chatMessage.ticket_id = "2023-11-10-5a994e69-7a49-4f91-bd2f-d1bec831daa9"
    return chatMessage


def generate_random_chinese(length):
    chinese_characters = [chr(random.randint(0x4e00, 0x9fff)) for _ in range(length)]
    return ''.join(chinese_characters)

def getTestChatMessage():
    # 生成随机的消息ID、工单ID、发送者、消息内容和消息时间
    message_id = random.randint(1, 1000)
    ticket_id = random.randint(1, 5)
    sender = generate_random_chinese(5)  # 随机生成5个中文字符的发送者名字
    content = generate_random_chinese(10)  # 随机生成20个中文字符的消息内容

    message_time = "2021-10-28 10:00:00"  # 固定消息时间
    message_type = random.choice(list(MessageType))  # 随机选择消息类型

    chatMessage = ChatRecord(message_id, ticket_id, sender, content, message_time, message_type)
    chatMessage.ticket_id = "001"
    return chatMessage