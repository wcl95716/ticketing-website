
import time
# import keyboard
import sys
import pandas as pd
sys.path.append("./src")
import requests

from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory

import time
from models.wechat_bot.types.group_manager import GroupManager
from models.wechat_bot.utils.chat import get_group_list, send_file_from_url, send_message
from utils import local_logger
from models.wechat_bot.config import config




def fix_online_tasks() :
    tasks: list[tuple[str]] = ChatActionFunctionFactory.get_online_tasks()
    local_logger.logger.info("fix_online_tasks tasks : %s", len(tasks) )
    # tasks 按照第一个元素排序
    
    if tasks is not None:
        count = 0
        for task in tasks:
            print(f"处理在线消息 count= {count} task= {task}")
            try:
                if task[2] == 1:
                    send_file_from_url(task[0], task[1])
                    pass 
                elif task[2] == 0:
                    send_message(task[0], task[1])
                    pass 
            except Exception as e:
                local_logger.logger.info(f"处理在线消息出现错误  {str(e)}")

# 读取群聊列表
# 从excel中读取群聊列表
def get_group_list_from_excel() -> list[str]:
    import pandas as pd

    df = pd.read_excel("data/微信服务群.xlsx", engine='openpyxl')
    print(df)
    result = []
    for index, row in df.iterrows():
        # 微信服务群名称
        group_name = row['微信服务群名称']
        result.append(group_name)

    # 使用set去除重复数据，然后再转回列表
    unique_group_list = list(set(result))
    return unique_group_list



def test_group_manager():
    
    # group_list = ["测试4群", "测试3群","测试2群"]
    group_list = ["测试4群", "测试3群","测试2群","无锡公司-注册群","太仓公司安装注册群","昆山一组（苏州）"]
    group_list = get_group_list_from_excel()
    # group_list = ["测试2群"]
    
    config.update_robot_name()
    group_manager = GroupManager(group_list)
    while True:  # 循环直到停止标志为True
        print("开始处理群聊任务")
        try:
            group_list = get_group_list()
            # 获取group_list 
            group_list = group_list[:3]
            print(f"获取group_list  {group_list}")
            for group_id in group_list:
                group_manager.process_one_group_tasks(group_id)
        
            fix_online_tasks()
        except Exception as e:
            local_logger.logger.info(f"处理群聊任务时发生错误：{str(e)}")
        time.sleep(1)


if __name__ == "__main__":
    print("开始处理群聊任务")
    test_group_manager()
    pass

