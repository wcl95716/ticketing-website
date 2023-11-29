import sys
import pandas as pd
from models.wechat_robot_online.types.robot_task_type import RobotTask
from utils.table_image import create_table_image

sys.path.append("./src")
from utils import local_logger

from models.wechat_robot_online.types.organization_group_type import OrganizationGroup
from models.wechat_robot_online.types.vehicle_type import Vehicle


class LogProcessingFilesUrl:
    
    def __init__(self,vehicle_data_url:str , organization_group_url:str,language_template_url:str) -> None:
        self.vehicle_data_url = vehicle_data_url
        self.organization_group_url = organization_group_url
        self.language_template_url = language_template_url
        pass
    pass

class LogProcessing:
    
    @staticmethod
    def get_pandas_df(vehicle_data_list:list[Vehicle],group:OrganizationGroup):
        data = []
        for vehicle_data in vehicle_data_list:
            
            row = {
                # 'Organization Group': vehicle_data.organization,
                'Plate Number': vehicle_data.plate_number,
                'Organization': vehicle_data.organization,
                'Status': vehicle_data.status,
                'Camera Status': vehicle_data.camera_status,
                'Group Name': group.group_name
            }

            data.append(row)
        # df = pd.DataFrame(data)
        # return df
        return data
        pass
    
    @staticmethod
    # 获取RobotTask
    def get_robot_task(vehicle_data_list:list[Vehicle],group:OrganizationGroup) -> RobotTask:
        data = LogProcessing.get_pandas_df(vehicle_data_list,group)
        df = pd.DataFrame(data)
        img_path = create_table_image(df)
        to_user = group.group_name
        robot_task = RobotTask(to_user = to_user, content = img_path)
        return robot_task
        pass
    
    
    @staticmethod
    def get_robot_task_by_status(vehicle_data_list:list[Vehicle],group:OrganizationGroup) -> RobotTask:
        content = ""
        for vehicle_data in vehicle_data_list:
            content += vehicle_data.plate_number+","
            
        content += "状态为"+vehicle_data.status
        to_user = group.group_name
        robot_task = RobotTask(to_user = to_user, content = content ,task_type=1)
        return robot_task
        pass

    
    """
    LogProcessingType类用于分类日志数据
    vehicle_data 按照 organization_group进行分类
    """
    
    def __init__(self, vehicle_data: list[Vehicle], organization_group: list[OrganizationGroup]):
        self.vehicle_data = vehicle_data
        self.organization_group = organization_group
        self.vehicle_data_by_group = self.get_vehicle_data_by_group()
        self.vehicle_data_by_status = self.get_vehicle_data_by_status()
        pass
    
    def get_vehicle_data_by_status(self) -> dict[OrganizationGroup,dict[str , list[Vehicle] ]]:
        
        vehicle_data_by_group:dict[OrganizationGroup,list[Vehicle]] = self.get_vehicle_data_by_group()
        vehicle_data_by_status:dict[OrganizationGroup,dict[str , list[Vehicle] ]] = {}
        # vehicle_data_by_group 每个OrganizationGroup 下的 list[Vehicle]再根据 Vehicle 的 status 进行分类
        for org_group, vehicle_data_list in vehicle_data_by_group.items():
            # 遍历每个Vehicle对象
            for vehicle_data in vehicle_data_list:
                # 如果vehicle_data_by_status字典中不存在org_group组织，则创建一个空字典
                if org_group not in vehicle_data_by_status:
                    vehicle_data_by_status[org_group] = {}
                # 如果vehicle_data_by_status字典中不存在vehicle_data.status状态，则创建一个空列表
                if vehicle_data.status not in vehicle_data_by_status[org_group]:
                    vehicle_data_by_status[org_group][vehicle_data.status] = []
                # 将Vehicle对象添加到vehicle_data_by_status字典中
                vehicle_data_by_status[org_group][vehicle_data.status].append(vehicle_data)
        return vehicle_data_by_status
        
        pass 
    
    def get_vehicle_data_by_group(self) -> dict[OrganizationGroup,list[Vehicle]]:
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
    
    
    # 获取RobotTask
    def get_all_robot_task_by_group(self) -> list[RobotTask]:
        vehicle_data_by_group = self.get_vehicle_data_by_group()
        result: list[RobotTask]=  []
        for org_group, vehicle_data_list in vehicle_data_by_group.items():
            task = LogProcessing.get_robot_task(vehicle_data_list, org_group)
            result.append(task)
        
        return result
        pass
    
    def get_all_robot_task_by_group_and_status(self) ->list[RobotTask]:
        vehicle_data_by_status = self.get_vehicle_data_by_status()
        result: list[RobotTask]=  []
        for org_group, vehicle_data_list in vehicle_data_by_status.items():
            for status, vehicle_data_list in vehicle_data_list.items():
                task = LogProcessing.get_robot_task_by_status(vehicle_data_list, org_group)
                result.append(task)
        return result
        pass
    pass


