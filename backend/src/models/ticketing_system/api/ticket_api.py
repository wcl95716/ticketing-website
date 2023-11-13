import os
import json
from models.ticketing_system.storage import ticket_storage

from models.ticketing_system.types.ticket_record import TicketRecord, getTestTicket

def add_ticket(ticket: dict):
    ticketRecord:TicketRecord = TicketRecord.from_dict(ticket)
    ticket_storage.save_ticket_to_file(ticketRecord)
    pass

def update_ticket_record_in_file(ticket: dict):
    ticketRecord:TicketRecord = TicketRecord.from_dict(ticket)
    ticket_storage.update_ticket_record_in_file(ticketRecord)
    

def get_ticket(ticket_id: str) -> TicketRecord :
    result = ticket_storage.get_ticket_record_from_file(ticket_id)
    return result
    pass


def get_all_tickets() -> list[TicketRecord]:
    result = ticket_storage.get_all_ticket_record_from_files()
    return result
    pass 

def delete_ticket(ticket_id: str):
    ticket_storage.delete_ticket_record(ticket_id)
    

    
def get_test_ticket() -> TicketRecord:
    return getTestTicket().to_dict()
    pass
    