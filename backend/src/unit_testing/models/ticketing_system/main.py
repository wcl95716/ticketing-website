import sys

sys.path.append("./src")
from models.ticketing_system.utils.user_storage import add_user_to_file, get_users_to_file

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
    
    
if __name__ == "__main__":
    
    test_add_user()
    pass