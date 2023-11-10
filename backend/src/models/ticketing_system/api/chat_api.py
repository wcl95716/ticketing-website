# 在 storage.py 中
import os
from models.ticketing_system.storage import chat_storage

from models.ticketing_system.types.chat_record import ChatRecord


def add_chat_record(chat_record_json: dict):
    chat_record = ChatRecord.from_json(chat_record_json)
    print(chat_record.to_json())
    chat_storage.add_chat_record_to_file(chat_record)
    pass



def get_chat_history(ticket_id: str) -> list[dict]:
    chats:list[dict] = chat_storage.get_chat_history_from_file(ticket_id)
    return chats
    pass