import sys

sys.path.append("./src")


import re
from typing import List

from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory, ChatActionsEnum

class ChatCommandHandler:
    def __init__(self, robot_name, actions:list[ChatActionsEnum]):
        self._robot_name = robot_name
        self._actions = actions
        # self._patterns = self.create_patterns()
    
    def create_patterns(self):
        # 使用正则表达式模式
        patterns = [rf'@{re.escape(self._robot_name)}\s*({re.escape(action.value)})' for action in self._actions]
        return patterns
    
    def search(self, message:str):
        for pattern,action in zip(self.create_patterns(), self._actions):
            match = re.search(pattern, message)
            # print("pattern : ",pattern)
            # print("action : ",action)
            # print("message : ",message)
            # print("match : ",match)
            # print("")
            if match:
                return action
        return None


if __name__ == "__main__":


    # 创建一个ChatConfig实例，传递多个不同的action
    config = ChatCommandHandler("机器人名", [ChatActionsEnum.CREATE_WORK_ORDER])

    messages = ['@机器人名 创建工单', '@机器人名 执行任务', '@机器人名 其他动作']

    for message in messages:
        # print(f"要匹配的消息: {message}")
        action = config.search(message)
        if action:
            # 提取关键词
            # keyword = match.group(1)
            print(f"匹配到关键词: {action}")
            result = ChatActionFunctionFactory.get_action_function(action)(message)
            print("执行完毕, result : ",result)
            # break
        else:
            print("没有匹配到关键词")
