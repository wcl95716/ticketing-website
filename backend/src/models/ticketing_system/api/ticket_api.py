import os
import json
from models.ticketing_system.storage import ticket_storage

from models.ticketing_system.types.ticket_record import TicketRecord

def add_ticket(ticket: TicketRecord):
    ticket_storage.save_ticket_to_file(ticket)
    pass

def get_ticket(ticket_id: str) -> TicketRecord :
    result = ticket_storage.get_ticket_record_from_file(ticket_id)
    return result
    pass


def get_all_tickets() -> list[TicketRecord]:
    result = ticket_storage.get_all_ticket_record_from_files()
    return result
    pass 