# 示例用法
from models.ticketing_system.types.enum_type import Priority, TicketStatus
from models.ticketing_system.types.ticket import Ticket
from database.chatMessage import testChatMessage
from models import ticketing_system
from models.ticketing_system.types.chat_message import ChatMessage



# ticket = Ticket(1, "问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
# ticket.add_history("支持团队", TicketStatus.IN_PROGRESS, "支持团队", "2023-10-28 10:15:00")
# ticket.add_history("用户A", TicketStatus.COMPLETED, "支持团队", "2023-10-28 11:00:00")

# print(ticket.ticket_id)
# testChatMessage()

if __name__ == "__main__":
    # print( ticketing_system.chat_message.getTestChatMessage().to_json() )
    his_list:list[ChatMessage] = []
    for i in range(10):
        message = ticketing_system.chat_message.getTestChatMessage()
        his_list.append(message)
        ticketing_system.storage.insert_message(message)

    for his in his_list:
        print(ticketing_system.storage.read_chat_history(his.ticket_id) )
        print()