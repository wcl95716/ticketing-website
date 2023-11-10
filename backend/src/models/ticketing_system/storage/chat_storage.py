# 在 storage.py 中
import json
import os

from models.ticketing_system.types.chat_record import ChatRecord

data_path = "data/work_order_logs"
chat_history_name = "chat_history"

def add_chat_record_to_file(message: ChatRecord):
    folder_path = f"{data_path}/{message.ticket_id}/"
    file_name = f"{folder_path}{chat_history_name}.txt"
    try:
        # 创建工单文件夹（如果不存在）
        os.makedirs(folder_path, exist_ok=True)

        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(message.to_json_str() + '\n')  # 将消息对象转换为JSON字符串并写入文件
        print(f"消息已追加到文件 {file_name}")
    except Exception as e:
        print(f"追加消息时发生错误：{str(e)}")


def get_chat_history_from_file(ticket_id: str) -> list[dict]:
    folder_path = f"{data_path}/{ticket_id}/"
    file_name = f"{folder_path}{chat_history_name}.txt"
    
    chat_history:list[dict] = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                record:dict = json.loads(line.strip())
                print(record)
                chat_history.append(record)  # 去除末尾的换行符并添加到聊天记录列表
    except FileNotFoundError:
        print(f"文件 {file_name} 不存在")
    except Exception as e:
        print(f"读取文件时发生错误：{str(e)}")

    return chat_history