# 在 storage.py 中
from werkzeug.utils import secure_filename
import json
import os

from models.ticketing_system.types.chat_record import ChatRecord
from werkzeug.datastructures import FileStorage
import uuid

from utils import local_logger

data_path = "data/work_order_logs"
chat_history_name = "chat_history"

file_data_path = "data/chat_files"

def add_chat_record_to_file(message: ChatRecord):
    folder_path = f"{data_path}/{message.ticket_id}/"
    file_name = f"{folder_path}{chat_history_name}.txt"
    try:
        # 创建工单文件夹（如果不存在）
        os.makedirs(folder_path, exist_ok=True)

        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(message.to_json_str() + '\n')  # 将消息对象转换为JSON字符串并写入文件
        local_logger.logger.info(f"消息已追加到文件 {file_name}")
    except Exception as e:
        local_logger.logger.info(f"追加消息时发生错误：{str(e)}")


def get_chat_history_from_file(ticket_id: str) -> list[dict]:
    folder_path = f"{data_path}/{ticket_id}/"
    file_name = f"{folder_path}{chat_history_name}.txt"
    
    chat_history:list[dict] = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # 去除末尾的换行符并检查是否为空白行
                cleaned_line = line.strip()
                if cleaned_line:  # 如果不是空白行
                    record: dict = json.loads(cleaned_line)
                    # print(record)
                    chat_history.append(record)
    except FileNotFoundError:
        local_logger.logger.info(f"文件 {file_name} 不存在")
    except Exception as e:
        local_logger.logger.info(f"读取文件时发生错误：{str(e)}")

    return chat_history


def generate_unique_filename(filename):
    # 确保文件名是安全的
    secure_filename_base = secure_filename(os.path.splitext(filename)[0])
    extension = os.path.splitext(filename)[1]

    # 生成唯一的文件名前缀
    unique_prefix = str(uuid.uuid4().hex)

    # 构建最终的唯一文件名
    unique_filename = f"{unique_prefix}_{secure_filename_base}{extension}"
    
    return unique_filename

# 添加聊天中的文件储存
def upload_file(file: FileStorage):
    file_name = generate_unique_filename(file.filename)
    file_path = f"{file_data_path}/{file_name}"
    local_logger.logger.info("upload_file file_path ",file_path)
    try:
        # 创建文件夹（如果不存在）
        os.makedirs(file_data_path, exist_ok=True)
        file.save(file_path)
        local_logger.logger.info(f"文件已保存到 {file_path}")
        return file_name
    except Exception as e:
        local_logger.logger.info(f"保存文件时发生错误：{str(e)}")
    pass

def get_file_path(filename:str):
    file_path = f"{file_data_path}/{filename}"
    # 获取真实路径
    file_path = os.path.abspath(os.path.join(file_data_path, filename))
    local_logger.logger.info("get_file_path %s" ,file_path )
    return file_path