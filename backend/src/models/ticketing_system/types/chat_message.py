import json
import random
import string
from typing import List, Optional
from enum import Enum

from models.ticketing_system.types.enum_type import MessageType


class ChatMessage:
    def __init__(self, message_id: int, ticket_id: int, sender: str, content: str, message_time: str, message_type: MessageType):
        self.message_id = message_id  # 消息ID
        self.ticket_id = ticket_id  # 关联的工单ID
        self.sender = sender  # 发送者
        self.content = content  # 消息内容
        self.message_time = message_time  # 消息时间
        self.message_type = message_type  # 消息类型

    def to_json(self):
        # 将 MessageType 转换为字符串
        message_type_str = self.message_type.value if self.message_type else ""
        
        # 创建一个字典来表示对象
        data = {
            "message_id": self.message_id,
            "ticket_id": self.ticket_id,
            "sender": self.sender,
            "content": self.content,
            "message_time": self.message_time,
            "message_type": message_type_str
        }
        
        return json.dumps(data,ensure_ascii=False)
    
    @classmethod
    def from_json(cls, json_string):
        data = json.loads(json_string)
        return cls(**data)


# 创建main 测试
def testChatMessage():
    chatMessage = ChatMessage(1, 2, "张三", "你好", "2021-10-28 10:00:00", MessageType.TEXT)
    print(chatMessage.to_json())
    chatMessage2 = ChatMessage.from_json(chatMessage.to_json())
    print(chatMessage2.to_json())


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

    chatMessage = ChatMessage(message_id, ticket_id, sender, content, message_time, message_type)
    return chatMessage