import sys
sys.path.append("./src")


# 示例用法
import datetime
import random
import time
import uuid
from models.ticketing_system.types.chat_record import ChatRecord
from models.ticketing_system.types.enum_type import Priority, TicketStatus
from models import ticketing_system

import werkzeug
from service import flask_service

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
# 配置文件上传目录和允许的文件扩展名
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    # print( ticketing_system.chat_message.getTestChatMessage().to_json() )
    # his_list:list[ChatRecord] = []
    # for i in range(10):
    #     message = ticketing_system.chat_record.getTestChatMessage()
    #     # his_list.append(message)
    #     ticketing_system.chat_api.add_chat_record(message.to_json())

    # for his in his_list:
    #     print(ticketing_system.chat_api.get_chat_history(his.ticket_id) )
    #     print()
    #flask_service.get_app().run(host='0.0.0.0',port=8001)
    #ticket.testTicket()
    # ticket = ("问题报告", "2023-10-28 10:00:00", TicketStatus.NEW, Priority.HIGHEST, "用户A", None, "报告问题", None)
    
    # ticketing_system.ticket_api.add_ticket()
    file_name = "4abf3ecb36d843b6be12d2daefe5fc3f_IMG_0357.jpeg"
    print(allowed_file(file_name))
    
    pass 