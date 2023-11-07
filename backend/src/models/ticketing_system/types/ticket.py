import datetime
import random
import time
from typing import List, Optional

from models.ticketing_system.types.enum_type import Priority, TicketStatus
import uuid

# class TicketHistory:
#     def __init__(self, history_id: int, ticket_id: int, operator: str, status: TicketStatus, assigned_to: Optional[str], timestamp: str):
#         self.history_id = history_id  # 操作历史ID
#         self.ticket_id = ticket_id  # 关联的工单ID
#         self.operator = operator  # 操作者
#         self.status = status  # 工单状态
#         self.assigned_to = assigned_to  # 分配给（可以为 None）
#         self.timestamp = timestamp  # 操作时间

class Ticket:

    def __init__(self, title: str, created_time: str, status: TicketStatus, priority: Priority,
                 creator: str, assigned_to: Optional[str], ticket_type: str, closed_time: Optional[str]):
        self.ticket_id = Ticket.generate_ticket_id()
        self.title = title  # 工单标题
        self.created_time = created_time  # 创建时间
        self.status = status  # 状态
        self.priority = priority  # 优先级
        self.creator = creator  # 创建者
        self.assigned_to = assigned_to  # 分配给
        self.ticket_type = ticket_type  # 工单类型
        self.closed_time = closed_time  # 关闭时间

    @classmethod
    def generate_ticket_id(cls):
        # 使用时间戳和随机数生成唯一的 ticket_id
        timestamp = datetime.datetime.now().date()
        ticket_id = f"{timestamp}-{str(uuid.uuid4())}"
        return ticket_id
        



