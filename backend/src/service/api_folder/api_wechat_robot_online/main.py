import threading
from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for
from flask_cors import CORS
import os
import markdown2

from models import ticketing_system
from models.ticketing_system.types.ticket_record import TicketRecord
from models.ticketing_system.types.user_profile import UserProfile
from models.wechat_bot.types.chat_action_function import ChatActionFunctionFactory
from models.wechat_robot_online.api.main_api import get_log_processing, upload_img_file
from models.wechat_robot_online.types.log_processing_type import LogProcessingFilesUrl
from models.wechat_robot_online.types.robot_task_type import RobotTask, RobotTaskType
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
            if task.task_type == RobotTaskType.IMAGE_TYPE.value:
                url =  upload_img_file(task.content)
                task.content = url
            local_logger.logger.info(f"task {task.to_user} task.content = { task.content}")
        tasks_local.extend(tasks)
    pass 

def clean_tasks():
    with tasks_lock:
        tasks_local.clear()
    pass 



@api_bp.route('/add_task' , methods=['POST'])
def api_add_task():
    data = request.get_json()
    if 'to_user' not in data or 'content' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    local_logger.logger.info("process-log json : %s", data)
    # 创建LogProcessingFilesUrl对象
    task = RobotTask(
        data['to_user'],
        data['content'],
        data['task_type'],
    )
    add_tasks([task])
    return jsonify({'message': 'LogProcessingFilesUrl object received successfully'}), 200
    pass
    
@api_bp.route('/add_remind_ticket_task' , methods=['POST'])
def api_add_remind_ticket_task():
    data = request.get_json()
    if 'ticket_id' not in data :
        return jsonify({'error': 'Missing required fields'}), 400
    local_logger.logger.info("process-log json : %s", data)
    # 创建LogProcessingFilesUrl对象
    ticket_id = data['ticket_id']
    # 获取ticket
    ticket_content:TicketRecord = ticketing_system.ticket_api.get_ticket(ticket_id)
    
    if ticket_content is None:
        return jsonify({'error': 'Missing required fields'}), 400
    try:
        ticket_source = ticket_content.source
        local_logger.logger.info("ticket_source : %s", ticket_source)
        group_id = ticket_source['group_id']
        customer_id = ticket_source['customer_id']
        to_user = group_id
        content = ChatActionFunctionFactory.get_work_order_link(ticket_id , customer_id)
        task_type = RobotTaskType.TEXT_TYPE.value
        task = RobotTask(
            to_user,
            content,
            task_type,
        )
        local_logger.logger.info("add_remind_ticket_task task : %s", task.__dict__)
        add_tasks([task])
        local_logger.logger.info("add_remind_ticket_task success")
        return jsonify({'message': 'LogProcessingFilesUrl object received successfully'}), 200
    except Exception as e:
        return jsonify({'error': 'Missing required fields'}), 400
    
    return jsonify({'message': 'LogProcessingFilesUrl object received successfully'}), 200
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
    add_tasks(log_processing.get_all_robot_task_by_group())
    add_tasks(log_processing.get_all_robot_task_by_group_and_status())
    # threading.Thread(target=lambda: add_tasks(log_processing.get_all_robot_task_by_group())).start()
    # threading.Thread(target=lambda: add_tasks(log_processing.get_all_robot_task_by_group_and_status())).start()
    # 在这里可以对LogProcessingFilesUrl对象进行进一步处理，例如保存到数据库或进行其他操作
    return jsonify({'message': 'LogProcessingFilesUrl object received successfully'}), 200

def get_tasks_json():
    with tasks_lock:
        result_json = [ticket.__dict__ for ticket in tasks_local]
        tasks_local.clear()
        return result_json
    pass 

# 定义用于获取上传文件的 URL 的路由
@api_bp.route('/get_task' , methods=['GET'])
def api_get_task():
    return jsonify(get_tasks_json())
    pass 
