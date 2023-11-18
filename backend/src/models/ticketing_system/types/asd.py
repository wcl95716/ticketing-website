from datetime import datetime

def parse_datetime(date_string):
    try:
        # 尝试解析第一种格式
        return datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        try:
            # 尝试解析第二种格式
            return datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            # 如果两种格式都无法解析，可以返回None或引发异常，具体取决于你的需求
            return None

# 测试解析函数
date_string1 = '2023-11-01 01:40:28'
date_string2 = '2023-11-17T16:53:46.732386'

date_obj1 = parse_datetime(date_string1)
date_obj2 = parse_datetime(date_string2)

if date_obj1:
    print("第一种格式解析结果:", date_obj1)
else:
    print("无法解析第一种格式")

if date_obj2:
    print("第二种格式解析结果:", date_obj2)
else:
    print("无法解析第二种格式")
