
import sys
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
            organization = row['车辆组织']
            group_name = row['群名称']
            org_group = OrganizationGroup(organization, group_name)
            organization_groups.append(org_group)

        return organization_groups
    else:
        return None


def get_log_processing(vehicle_url, organization_group_url) -> LogProcessing:
    
    org_group_list = get_organizationgroups_from_url(organization_group_url)
    vehicle_list = get_vehicles_from_url(vehicle_url)
    log_processing = LogProcessing(vehicle_list, org_group_list)
    return log_processing
    pass

if __name__=='__main__':

    # 传入Excel文件路径，并获取OrganizationGroup对象列表
    excel_file_path = "http://127.0.0.1:8001/test/uploads/4864190028c54502aaee3f1883e3323a_.xlsx"
    vehicle_url = "http://localhost:8001/test/uploads/2c2f107d62fc49ac83d88f645fdf034d_.xlsx"

    # 获取分类后的数据
    # 创建LogProcessingType对象并进行分类
    log_processing = get_log_processing(vehicle_url, excel_file_path)

    for org_group, vehicle_data_list in log_processing.vehicle_data_by_group.items():
        data = LogProcessing.get_pandas_df(vehicle_data_list)
        df = pd.DataFrame(data)
        print(df)
        create_table_image(df)
        
        break

    # Create a DataFrame from the list of dictionaries

    local_logger.logger.info("LogProcessingType类测试成功！")