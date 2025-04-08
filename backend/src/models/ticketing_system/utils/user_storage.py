

import json
import os
import sys
import pandas as pd
sys.path.append("./src")


from models.ticketing_system.types.user_profile import UserProfile
from models.ticketing_system.types import user_profile
from utils import local_logger



user_file_path = "data/users/"
user_file_name = "ticketing_system_user_data.txt"

def add_user_to_file(user: UserProfile):
    folder_path = f"{user_file_path}"
    file_name = f"{folder_path}{user_file_name}"
    user_list = get_users_to_file()
    for i in range(len(user_list)):
        if user_list[i]["user_id"] == user.user_id:
            local_logger.logger.info("用户已存在")
            return 
            pass

    os.makedirs(folder_path, exist_ok=True)
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(json.dumps(user.to_dict())  + '\n')  # 将消息对象转换为JSON字符串并写入文件
    local_logger.logger.info("用户添加成功")
    
    return 

        
        
def update_user(user: UserProfile):   
    user_list = get_users_to_file()
    for i in range(len(user_list)):
        if user_list[i]["user_id"] == user.user_id:
            user_list[i] = user.to_dict()
            break
        if i == len(user_list) - 1:
            local_logger.logger.info("用户不存在")
            return 
            pass
    folder_path = f"{user_file_path}"
    file_name = f"{folder_path}{user_file_name}"

    # 创建工单文件夹（如果不存在）
    os.makedirs(folder_path, exist_ok=True)

    with open(file_name, 'w', encoding='utf-8') as file:
        for user in user_list:
            file.write(json.dumps(user)  + '\n')  # 将消息对象转换为JSON字符串并写入文件
    local_logger.logger.info("用户更新成功")

    pass

def get_users_to_file() -> list[dict]:
    folder_path = f"{user_file_path}"
    file_name = f"{folder_path}{user_file_name}"
    
    users:list[dict] = []

    try:
         # 创建工单文件夹（如果不存在）
        os.makedirs(folder_path, exist_ok=True)
        with open(file_name, 'r', encoding='utf-8') as file:
            for line in file:
                # 去除末尾的换行符并检查是否为空白行
                cleaned_line = line.strip()
                if cleaned_line:  # 如果不是空白行
                    record: dict = json.loads(cleaned_line)
                    # 更改头像地址
                    record["avatar_url"] = "http://14.103.200.99:8001/test/uploads/79cd180e87d345be9fd60123183fec4a_16211702261434_.pic.jpg"
                    # print(record)
                    users.append(record)
    except FileNotFoundError:
        local_logger.logger.info(f"文件 {file_name} 不存在")
    except Exception as e:
        local_logger.logger.info(f"读取文件时发生错误：{str(e)}")

    return users
    pass

def get_user_by_id(user_id: str) -> UserProfile:
    users:list[dict] = get_users_to_file()
    for user in users:
        if user["user_id"] == user_id:
            return UserProfile.from_dict(user)
    return None
    pass



def read_profiles_from_excel(filename) -> list[UserProfile]:
    # 读取Excel文件
    df = pd.read_excel(user_file_path + filename)

    # 将每行转换为UserProfile对象
    profiles = []
    for _, row in df.iterrows():
        profile = UserProfile(
            user_id=row['user_id'],
            name=row['name'],
            email=row.get('email'),
            phone=row.get('phone'),
            avatar=row.get('avatar'),
            avatar_url=row.get('avatar_url'),
            info=row.get('info'),
            password=row.get('password')
        )
        profiles.append(profile)
    return profiles

def write_profiles_to_excel(filename, profiles:list[UserProfile]):
    # 将每个UserProfile对象转换为字典
    # data = [profile.to_dict() for profile in profiles]
    data = get_users_to_file()
    # 转换为DataFrame
    df = pd.DataFrame(data)
    # 写入Excel
    df.to_excel(user_file_path+filename, index=False)
    
def write_profiles_to_csv(filename, profiles):
    # 将每个UserProfile对象转换为字典
    data = get_users_to_file()
    # 转换为DataFrame
    df = pd.DataFrame(data)
    # 写入CSV
    df.to_csv(user_file_path+filename, index=False)
    
    
# write_profiles_to_excel("user_data.xlsx", get_users_to_file())
# users = read_profiles_from_excel("user_data.xlsx")
# for user in users:
#     print(user.to_dict())
#     pass