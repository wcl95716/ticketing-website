from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for
from flask_cors import CORS
import os
import markdown2

from models import ticketing_system
from models.ticketing_system.types.ticket_record import TicketRecord
from models.ticketing_system.types.user_profile import UserProfile
from models.wechat_robot_online.types.log_processing_type import LogProcessingFilesUrl
from utils import  local_logger

from service.api_folder.api_ticketing_system.sub_model1 import api_bp as api_bp_sub
api_bp = Blueprint('wechat_robot_online', __name__ ,url_prefix='/wechat-robot-online')

api_bp.register_blueprint(api_bp_sub)

CORS(api_bp) # 解决跨域问题

# 定义用于测试的 API 路由
@api_bp.route('/api_endpoint')
def api_endpoint():
    return "This is an API endpoint from api_module.py"



# 创建一个用于接收LogProcessingFilesUrl对象的API端点
@api_bp.route('/process-log', methods=['POST'])
def process_log():
    # 解析前端传递的JSON数据
    data = request.get_json()

    # 检查JSON中是否包含所需的字段
    if 'vehicle_data_url' not in data or 'organization_group_url' not in data or 'language_template_url' not in data:
        return jsonify({'error': 'Missing required fields'}), 400

    # 创建LogProcessingFilesUrl对象
    log_processing_files_url = LogProcessingFilesUrl(
        data['vehicle_data_url'],
        data['organization_group_url'],
        data['language_template_url']
    )

    # 在这里可以对LogProcessingFilesUrl对象进行进一步处理，例如保存到数据库或进行其他操作

    return jsonify({'message': 'LogProcessingFilesUrl object received successfully'}), 200



