import sys
sys.path.append("./src")
from utils import local_logger
from models.wechat_robot_online.api.main_api import get_organizationgroups_from_url, get_vehicles_from_url


from models.wechat_robot_online.types.organization_group_type import OrganizationGroup
from models.wechat_robot_online.types.vehicle_type import Vehicle


class LogProcessingType:
    """
    LogProcessingType类用于分类日志数据
    vehicle_data 按照 organization_group进行分类
    """
    
    def __init__(self, vehicle_data: list[Vehicle], organization_group: list[OrganizationGroup]):
        self.vehicle_data = vehicle_data
        self.organization_group = organization_group
        self.vehicle_data_by_group = self.get_vehicle_data_by_group()
        pass
    
    def get_vehicle_data_by_group(self):
        """
        通过organization_group对vehicle_data进行分类
        """
        vehicle_data_by_group:dict[OrganizationGroup,list[Vehicle]] = {}
        
        # 遍历每个组织的Vehicle对象列表
        for vehicle_data in self.vehicle_data:
            
            # 遍历每个OrganizationGroup对象
            for org_group in self.organization_group:
                
                # 如果Vehicle对象的organization_group属性等于OrganizationGroup对象的group_name属性
                if vehicle_data.organization == org_group.organization:
                    
                    # 如果vehicle_data_by_group字典中不存在org_group组织，则创建一个空列表
                    if org_group not in vehicle_data_by_group:
                        vehicle_data_by_group[org_group] = []
                        
                    # 将Vehicle对象添加到vehicle_data_by_group字典中
                    vehicle_data_by_group[org_group].append(vehicle_data)
                    
        return vehicle_data_by_group
        pass
    pass


if __name__=='__main__':

    # 传入Excel文件路径，并获取OrganizationGroup对象列表
    excel_file_path = "http://127.0.0.1:8001/test/uploads/4864190028c54502aaee3f1883e3323a_.xlsx"
    org_group_list:list[OrganizationGroup] = get_organizationgroups_from_url(excel_file_path)
    
    vehicle_url = "http://localhost:8001/test/uploads/2c2f107d62fc49ac83d88f645fdf034d_.xlsx"
    vehicle_list:list[Vehicle] = get_vehicles_from_url(vehicle_url)
    
    # 创建LogProcessingType对象并进行分类
    log_processing = LogProcessingType(vehicle_list, org_group_list)

    # 获取分类后的数据
    # 创建LogProcessingType对象并进行分类
    log_processing = LogProcessingType(vehicle_list, org_group_list)

    # 获取分类后的数据
    vehicle_data_by_group = log_processing.get_vehicle_data_by_group()

    # 遍历vehicle_data_by_group字典
    for org_group, vehicle_data_list in vehicle_data_by_group.items():
        print(f"Organization Group: {org_group.__dict__}  {len(vehicle_data_list)}")
        
        # 遍历每个组织的Vehicle对象列表
        for vehicle_data in vehicle_data_list:
            # print(f"Vehicle Data: {vehicle_data.__dict__}")
            print(f"{vehicle_data.plate_number},{vehicle_data.organization},{vehicle_data.status},{vehicle_data.camera_status},")
            
            
    local_logger.logger.info("LogProcessingType类测试成功！")
