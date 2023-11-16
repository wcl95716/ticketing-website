

import json
import os

from models.ticketing_system.types.user_profile import UserProfile
from models.ticketing_system.types import user_profile
from utils import local_logger


user_file_path = "data/users/"
user_file_name = "user_data.json"

def add_user_to_file(user: UserProfile):
    folder_path = f"{user_file_path}"
    file_name = f"{folder_path}{user_file_name}"
    try:
        # 创建工单文件夹（如果不存在）
        os.makedirs(folder_path, exist_ok=True)

        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(json.dumps(user.to_dict())  + '\n')  # 将消息对象转换为JSON字符串并写入文件
        local_logger.logger.info("用户追加成功")
    except Exception as e:
        local_logger.logger.info(f"追加消息时发生错误：{str(e)}")
        

def get_users_to_file() -> list[dict]:
    folder_path = f"{user_file_path}"
    file_name = f"{folder_path}{user_file_name}"
    
    users:list[dict] = []

    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # 去除末尾的换行符并检查是否为空白行
                cleaned_line = line.strip()
                if cleaned_line:  # 如果不是空白行
                    record: dict = json.loads(cleaned_line)
                    # print(record)
                    users.append(record)
    except FileNotFoundError:
        local_logger.logger.info(f"文件 {file_name} 不存在")
    except Exception as e:
        local_logger.logger.info(f"读取文件时发生错误：{str(e)}")

    return users
    pass

