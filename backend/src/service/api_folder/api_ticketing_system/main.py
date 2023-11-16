from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for
from flask_cors import CORS
import os

from models import ticketing_system
from models.ticketing_system.types.user_profile import UserProfile
from utils import  local_logger

from service.api_folder.api_ticketing_system.sub_model1 import api_bp as api_bp_sub
api_bp = Blueprint('ticketing_system', __name__ ,url_prefix='/test')

api_bp.register_blueprint(api_bp_sub)


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
        return jsonify({"error": str(e)})


# 获取聊天记录的接口
@api_bp.route('/get_chat_history/<ticket_id>', methods=['GET'])
def api_get_chat_history(ticket_id):
    try:
        chats = ticketing_system.chat_api.get_chat_history(ticket_id)
        local_logger.logger.info("api_get_chat_history  successfully")
        return jsonify(chats)
    except Exception as e:
        return jsonify({"error": str(e)})


# 添加工单的接口
@api_bp.route('/add_ticket')
def api_add_ticket():
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
@api_bp.route('/get_all_tickets', methods=['GET'])
def api_get_all_tickets():
    try:
        all_tickets = ticketing_system.ticket_api.get_all_tickets()
        # 请确保将所有票证数据转换为 JSON 格式并返回
        # 例如：return jsonify([ticket.to_dict() for ticket in all_tickets])
        return jsonify([ticket.to_dict() for ticket in all_tickets]) 
    except Exception as e:
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
    
    local_logger.logger.info("upload_file save begin ")
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
        local_logger.logger.info("api_get_users  ", users)
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