import re

# 定义一个正则表达式模式，使用Unicode转义
pattern = r"\u2005创建工单"

# 测试字符串，包含了实际的Unicode字符\u2005
test_string = "@AI苏博蒂奇\u2005创建工单"

# 在测试字符串中搜索模式
match = re.search(pattern, test_string)

if match:
    print("匹配成功")
else:
    print("匹配失败")
