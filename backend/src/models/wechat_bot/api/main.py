
import time
# import keyboard
import sys
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
    local_logger.logger.info("fix_online_tasks tasks : %s", tasks)
    if tasks is not None:
        for task in tasks:
            print(f"处理群聊任务 {task}")
            if task[2] == 0:
                send_file_from_url(task[0], task[1])
            elif task[2] == 1:
                send_message(task[0], task[1])

    

def test_group_manager():
    # group_list = ["测试4群", "测试3群","测试2群"]
    group_list = ["测试4群", "测试3群","测试2群","无锡公司-注册群","太仓公司安装注册群","昆山一组（苏州）"]
    # group_list = ["测试2群"]
    group_manager = GroupManager(group_list)
 
    config.update_robot_name()
    while True:  # 循环直到停止标志为True
        print("开始处理群聊任务")
        try:
            group_list = get_group_list()
            # 获取group_list 前三个群聊
            group_list = group_list[:1]
            group_manager.process_group_tasks(process_group_list=group_list)
            fix_online_tasks()

        except Exception as e:
            local_logger.logger.info(f"处理群聊任务时发生错误：{str(e)}")
        time.sleep(1)


if __name__ == "__main__":
    print("开始处理群聊任务")
    test_group_manager()
    pass
