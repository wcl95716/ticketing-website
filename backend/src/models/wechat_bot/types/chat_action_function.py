

from enum import Enum

class ChatActionsEnum(Enum):
    WORK_ORDER_CREATE = "创建工单"
    WORK_ORDER_UPDATE = "工单更新"
    EXECUTE_TASK = "执行任务"
    OTHER_ACTION = "其他动作"
    
    
class ChatActionFunctionFactory:
    @staticmethod
    def work_order_create(message: tuple = None) -> str:
        # 编写创建工单的操作逻辑
        print("create_work_order message : ",message)
        return f"@{message[0]} 工单已创建 https://www.baidu.com"
    
    def work_order_update(message: tuple = None):
        # 编写工单更新的操作逻辑
        return "工单已更新"
    
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

