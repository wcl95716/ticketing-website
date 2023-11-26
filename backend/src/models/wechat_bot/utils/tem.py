import pandas as pd

def save_list_to_excel(list_data, filename):
    # 将列表转换为DataFrame
    df = pd.DataFrame({'group_names': list_data})
    # 将DataFrame写入Excel文件
    df.to_excel(filename, index=False)

# 待保存的列表
group_list = ["测试4群", "测试3群"]

# 调用函数保存数据
save_list_to_excel(group_list, 'groups.xlsx')
