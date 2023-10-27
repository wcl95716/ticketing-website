from typing import List, Optional

from backend.models.types import Priority, TicketStatus



class TicketHistory:
    def __init__(self, history_id: int, ticket_id: int, operator: str, status: TicketStatus, assigned_to: Optional[str], timestamp: str):
        self.history_id = history_id  # 操作历史ID
        self.ticket_id = ticket_id  # 关联的工单ID
        self.operator = operator  # 操作者
        self.status = status  # 工单状态
        self.assigned_to = assigned_to  # 分配给（可以为 None）
        self.timestamp = timestamp  # 操作时间

class Ticket:
    def __init__(self, ticket_id: int, title: str, created_time: str, status: TicketStatus, priority: Priority,
                 creator: str, assigned_to: Optional[str], ticket_type: str, closed_time: Optional[str]):
        self.ticket_id = ticket_id  # 工单ID
        self.title = title  # 工单标题
        self.created_time = created_time  # 创建时间
        self.status = status  # 状态
        self.priority = priority  # 优先级
        self.creator = creator  # 创建者
        self.assigned_to = assigned_to  # 分配给
        self.ticket_type = ticket_type  # 工单类型
        self.closed_time = closed_time  # 关闭时间
        self.history = []  # 操作历史
        self.max_history_length = 100  # 最大操作历史记录数量

    def add_history(self, operator: str, status: TicketStatus, assigned_to: Optional[str], timestamp: str):
        history_id = len(self.history) + 1
        history_entry = TicketHistory(history_id, self.ticket_id, operator, status, assigned_to, timestamp)
        self.history.append(history_entry)



