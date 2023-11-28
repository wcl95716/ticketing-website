
import sys
sys.path.append("./src")

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


if __name__=='__main__':

    # 传入Excel文件路径，并获取OrganizationGroup对象列表
    excel_file_path = "http://127.0.0.1:8001/test/uploads/4864190028c54502aaee3f1883e3323a_.xlsx"
    org_group_list = get_organizationgroups_from_url(excel_file_path)

    # 现在你可以在后续的代码中使用org_group_list来操作这些数据
    for org_group in org_group_list:
        print(f"车辆组织: {org_group.organization}, 群名称: {org_group.group_name}")