
import requests
import datetime
from enum import Enum

from utils import local_logger
from urllib.parse import quote

class ChatActionsEnum(Enum):
    WORK_ORDER_CREATE = r""
    WORK_ORDER_UPDATE = r"工单更新"
    EXECUTE_TASK = r"执行任务"
    OTHER_ACTION = r"其他动作"
    SEND_LOG_FILE = r"发送日志文件"
    
    
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

    @staticmethod
    def add_ticket_init_chat(ticket_record: dict = None , group_message:list[tuple] = None, sender_name:str = None) -> dict:
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
            "message_type": message_type,
            "chat_profile":1001
        }
        response = requests.post(url, json=chatMessage)
        if group_message is None:
            return 
        num_messages = len(group_message)
        # 设置要取的最后十条消息的数量
        num_to_keep = 5
        last_ten_messages = group_message[-num_to_keep:] if num_messages >= num_to_keep else group_message

        try:
            for message in last_ten_messages:
                message_id = ""
                sender = message[0]  
                if sender != sender_name:
                    continue  
                    
                content = message[1]
                message_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                message_type = 0
                chatMessage = {
                    "message_id": message_id,
                    "ticket_id": ticket_id,
                    "sender": sender,
                    "content": content,
                    "message_time": message_time,
                    "message_type": message_type,
                    "chat_profile":1000
                }
                response = requests.post(url, json=chatMessage)
                pass
        except Exception as e:
            local_logger.logger.info("add_ticket_init_chat error : %s", str(e))
            pass
            
        

    @staticmethod
    def get_work_order_link(ticket_id: str ,customer_id ) -> str:
        original_string = customer_id
        encoded_string = quote(original_string, encoding='utf-8')
        return f"@{customer_id} 工单id: {ticket_id}  工单消息通知  {ChatActionFunctionFactory.page_url}?ticket_id={ticket_id}&customer_id={encoded_string}"
    
    @staticmethod
    def work_order_create(group_id, message: tuple = None,group_messages:list[tuple] = None ) -> tuple[str]:
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
        ChatActionFunctionFactory.add_ticket_init_chat(ticket_response,group_messages , message[0])
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
    def get_online_tasks(api_url = 'http://47.116.201.99:8001/wechat_robot_online/get_task') -> list[tuple[str]]:
        try:
            # 发送 GET 请求
            response = requests.get(api_url)
            # 检查响应状态码
            if response.status_code == 200:
                # 解析 JSON 响应
                task_data:list[dict] = response.json()
                result = []
                for task in task_data:
                    result.append((task["to_user"], task["content"],task["task_type"]))
                result.sort(key=lambda x: x[0])
                return result
            else:
                print(f"请求失败，状态码：{response.status_code}")
        except Exception as e:
            print(f"请求发生异常：{str(e)}")
        
        pass 
    
        
    # @staticmethod
    # def send_log_file(task: dict = None) -> tuple[str]:
    #      # data like : [{'content': 'http://47.116.201.99:8001/test/uploads/402fb8848690486782a5dd2b6c73ad6a_b6aa2cbea01642709f62526ba59b40f4.png', 'task_type': None, 'to_user': '昆山一组（苏州）'}, {'content': 'http://47.116.201.99:8001/test/uploads/847e92cd766145aeb84b5d54a3d9bb28_bbca4427f9894640b230df88aa3f73a6.png', 'task_type': None, 'to_user': '无锡公司-注册群'}, {'content': 'http://47.116.201.99:8001/test/uploads/a09a1921dd2a4282aa829ba1d0b7da8f_59a47f551acd47bb8bd3c45b638ca73d.png', 'task_type': None, 'to_user': '太仓公司安装注册群'}]
    #     return (task["to_user"], task["content"])
    
    @staticmethod
    def execute_task():
        # 编写执行任务的操作逻辑
        return "任务已执行"
    
    @staticmethod
    def other_action():
        # 编写其他动作的操作逻辑
        return "其他动作已处理"

    @staticmethod
    def get_action_function(action: ChatActionsEnum) -> callable:
        action_function = getattr(ChatActionFunctionFactory, action.name.lower(), None)
        return action_function

