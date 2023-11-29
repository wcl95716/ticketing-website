
import sys

import requests

from models.wechat_robot_online.types.robot_task_type import RobotTask
sys.path.append("./src")

from models.wechat_robot_online.types.log_processing_type import LogProcessing
from utils import local_logger
from utils.table_image import create_table_image


import pandas as pd
from models.wechat_robot_online.types.organization_group_type import OrganizationGroup
from models.wechat_robot_online.types.vehicle_type import Vehicle

from utils.download_file import download_excel_and_read


def get_vehicles_from_url(excel_url:str) -> list[Vehicle]:
    # 读取Excel文件
    
    df:pd.DataFrame = download_excel_and_read(excel_url)
    
    # print("asdasddasd  ",df)
    if df is None:
        return None
    # 将Excel数据转化为Vehicle对象列表
    
    vehicles:list[Vehicle] = []
    for index, row in df.iterrows():
        plate_number = row['车牌号码']
        organization = row['车辆组织']
        status = row['车辆状态（离线/定位）']
        camera_status = row['摄像头状态']
        
        vehicle = Vehicle(plate_number, organization, status, camera_status)
        vehicles.append(vehicle)
    return vehicles


def get_organizationgroups_from_url(excel_url: str) -> list[OrganizationGroup]:

    # 使用download_excel_and_read函数下载Excel文件并读取内容
    df = download_excel_and_read(excel_url)
    
    if df is not None:
        # 创建一个空列表来存储OrganizationGroup对象
        organization_groups = []

        # 遍历DataFrame的行，为每一行的数据创建一个OrganizationGroup对象
        for index, row in df.iterrows():
            organization = row['客户名称']
            group_name = row['微信服务群名称']
            org_group = OrganizationGroup(organization, group_name)
            organization_groups.append(org_group)

        return organization_groups
    else:
        return None


def get_log_processing(vehicle_url, organization_group_url) -> LogProcessing:
    vehicle_list = get_vehicles_from_url(vehicle_url)
    org_group_list = get_organizationgroups_from_url(organization_group_url)
    
    log_processing = LogProcessing(vehicle_list, org_group_list)
    return log_processing
    pass

def get_tasks( vehicle_url, organization_group_url) -> list[RobotTask]:
    log_processing = get_log_processing(vehicle_url, organization_group_url)
    tasks = log_processing.get_all_robot_task()
    return tasks
    pass 

def upload_img_file(img_path:str) -> None:
    url = 'http://47.116.201.99:8001/test/upload_file'
    file_path = img_path
    # files = {'file': ( , open(file_path, 'rb'))}
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    
    # 检查响应状态码是否为 200，表示请求成功
    if response.status_code == 200:
        # 使用 response.json() 方法解析返回的 JSON 数据
        json_data = response.json()
        
        # 获取 file_url 字段的值
        file_url = json_data.get('file_url', None)
        
        if file_url:
            return file_url
        else:
            print("File URL not found in the JSON response.")
            return None
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None

    

if __name__=='__main__':

    # 传入Excel文件路径，并获取OrganizationGroup对象列表
    vehicle_url= "http://127.0.0.1:8001/test/uploads/c2faed2d0ed641f59cb8b46fe236a7eb_-.xlsx"
    excel_file_path= "http://localhost:8001/test/uploads/ab0c379448914cfb8b4d02eca10d4862_-.xlsx"

    # 获取分类后的数据
    # 创建LogProcessingType对象并进行分类
    log_processing = get_log_processing(vehicle_url, excel_file_path)
    
    tasks = log_processing.get_all_robot_task()
    print(len(log_processing.vehicle_data_by_group.keys()) , len(tasks) )
    for task in tasks:
        print("task: ",task.to_user , task.content)

    # Create a DataFrame from the list of dictionaries

    local_logger.logger.info("LogProcessingType类测试成功！")