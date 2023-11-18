# 在 storage.py 中
import os
from cgi import FieldStorage
from models.ticketing_system.storage import chat_storage

from models.ticketing_system.types.chat_record import ChatRecord
from utils import local_logger


def add_chat_record(chat_record_json: dict):

    chat_record = ChatRecord.from_json(chat_record_json)
    chat_storage.add_chat_record_to_file(chat_record)

    pass


def get_chat_history(ticket_id: str) -> list[dict]:
    chats:list[dict] = chat_storage.get_chat_history_from_file(ticket_id)
    for chat in chats:
        try:
            chat["file_url"] = "http://47.116.201.99:8001/test/uploads/"+ chat["file_id"]
        except Exception as e:
            print(f"获取聊天记录时发生错误：{str(e)}")
            chat["file_url"] = ""
    return chats
    past
    
def upload_file(file: FieldStorage):
    return chat_storage.upload_file(file)
    pass

def get_file(file_name: str):
    return chat_storage.get_file_path(file_name)
    pass






