import requests
import pandas as pd
from io import BytesIO

def download_excel_and_read(excel_url: str) -> pd.DataFrame:
    try:
        # 使用requests库下载Excel文件
        response = requests.get(excel_url)

        if response.status_code == 200:
            # 使用BytesIO对象包装字节数据
            content = BytesIO(response.content)
            
            # 使用pandas库读取Excel文件内容
            df = pd.read_excel(content, engine='openpyxl')
            return df
        else:
            print("Failed to download Excel file")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

# 调用函数并传入Excel文件的URL
# excel_url = "http://localhost:8001/test/uploads/2c2f107d62fc49ac83d88f645fdf034d_.xlsx"
# df = download_excel_and_read(excel_url)

# if df is not None:
#     # 现在你可以操作df，处理Excel文件的内容
#     print(df.head())  # 打印前几行数据
