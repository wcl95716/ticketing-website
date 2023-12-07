
from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for

from flask_cors import CORS
import os
import markdown2
import pandas as pd

from models import ticketing_system
from models.ticketing_system.types.ticket_record import TicketRecord
from models.ticketing_system.types.user_profile import UserProfile
from utils import  local_logger

from service.api_folder.api_ticketing_system.sub_model1 import api_bp as api_bp_sub
api_bp = Blueprint('ticketing_system', __name__ ,url_prefix='/test')

api_bp.register_blueprint(api_bp_sub)

# 配置文件上传目录和允许的文件扩展名
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt','xlsx','csv', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'mp4', 'webm', 'ogg', 'mov'}

# 辅助函数，检查文件扩展名是否允许
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

CORS(api_bp) # 解决跨域问题

# 定义用于测试的 API 路由
@api_bp.route('/api_endpoint')
def api_endpoint():
    return "This is an API endpoint from api_module.py"


# 添加聊天记录的接口
@api_bp.route('/add_chat_record', methods=['POST'])
def api_add_chat_record():
    try:
        local_logger.logger.info("add_chat_record begin ")
        chat_record_json = request.get_json()
        local_logger.logger.info("add_chat_record json : %s", chat_record_json)
        ticketing_system.chat_api.add_chat_record(chat_record_json)
        local_logger.logger.info("api_add_chat_record  successfully")
        return jsonify({"message": "Chat record added successfully"})
    except Exception as e:
        local_logger.logger.info("api_add_chat_record error : %s", str(e))
        return jsonify({"error": str(e)})


# 获取聊天记录的接口
@api_bp.route('/get_chat_history/<ticket_id>', methods=['GET'])
def api_get_chat_history(ticket_id):
    try:
        chats = ticketing_system.chat_api.get_chat_history(ticket_id)
        if chats is None:
            return jsonify({"error": "No chat history found"})
        local_logger.logger.info("api_get_chat_history  successfully")
        return jsonify(chats)
    except Exception as e:
        return jsonify({"error": str(e)})


