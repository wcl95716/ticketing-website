import sys

sys.path.append("./src")
from models.ticketing_system.storage.user_storage import add_user_to_file

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

    user_name = user_profile.get_test_user()
    add_user_to_file(user_name)
        

if __name__ == "__main__":
    
    test_add_user()
    pass