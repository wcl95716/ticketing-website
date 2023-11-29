import sys
import pandas as pd

sys.path.append("./src")
from utils import local_logger

from models.wechat_robot_online.types.organization_group_type import OrganizationGroup
from models.wechat_robot_online.types.vehicle_type import Vehicle


class LogProcessingType:
    
    @staticmethod
    def get_pandas_df(vehicle_data_list:list[Vehicle]):
        data = []
        for vehicle_data in vehicle_data_list:
            
            row = {
                # 'Organization Group': vehicle_data.organization,
                'Plate Number': vehicle_data.plate_number,
                'Organization': vehicle_data.organization,
                'Status': vehicle_data.status,
                'Camera Status': vehicle_data.camera_status
            }
            row = vehicle_data.__dict__
            
            data.append(row)
        # df = pd.DataFrame(data)
        # return df
        return data
        pass
    
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
    
    def get_vehicle_data_by_status(self):
        """
        通过status对vehicle_data进行分类
        """
        pass
    

    pass


