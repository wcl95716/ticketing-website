import datetime
import json
import random
import time
from typing import List, Optional

from models.ticketing_system.types.enum_type import Priority, TicketStatus
import uuid

class TicketRecord:

    def __init__(self, title: str, created_time: str, status: TicketStatus, priority: Priority,
                 creator: str, assigned_to: Optional[str], ticket_type: str, closed_time: Optional[str]):
        self.ticket_id = TicketRecord.generate_ticket_id()
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
    
    def to_dict(self):
        return {
            "ticket_id": self.ticket_id,
            "title": self.title,
            "created_time": self.created_time,
            "status": self.status.value,  # 使用枚举值
            "priority": self.priority.value,  # 使用枚举值
            "creator": self.creator,
            "assigned_to": self.assigned_to,
            "ticket_type": self.ticket_type,
            "closed_time": self.closed_time
        }
    
    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
    
    @classmethod
    def from_dict(cls, ticket_data):
        ticket = cls(
            title=ticket_data["title"],
            created_time=ticket_data["created_time"],
            status=TicketStatus(ticket_data["status"]),
            priority=Priority(ticket_data["priority"]),
            creator=ticket_data["creator"],
            assigned_to=ticket_data["assigned_to"],
            ticket_type=ticket_data["ticket_type"],
            closed_time=ticket_data["closed_time"]
        )
        ticket.ticket_id = ticket_data["ticket_id"]
        return ticket
    
    @classmethod
    def from_json(cls, json_string):
        ticket_data = json.loads(json_string)
        return TicketRecord.from_dict(ticket_data)
    

# 创建一个测试数据


        

def testTicket():
    ticket = Ticket("问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
    print(ticket.to_json())
    ticket2 = Ticket.from_json(ticket.to_json())
    print(ticket2.to_json())