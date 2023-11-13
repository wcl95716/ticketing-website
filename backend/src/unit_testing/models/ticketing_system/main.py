import sys
sys.path.append("./src")


from models.ticketing_system.types import chat_record,ticket_record
from models.ticketing_system.types.enum_type import Priority, TicketStatus
from models import ticketing_system

from service import flask_service


if __name__ == "__main__":
    
    tick_tem = ticket_record.getTestTicket()
    print(tick_tem.to_dict())
    tick_tem.ticket_id = None
    tick_tem2 = ticket_record.TicketRecord.from_dict(tick_tem.to_dict())
    print(tick_tem2.to_dict())
    pass