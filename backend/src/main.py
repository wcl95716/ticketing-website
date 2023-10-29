# 示例用法
from database.chatMessage import testChatMessage
from models.ticket import Ticket
from models.types import Priority, TicketStatus


ticket = Ticket(1, "问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
ticket.add_history("支持团队", TicketStatus.IN_PROGRESS, "支持团队", "2023-10-28 10:15:00")
ticket.add_history("用户A", TicketStatus.COMPLETED, "支持团队", "2023-10-28 11:00:00")

print(ticket.ticket_id)
testChatMessage()