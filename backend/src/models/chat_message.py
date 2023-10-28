from typing import List, Optional
from enum import Enum

from src.models.types import MessageType
class ChatMessage:
    def __init__(self, message_id: int, ticket_id: int, sender: str, content: str, message_time: str, message_type: MessageType):
        self.message_id = message_id  # 消息ID
        self.ticket_id = ticket_id  # 关联的工单ID
        self.sender = sender  # 发送者
        self.content = content  # 消息内容
        self.message_time = message_time  # 消息时间
        self.message_type = message_type  # 消息类型


