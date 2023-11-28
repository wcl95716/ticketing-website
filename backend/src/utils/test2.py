import pandas as pd
import matplotlib.pyplot as plt

# 创建测试数据
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [30, 25, 35],
    'Location': ['New York', 'Los Angeles', 'Chicago']
}
data = {
    '车牌号': ['苏B00666D', '苏B80997', '苏B99862', '苏BA9822', '苏BM0182', '苏BM0190', '苏BM2308', '苏BM8853', '苏BM8885', '苏BR5736', '苏BR8161', '苏BW3705', '苏BW5960', '苏BY2715'],
    '公司名称': ['无锡市绿洲接送客运服务有限公司'] * 14,
    '状态': ['离线1天', '离线1天', '离线2天', '熄火4天', 'nan', '熄火1天', '熄火1天', 'nan', 'nan', '熄火1天', '熄火1天', '熄火1天', '离线8天', '离线5天'],
    '问题描述': ['nan', 'nan', 'nan', 'nan', 'AV03,AV04遮挡', 'nan', 'nan', '通通道全黑屏', 'AV03摄像头需要擦拭', 'nan', 'nan', 'nan', 'nan', 'nan']
}

# 将数据转换为DataFrame
df = pd.DataFrame(data)

# 创建表格图像
fig, ax = plt.subplots(figsize=(8, 4))
ax.axis('tight')
ax.axis('off')
# ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

# 指定使用中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1, 1.5)  # 调整行高以适应中文字符

# 保存图像为文件
plt.savefig('table_image.png', bbox_inches='tight', pad_inches=0.1)
plt.show()