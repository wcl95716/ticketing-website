import requests

# 定义 LogProcessingFilesUrl 对象数据
data = {
    'vehicle_data_url': 'http://47.116.201.99:8001/test/uploads/201a044dd5e142dabf4264be33dcb449_-.xlsx',
    'organization_group_url': 'http://47.116.201.99:8001/test/uploads/c5b6860bd57e4922a8faf8fc25417ceb_-.xlsx',
    'language_template_url': ''
}

# 发送 POST 请求到 API 端点
url = 'http://47.116.201.99:8001/wechat_robot_online/process_log'  # 替换为实际的 API 地址
response = requests.post(url, json=data)

# 检查响应
if response.status_code == 200:
    print('Request successful!')
    print(response.json())
else:
    print(f'Request failed with status code: {response.status_code}')
    print(response.text)
