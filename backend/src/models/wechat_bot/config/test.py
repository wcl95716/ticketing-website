import re

class ChatConfig:
    def __init__(self, robot_name, actions):
        self._robot_name = robot_name
        self._actions = actions
        # self._patterns = self.create_patterns()
    
    def create_patterns(self):
        # 使用正则表达式模式
        patterns = [rf'@{re.escape(self._robot_name)} ({re.escape(action)})' for action in self._actions]
        return patterns
    
    def search(self, message:str):
        for pattern in self.create_patterns():
            match = re.search(pattern, message)
            if match:
                return match
        return None

# 创建一个ChatConfig实例，传递多个不同的action
config = ChatConfig("机器人名", ["创建工单", "执行任务", "其他动作"])

# # 获取不同的正则表达式模式
# patterns = config.create_patterns()

# print("patterns : ",patterns)

# 要匹配的消息
messages = ['@机器人名 创建工单', '@机器人名 执行任务', '@机器人名 其他动作']

for message in messages:
    # print(f"要匹配的消息: {message}")
    match = config.search(message)
    if match:
        # 提取关键词
        keyword = match.group(1)
        print(f"匹配到关键词: {keyword}")
        # break
    else:
        print("没有匹配到关键词")
