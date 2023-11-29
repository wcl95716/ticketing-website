import threading
from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for
from flask_cors import CORS
import os
import markdown2

from models import ticketing_system
from models.ticketing_system.types.ticket_record import TicketRecord
from models.ticketing_system.types.user_profile import UserProfile
from models.wechat_robot_online.api.main_api import get_log_processing, upload_img_file
from models.wechat_robot_online.types.log_processing_type import LogProcessingFilesUrl
from models.wechat_robot_online.types.robot_task_type import RobotTask
from utils import  local_logger

from service.api_folder.api_ticketing_system.sub_model1 import api_bp as api_bp_sub
api_bp = Blueprint('wechat_robot_online', __name__ ,url_prefix='/wechat_robot_online')

api_bp.register_blueprint(api_bp_sub)

CORS(api_bp) # 解决跨域问题

# 定义用于测试的 API 路由
@api_bp.route('/api_endpoint')
def api_endpoint():
    return "This is an API endpoint from api_module.py"


tasks_local:list[RobotTask] = []
# 创建一个锁对象
tasks_lock = threading.Lock()

def add_tasks(tasks:list[RobotTask]):
    # 在修改 tasks_local 列表之前获取锁
    with tasks_lock:
        
        for task in tasks:
            url =  upload_img_file(task.content)
            task.content = url
            local_logger.logger.info(f"task {task.to_user} task.content = { task.content}")
        tasks_local.extend(tasks)
    pass 

def clean_tasks():
    with tasks_lock:
        tasks_local.clear()
    pass 

def get_tasks_json():
    with tasks_lock:
        result_json = jsonify([ticket.__dict__ for ticket in tasks_local])
        tasks_local.clear()
        return result_json
    pass 
    

# 创建一个用于接收LogProcessingFilesUrl对象的API端点
@api_bp.route('/process_log', methods=['POST'])
def api_process_log():
    # 解析前端传递的JSON数据
    data = request.get_json()

    # 检查JSON中是否包含所需的字段
    if 'vehicle_data_url' not in data or 'organization_group_url' not in data or 'language_template_url' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    local_logger.logger.info("process-log json : %s", data)
    # 创建LogProcessingFilesUrl对象
    log_processing_files_url = LogProcessingFilesUrl(
        data['vehicle_data_url'],
        data['organization_group_url'],
        data['language_template_url']
    )
    
    log_processing = get_log_processing(log_processing_files_url.vehicle_data_url , log_processing_files_url.organization_group_url)
    
    local_logger.logger.info("get_class")
    # add_tasks(log_processing.get_all_robot_task())
    threading.Thread(target=lambda: add_tasks(log_processing.get_all_robot_task())).start()
    
    # 在这里可以对LogProcessingFilesUrl对象进行进一步处理，例如保存到数据库或进行其他操作
    return jsonify({'message': 'LogProcessingFilesUrl object received successfully'}), 200


# 定义用于获取上传文件的 URL 的路由
@api_bp.route('/get_task' , methods=['GET'])
def api_get_task():
    return jsonify(get_tasks_json())
    pass 
