import datetime
import json
import random
import time
from typing import List, Optional

from models.ticketing_system.types.enum_type import Priority, TicketStatus
import uuid

class TicketRecord:

    def __init__(self, title: str, created_time: str, status: TicketStatus, priority: Priority,
                 creator: str, assigned_to: Optional[str],
                closed_time: Optional[str],
                ticket_type: str = None,
                ):
        self.ticket_id = TicketRecord.generate_ticket_id()
        self.title = title  # 工单标题
        self.created_time = created_time  # 创建时间
        self.status = status  # 状态
        self.priority = priority  # 优先级
        self.creator = creator  # 创建者
        self.assigned_to = assigned_to  # 分配给
        self.ticket_type = ticket_type  # 工单类型
        self.closed_time = closed_time  # 关闭时间
        self.update_time = created_time # 更新时间

    @classmethod
    def generate_ticket_id(cls):
        # 使用时间戳和随机数生成唯一的 ticket_id
        timestamp = datetime.datetime.now().date()
        time_id = int(time.time() * 1000 * 1000)
        last_ten_digits = time_id % (10**13)
        ticket_id = f"{timestamp}-{last_ten_digits}"
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
            "closed_time": self.closed_time,
            "update_time": self.update_time,
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
        ticket.ticket_id = ticket_data.get("ticket_id") or cls.generate_ticket_id()
        ticket.update_time =  ticket_data.get("created_time") or ticket_data["update_time"],
        return ticket
    
    @classmethod
    def from_json(cls, json_string):
        ticket_data = json.loads(json_string)
        return TicketRecord.from_dict(ticket_data)


def get_datetime(date_string: str ):
    try:
        # 尝试解析第一种格式
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            # 尝试解析第二种格式
            return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            # 如果两种格式都无法解析，可以返回None或引发异常，具体取决于你的需求
            return None


class TicketFilter:
    def __init__(self, search_criteria:str = None , status:TicketStatus = None ,start_date:str = None , end_date:str = None):
        self.search_criteria = search_criteria
        self.status = status
        self.start_date = start_date
        self.end_date = end_date
        pass 
    
    def to_dict(self):
        return {
            "search_criteria": self.search_criteria,
            "status": self.status.value if self.status != None else None,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }
    
    @classmethod
    def from_dict(cls, json_data: dict ):
        json_data["status"] = TicketStatus(json_data["status"]) if json_data["status"] != None else None
        return cls(**json_data)
        pass
    
    def get_filter_condition_ticket(self , list_ticket:List[TicketRecord]) -> List[TicketRecord] :
        # 根据条件筛选出符合条件的工单
        return self.get_filter_condition_ticket_id(list_ticket)
        pass

    def get_filter_condition_ticket_id(self ,  list_ticket:List[TicketRecord]) -> List[TicketRecord]:
        # 根据条件筛选出符合条件的工单ID
        result_list:List[TicketRecord]  = []
        for ticket in list_ticket:
            # self.start_date <= ticket.created_time <= self.end_date: 
            # 它们都是字符串 帮我转换成时间
            # 将字符串日期解析为 datetime 对象
            start_date = get_datetime(self.start_date)# datetime.datetime.strptime(self.start_date, "%Y-%m-%d %H:%M:%S")
            end_date = get_datetime(self.end_date) #datetime.datetime.strptime(self.end_date, "%Y-%m-%d %H:%M:%S")
            created_time = get_datetime(self.created_time) # datetime.datetime.strptime(ticket.created_time, "%Y-%m-%d %H:%M:%S")
            if self.search_criteria in ticket.ticket_id:
                result_list.append(ticket)
            elif self.search_criteria in ticket.title:
                result_list.append(ticket)
            elif self.search_criteria in ticket.assigned_to:
                result_list.append(ticket)
            elif self.status == ticket.status and self.status != None:
                result_list.append(ticket)
                pass 
            elif start_date <= created_time <= end_date:
                result_list.append(ticket)
                pass
        return result_list

    
    pass 




# 创建一个测试数据
def testTicket():
    ticket = TicketRecord("问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
    print(ticket.to_json())
    ticket2 = TicketRecord.from_json(ticket.to_json())
    print(ticket2.to_json())
    
    
def generate_random_chinese(length):
    chinese_characters = [chr(random.randint(0x4e00, 0x9fff)) for _ in range(length)]
    return ''.join(chinese_characters)

#创建一个随机的testTicket 数据
def getTestTicket():
    sender = generate_random_chinese(5)  # 随机生成5个中文字符的发送者名字
    ticket = TicketRecord(
        "问题报告", 
        datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        TicketStatus.NEW,
        Priority.HIGHEST,
        sender,
        None,
        "报告问题",
        None)
    return ticket
    pass 


# 创建一个根据条件搜索 TicketRecord 的class
# 用于在 ticket_storage.py 中的 search_ticket_record_from_files 方法中使用
# 条件为: creator/ticket_id/