# 添加工单的接口
@api_bp.route('/add_test_ticket')
def api_add_ticket_test():
    try:
        # ticket_data = request.get_json()
        # 请确保根据需要创建 TicketRecord 对象并将数据传递给 add_ticket 函数
        # 例如：ticket = TicketRecord(**ticket_data)
        # 然后将 ticket 传递给 add_ticket 函数
        ticket_data = ticketing_system.ticket_api.get_test_ticket()
        local_logger.logger.info(ticket_data)
        ticketing_system.ticket_api.add_ticket(ticket_data)
        return jsonify({"message": "Ticket added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


# 修改工单的接口
@api_bp.route('/update_ticket', methods=['POST'])
def api_update_ticket():
    try:
        ticket_data = request.get_json()
        local_logger.logger.info("ticket_data : %s", ticket_data)
        ticketing_system.ticket_api.update_ticket(ticket_data)
        return jsonify({"message": "Ticket updated successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


# 获取一个工单的接口
@api_bp.route('/get_ticket/<ticket_id>', methods=['GET'])
def api_get_ticket(ticket_id):
    try:
        ticket = ticketing_system.ticket_api.get_ticket(ticket_id)
        # 请确保将 ticket 转换为字典或使用其他方式以 JSON 格式返回
        # 例如：return jsonify(ticket.to_dict())
        return jsonify(ticket.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

# 删除工单的接口
@api_bp.route('/delete_ticket/<ticket_id>', methods=['GET'])
def api_delete_ticket(ticket_id):
    try:
        ticketing_system.ticket_api.delete_ticket(ticket_id)
        
        return jsonify({"message": "delete_ticket successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


# 获取所有工单的接口
@api_bp.route('/get_all_tickets', methods=['POST'])
def api_get_all_tickets():
    local_logger.logger.info("api_get_all_tickets begin ")
    try:
        ticket_filter_data = request.get_json()
        local_logger.logger.info("ticket_filter_data : %s", ticket_filter_data)
        # 如果没有传递任何筛选条件，则返回所有工单
        if not ticket_filter_data:
            all_tickets = ticketing_system.ticket_api.get_all_tickets()
            local_logger.logger.info("all_tickets : %d ", len(all_tickets))
            return jsonify([ticket.to_dict() for ticket in all_tickets])
        # 如果传递了筛选条件，则返回符合条件的工单
        result = ticketing_system.ticket_api.get_ticket_filter(ticket_filter_data)
        local_logger.logger.info("ticket_filter result : %d ", len(result))
        return jsonify([ticket.to_dict() for ticket in result])
        # all_tickets = ticketing_system.ticket_api.get_all_tickets()
        # # 请确保将所有票证数据转换为 JSON 格式并返回
        # # 例如：return jsonify([ticket.to_dict() for ticket in all_tickets])
        # return jsonify([ticket.to_dict() for ticket in all_tickets]) 
    except Exception as e:
        local_logger.logger.info("api_get_all_tickets error : %s", str(e))
        return jsonify({"error": str(e)})
    
# 添加工单的接口
@api_bp.route('/add_ticket', methods=['POST'])
def api_add_ticket():
    try:
        ticket_data = request.get_json()
        all_tickets = ticketing_system.ticket_api.get_all_tickets()
        for ticket in all_tickets:
            if ticket.creator == ticket_data["creator"]:
                 return  jsonify(ticket.to_dict())
        local_logger.logger.info("ticket_data : %s", ticket_data)
        ticket:TicketRecord = ticketing_system.ticket_api.add_ticket(ticket_data)
        #return jsonify({"message": "Ticket updated successfully"})
        return  jsonify(ticket.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

import os
import requests

@api_bp.route('/download_all_tickets', methods=['POST'])
def api_download_all_tickets():
    # 调用上传文件接口
    upload_url = "http://47.116.201.99:8001/test/upload_file"  # 替换为您的上传文件的接口URL
    try:
        ticket_filter_data = request.get_json()
        local_logger.logger.info("ticket_filter_data : %s", ticket_filter_data)
        # 如果没有传递任何筛选条件，则返回所有工单
        if not ticket_filter_data:
            all_tickets = ticketing_system.ticket_api.get_all_tickets()
            local_logger.logger.info("all_tickets : %d ", len(all_tickets))
            # 将数据转换为DataFrame
            df = pd.DataFrame([ticket.to_dict() for ticket in all_tickets])
            # 创建一个Excel文件并保存在当前路径下
            excel_file_path = "all_tickets.xlsx"
            df.to_excel(excel_file_path, index=False)
            

            files = {"file": open(excel_file_path, "rb")}
            response = requests.post(upload_url, files=files)
            
            if response.status_code == 200:
                file_info = response.json()
                file_url = file_info.get("file_url")
                return jsonify({'message': 'File uploaded successfully', 'file_url': file_url})
            
        # 如果传递了筛选条件，则返回符合条件的工单
        result = ticketing_system.ticket_api.get_ticket_filter(ticket_filter_data)
        local_logger.logger.info("ticket_filter result : %d ", len(result))
        # 将数据转换为DataFrame
        df = pd.DataFrame([ticket.to_dict() for ticket in result])
        # 创建一个Excel文件并保存在当前路径下
        excel_file_path = "filtered_tickets.xlsx"
        df.to_excel(excel_file_path, index=False)
        
        files = {"file": open(excel_file_path, "rb")}
        response = requests.post(upload_url, files=files)
        
        if response.status_code == 200:
            file_info = response.json()
            file_url = file_info.get("file_url")
            return jsonify({'message': 'File uploaded successfully', 'file_url': file_url})
            
    except Exception as e:
        local_logger.logger.info("api_get_all_tickets error : %s", str(e))
        return jsonify({"error": str(e)})


    
# 上传文件的接口
@api_bp.route('/upload_file', methods=['POST'])
def api_upload_file():
    
    local_logger.logger.info("upload_file begin ")
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No selected file'})
    
    local_logger.logger.info(f"upload_file save begin file.filename={file.filename}")
    if file and allowed_file(file.filename):
        file_name = ticketing_system.chat_api.upload_file(file)
        # 构造文件的 URL
        local_logger.logger.info("upload_file done file_name : %s", file_name)
        file_url = "http://47.116.201.99:8001/test/uploads/" + file_name

        return jsonify({'message': 'File uploaded successfully', 'file_id': file_name, 'file_url':file_url})
    return jsonify({'error': 'File upload failed'})

# api_bp = Blueprint('ticketing_system', __name__)
# CORS(api_bp) # 解决跨域问题

# 定义用于获取上传文件的 URL 的路由
@api_bp.route('/uploads/<filename>')
def api_get_file(filename):
    local_logger.logger.info("filename : %s", filename)
    file_path = ticketing_system.chat_api.get_file(filename)
    local_logger.logger.info("file_path : %s", file_path)
    return send_file(file_path)



@api_bp.route('/get_users' , methods=['GET'])
def api_get_users():
    try:
        users:list[dict] = ticketing_system.user_api.get_users()
        local_logger.logger.info("api_get_users %s ", users)
        # 请确保将所有票证数据转换为 JSON 格式并返回
        return jsonify(users) 
    except Exception as e:
        return jsonify({"error": str(e)})
    
@api_bp.route('/get_user/<user_id>', methods=['GET'])
def api_get_user(user_id):
    try:
        user:UserProfile = ticketing_system.user_api.get_user(user_id)
        # 请确保将 ticket 转换为字典或使用其他方式以 JSON 格式返回
        # 例如：return jsonify(ticket.to_dict())
        return jsonify(user.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})

# 添加更新用户接口
@api_bp.route('/update_user', methods=['POST'])
def api_update_user():
    try:
        user_data = request.get_json()
        local_logger.logger.info("user_data : %s", user_data)
        ticketing_system.user_api.update_user(user_data)
        return jsonify({"message": "User updated successfully"})
    except Exception as e:
        local_logger.logger.info("api_update_user error : %s", str(e))
        return jsonify({"error": str(e)})


@api_bp.route('/readme')
def api_get_readme():
    try:
        # 指定README.md文件的路径
        readme_file = 'src/service/api_folder/api_ticketing_system/readme.md'
        # 读取README.md文件内容
        with open(readme_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()

        # 使用markdown2库将Markdown转换为HTML
        html_content = markdown2.markdown(markdown_content)

        # 渲染HTML内容
        return render_template('markdown_template.html', content=html_content)
    except Exception as e:
        return str(e)
    