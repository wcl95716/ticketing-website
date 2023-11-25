import hashlib


process_group_list = ["测试4群123123", "测试3群"]

group_id = "测试4群"
# any(group_id.startswith(prefix) for prefix in process_group_list)

print(group_id.startswith("测试4群123123"))

print("测试4群123123".startswith(group_id))