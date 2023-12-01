import os
import json
from models.ticketing_system.utils import ticket_storage

from models.ticketing_system.types.ticket_record import TicketFilter, TicketRecord, getTestTicket

def add_ticket(ticket: dict) -> TicketRecord:
    ticketRecord:TicketRecord = TicketRecord.from_dict(ticket)
    ticket_storage.save_ticket_to_file(ticketRecord)
    return ticketRecord
    pass

def update_ticket(ticket: dict):
    ticketRecord:TicketRecord = TicketRecord.from_dict(ticket)
    ticket_storage.update_ticket_record_in_file(ticketRecord)
    

def get_ticket(ticket_id: str) -> TicketRecord :
    result = ticket_storage.get_ticket_record_from_file(ticket_id)
    return result
    pass

def get_all_tickets() -> list[TicketRecord]:
    result:list[TicketRecord] = ticket_storage.get_all_ticket_record_from_files()
    # result 根据 TicketRecord 的 created_time 排序
    result.sort(key=lambda x:x.created_time, reverse=True)
    return result
    pass 

def delete_ticket(ticket_id: str):
    ticket_storage.delete_ticket_record(ticket_id)
    
def get_test_ticket() -> TicketRecord:
    return getTestTicket().to_dict()
    pass

def get_ticket_filter(ticket_filter_dict:dict):
    ticket_filter = TicketFilter.from_dict(ticket_filter_dict)
    
    ticket_reord_list:list[TicketRecord] = get_all_tickets()
    
    result:list[TicketRecord] = ticket_filter.get_filter_condition_ticket(ticket_reord_list)
    return result
    
    pass



