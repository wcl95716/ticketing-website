import sys
import os
# 获取项目的根目录路径
project_root = os.path.dirname(os.path.abspath(__file__))
# 将项目的根目录添加到 sys.path
sys.path.insert(0, project_root)

# 示例用法
from src.models.ticket import Ticket
from src.models.types import Priority, TicketStatus


ticket = Ticket(1, "问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
ticket.add_history("支持团队", TicketStatus.IN_PROGRESS, "支持团队", "2023-10-28 10:15:00")
ticket.add_history("用户A", TicketStatus.COMPLETED, "支持团队", "2023-10-28 11:00:00")

print(ticket.ticket_id)