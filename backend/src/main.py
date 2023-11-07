# 示例用法
import datetime
import random
import time
import uuid
from models.ticketing_system.types.enum_type import Priority, TicketStatus
from models.ticketing_system.types.ticket import Ticket
from database.chatMessage import testChatMessage
from models import ticketing_system
from models.ticketing_system.types.chat_message import ChatMessage
from models.ticketing_system.types import ticket



# ticket = Ticket(1, "问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
# ticket.add_history("支持团队", TicketStatus.IN_PROGRESS, "支持团队", "2023-10-28 10:15:00")
# ticket.add_history("用户A", TicketStatus.COMPLETED, "支持团队", "2023-10-28 11:00:00")

# print(ticket.ticket_id)
# testChatMessage()

def generate_ticket_id():
    # 使用时间戳和随机数生成唯一的 ticket_id
    timestamp = datetime.datetime.now().date()
    ticket_id = f"{timestamp}-{str(uuid.uuid4())}"
    return ticket_id

if __name__ == "__main__":
    # print( ticketing_system.chat_message.getTestChatMessage().to_json() )
    # his_list:list[ChatMessage] = []
    # for i in range(10):
    #     message = ticketing_system.chat_message.getTestChatMessage()
    #     his_list.append(message)
    #     ticketing_system.storage.insert_message(message)

    # for his in his_list:
    #     print(ticketing_system.storage.read_chat_history(his.ticket_id) )
    #     print()

    #ticket.testTicket()
    #ticket = Ticket("问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
    #ticketing_system.ticket_storage.insert_ticket(ticket)
    for tem in ticketing_system.ticket_storage.read_all_tickets():
        print(tem.to_dict())