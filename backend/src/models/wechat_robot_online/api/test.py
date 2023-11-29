import requests

# 定义 LogProcessingFilesUrl 对象数据
data = {
    'vehicle_data_url': 'http://127.0.0.1:8001/test/uploads/c2faed2d0ed641f59cb8b46fe236a7eb_-.xlsx',
    'organization_group_url': 'http://localhost:8001/test/uploads/ab0c379448914cfb8b4d02eca10d4862_-.xlsx',
    'language_template_url': ''
}

# 发送 POST 请求到 API 端点
url = 'http://localhost:8001/wechat_robot_online/process_log'  # 替换为实际的 API 地址
response = requests.post(url, json=data)

# 检查响应
if response.status_code == 200:
    print('Request successful!')
    print(response.json())
else:
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)
