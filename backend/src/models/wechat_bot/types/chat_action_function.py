
import requests
import datetime
from enum import Enum

from utils import local_logger

class ChatActionsEnum(Enum):
    WORK_ORDER_CREATE = r"创建工单"
    WORK_ORDER_UPDATE = r"工单更新"
    EXECUTE_TASK = r"执行任务"
    OTHER_ACTION = r"其他动作"
    
    
class ChatActionFunctionFactory:
    
    page_url = "http://47.116.201.99:4000/user_chat_page"
    # ticket_id=2023-11-17-211224191561&customer_id=%E4%BD%A0%E6%98%AF
    @staticmethod
    def add_ticket_to_website(ticket_record: dict = None) -> dict:
        url = 'http://47.116.201.99:8001/test/add_ticket'
        response = requests.post(url, json=ticket_record)
        # 检查响应状态码
        if response.status_code == 200:
            # 如果响应状态码为200，表示成功添加工单
            ticket_info = response.json()
            # print("Success:", ticket_info)
            
            
            local_logger.logger.info("add_ticket_to_website ticket_info : %s", ticket_info)
            return ticket_info
        else:
            # 如果响应状态码不是200，表示添加工单时出现错误
            error_info = response.json()
            local_logger.logger.info ("Error:", error_info)
            return None
    pass

    def add_ticket_init_chat(ticket_record: dict = None) -> dict:
        url = 'http://47.116.201.99:8001/test/add_chat_record'
        ticket_id = ticket_record["ticket_id"]
        
            # 生成随机的消息ID、工单ID、发送者、消息内容和消息时间
        message_id = ""
        sender = '系统消息'  
        content = "你好，有什么可以帮你的?可以在此留言"

        message_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message_type = 0

        chatMessage = {
            "message_id": message_id,
            "ticket_id": ticket_id,
            "sender": sender,
            "content": content,
            "message_time": message_time,
            "message_type": message_type
        }
        response = requests.post(url, json=chatMessage)
        
        


    @staticmethod
    def get_work_order_link(ticket_id: str ,customer_id ) -> str:
        return f"@{customer_id} 工单通知  {ChatActionFunctionFactory.page_url}?ticket_id={ticket_id}&customer_id={customer_id}"
    
    @staticmethod
    def work_order_create(group_id, message: tuple = None) -> tuple[str]:
        # 编写创建工单的操作逻辑
        local_logger.logger.info("work_order_create begin ")
        if message is None:
            return None
        # return f"@{message[0]} 工单已创建 https://www.baidu.com"
        ticket_data = {
            "title":group_id+ " " +  message[0] + " " + message[1],
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
        ChatActionFunctionFactory.add_ticket_init_chat(ticket_response)
        local_logger.logger.info("work_order_create ticket_response : %s", ticket_response)
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

