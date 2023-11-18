import sys

sys.path.append("./src")
from models.ticketing_system.storage.user_storage import add_user_to_file, get_users_to_file

from models.ticketing_system.types import user_profile, chat_record,ticket_record
from models.ticketing_system.types.enum_type import Priority, TicketStatus
from models import ticketing_system

from service import flask_service


def test():
    tick_tem = ticket_record.getTestTicket()
    print(tick_tem.to_dict())
    tick_tem.ticket_id = None
    tick_tem2 = ticket_record.TicketRecord.from_dict(tick_tem.to_dict())
    print(tick_tem2.to_dict())
    
    
def test_add_user():
    for i in range(10):
        user_name = user_profile.get_test_user()
        add_user_to_file(user_name)
        users = get_users_to_file()
        
        print(users)
    
def test_ticket_filter():
    ticket_filter = ticket_record.TicketFilter()
    
    print(ticket_filter.to_dict())
    
    tes2 = ticket_record.TicketFilter.from_dict(ticket_filter.to_dict())
    
    print(tes2.to_dict())
    
    pass 

if __name__ == "__main__":
    
    test_ticket_filter()
    pass