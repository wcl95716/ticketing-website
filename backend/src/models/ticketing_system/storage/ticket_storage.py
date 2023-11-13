import os
import json

from models.ticketing_system.types.ticket_record import TicketRecord


data_path = "data/work_order_logs"

def save_ticket_to_file(ticket: TicketRecord):
    # 创建工单文件夹（如果不存在）
    folder_path = os.path.join(data_path, str(ticket.ticket_id))
    os.makedirs(folder_path, exist_ok=True)

    # 创建工单数据文件
    file_path = os.path.join(folder_path, "ticket_data.json")

    try:
        # 将工单数据写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(ticket.to_dict(), file, indent=4 ,ensure_ascii=False)  # 缩进格式化写入 JSON 文件

        print(f"工单数据已存储到文件 {file_path}")
    except Exception as e:
        print(f"存储工单数据时发生错误：{str(e)}")
        
def update_ticket_record_in_file(ticket: TicketRecord):
    folder_path = os.path.join(data_path, str(ticket.ticket_id))
    file_path = os.path.join(folder_path, "ticket_data.json")

    try:
        # 如果文件不存在，返回 None
        if not os.path.exists(file_path):
            print(f"工单数据文件不存在：{file_path}")
            return

        # 将工单数据写入文件
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(ticket.to_dict(), file, indent=4, ensure_ascii=False)  # 缩进格式化写入 JSON 文件

        print(f"工单数据已更新并存储到文件 {file_path}")
    except Exception as e:
        print(f"更新工单数据时发生错误：{str(e)}")


def get_ticket_record_from_file(ticket_id: str) -> TicketRecord :
    folder_path = os.path.join(data_path, str(ticket_id))
    file_path = os.path.join(folder_path, "ticket_data.json")

    try:
        # 如果文件不存在，返回 None
        if not os.path.exists(file_path):
            return None

        # 读取工单数据文件
        with open(file_path, 'r', encoding='utf-8') as file:
            ticket_data = json.load(file)

        # 创建工单对象并返回
        ticket = TicketRecord.from_dict(ticket_data)
        return ticket
    except Exception as e:
        print(f"读取工单数据时发生错误：{str(e)}")
        return None


def get_all_ticket_record_from_files() -> list[TicketRecord]:
    ticket_list:list[TicketRecord] = []
    try:
        # 获取 data_path 下的所有文件夹（每个文件夹代表一个工单）
        for folder_name in os.listdir(data_path):
            folder_path = os.path.join(data_path, folder_name)
            
            # 确保是文件夹并且包含 ticket_data.json 文件
            if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, "ticket_data.json")):
                # 读取工单数据
                ticket = get_ticket_record_from_file(folder_name)
                
                if ticket:
                    ticket_list.append(ticket)
    except Exception as e:
        print(f"读取所有工单数据时发生错误：{str(e)}")
    
    return ticket_list



def delete_ticket_record(ticket_id: str):
    folder_path = os.path.join(data_path, str(ticket_id))

    try:
        # 如果文件夹不存在，返回 None
        if not os.path.exists(folder_path):
            print(f"工单数据文件夹不存在：{folder_path}")
            return

        # 删除工单数据文件夹及其内容
        for root, dirs, files in os.walk(folder_path, topdown=False):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                os.remove(file_path)
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                os.rmdir(dir_path)

        # 删除工单数据文件夹
        os.rmdir(folder_path)
        print(f"工单数据文件夹及其内容已删除：{folder_path}")
    except Exception as e:
        print(f"删除工单数据时发生错误：{str(e)}")