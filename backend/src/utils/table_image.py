import os
import uuid
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


def create_table_image(df, directory = "./data/pngs/", file_name=None, base_height_per_row=0.24, base_width_per_column=2.0, min_width=5, min_height=4, max_width=15, max_height=250, dpi=300):
    """
    Create an image of a pandas DataFrame as a table, save it in the specified directory, and return the file path.

    Parameters:
    df (pandas.DataFrame): DataFrame to be visualized.
    directory (str): Directory where the image will be saved.
    file_name (str): Name of the file to save the image.
    base_height_per_row (float): Base height per row in inches.
    base_width_per_column (float): Base width per column in inches.
    min_width (int): Minimum width of the image in inches.
    min_height (int): Minimum height of the image in inches.
    max_width (int): Maximum width of the image in inches.
    max_height (int): Maximum height of the image in inches.
    dpi (int): Dots per inch (resolution of the image).

    Returns:
    str: Path of the saved image file.
    """
    if file_name is None:
        # file_name = 'table_image.png'
        # 获取一个随机的名字
        file_name = uuid.uuid4().hex + '.png'
        
    # Replace "nan" values with empty strings
    df = df.fillna("")

    # Set font properties for displaying Chinese characters 
    # plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    # plt.rcParams['font.sans-serif'] = ['AR PL UKai CN']
    
    
    # plt.rcParams['font.sans-serif'] = ['AR PL UKai CN']
    
    # font_path = '/usr/share/fonts/truetype/arphic/ukai.ttc:style=Bold'
    # # plt.rcParams['font.sans-serif'] = [font_path]
    # plt.rcParams['font.sans-serif'] = ['SimHei', 'SimSun', 'AR PL UKai CN', 'Noto Sans CJK']
    # # 清除 Matplotlib 缓存
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = ['AR PL UKai CN']
    plt.rcParams['font.sans-serif'] = []

    # # 然后重新设置字体配置
    plt.rcParams['font.sans-serif'] = ['AR PL UKai CN']

    # Calculate the ideal image size
    ideal_width = min(max(df.shape[1] * base_width_per_column, min_width), max_width)
    ideal_height = min(max(df.shape[0] * base_height_per_row, min_height), max_height)

    # Create a figure and axes with the calculated size
    fig, ax = plt.subplots(figsize=(ideal_width, ideal_height))

    # Plot the DataFrame as a table
    ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')

    # Hide axes
    ax.axis('off')
    ax.axis('tight')

    # Adjust layout
    plt.tight_layout()

    # Ensure directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Full path for the image
    full_path = os.path.join(directory, file_name)

    # Save the figure as an image
    plt.savefig(full_path, dpi=dpi)

    # Return the full path of the file
    return os.path.abspath(full_path)

# Example usage
# df = pd.read_excel("path_to_your_excel_file.xlsx", engine='openpyxl', nrows=20)
# file_path = create_table_image(df, directory='/path/to/save/directory', file_name='your_output_file_name.png')
# print("Image saved at:", file_path)




# data = {
#     '车牌号': ['苏B00666D', '苏B80997', '苏B99862', '苏BA9822', '苏BM0182', '苏BM0190', '苏BM2308', '苏BM8853', '苏BM8885', '苏BR5736', '苏BR8161', '苏BW3705', '苏BW5960', '苏BY2715'],
#     '公司名称': ['无锡市绿洲接送客运服务有限公司'] * 14,
#     '状态': ['离线1天', '离线1天', '离线2天', '熄火4天', 'nan', '熄火1天', '熄火1天', 'nan', 'nan', '熄火1天', '熄火1天', '熄火1天', '离线8天', '离线5天'],
#     '问题描述': ['nan', 'nan', 'nan', 'nan', 'AV03,AV04遮挡', 'nan', 'nan', '通通道全黑屏', 'AV03摄像头需要擦拭', 'nan', 'nan', 'nan', 'nan', 'nan']
# }
if __name__ == '__main__':
    # df = pd.read_excel("/Users/panda/Desktop/github.nosync/ticketing-website/backend/data/微信服务群规则-测试.xlsx", engine='openpyxl',nrows=20)
    df = pd.read_excel("/Users/panda/Desktop/github.nosync/ticketing-website/backend/data/副本监控日志-测试.xlsx", engine='openpyxl',nrows=20)
    
    print(create_table_image(df) )
