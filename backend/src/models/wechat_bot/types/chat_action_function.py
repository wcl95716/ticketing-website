
import requests
import datetime
from enum import Enum

class ChatActionsEnum(Enum):
    WORK_ORDER_CREATE = "创建工单"
    WORK_ORDER_UPDATE = "工单更新"
    EXECUTE_TASK = "执行任务"
    OTHER_ACTION = "其他动作"
    
    
class ChatActionFunctionFactory:
    
    def add_ticket_to_website(ticket_record: dict = None) -> dict:
        url = 'http://47.116.201.99:8001/test/add_ticket'
        response = requests.post(url, json=ticket_record)
        # 检查响应状态码
        if response.status_code == 200:
            # 如果响应状态码为200，表示成功添加工单
            ticket_info = response.json()
            return ticket_info
        else:
            # 如果响应状态码不是200，表示添加工单时出现错误
            error_info = response.json()
            print("Error:", error_info)
            return None
    pass


    @staticmethod
    def get_work_order_link(ticket_id: str ,customer_id ) -> str:
        return f"@{customer_id} 工单通知  https://test?ticket_id = {ticket_id} & customer_id = {customer_id}"
    
    @staticmethod
    def work_order_create(group_id, message: tuple = None) -> tuple[str]:
        # 编写创建工单的操作逻辑
        print("create_work_order message : ",message)
        if message is None:
            return None
        # return f"@{message[0]} 工单已创建 https://www.baidu.com"
        ticket_data = {
            "title": message[0] + " " + message[1],
            "created_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": 0,
            "priority": 0,
            "creator": message[0],
            "assigned_to": "",
            "ticket_type": "",
            "closed_time": "",
            "source": {
                "group_id": group_id,
                "customer_id": message[0],
            }
        }
        
        ticket_response = ChatActionFunctionFactory.add_ticket_to_website(ticket_data)
        if ticket_response is None:
            return None
        
        ticket_id = ticket_response["ticket_id"]
        return (group_id, ChatActionFunctionFactory.get_work_order_link(ticket_id , message[0]))
    
    # 工单更新逻辑
    @staticmethod
    def work_order_update(ticket_record: dict = None) ->  tuple[str]:
        # 编写工单更新的操作逻辑
        if ticket_record is None:
            return None
        
        # 获取数据源
        source = ticket_record["source"]
        group_id = source["group_id"]
        customer_id = source["customer_id"]
        ticket_id = ticket_record["ticket_id"]
        return (group_id, ChatActionFunctionFactory.get_work_order_link(ticket_id , customer_id))
        # return "工单已更新"
    
    @staticmethod
    def execute_task():
        # 编写执行任务的操作逻辑
        return "任务已执行"
    
    @staticmethod
    def other_action():
        # 编写其他动作的操作逻辑
        return "其他动作已处理"

    @staticmethod
    def get_action_function(action: ChatActionsEnum):
        print("action : ",action)
        action_function = getattr(ChatActionFunctionFactory, action.name.lower(), None)
        return action_function

