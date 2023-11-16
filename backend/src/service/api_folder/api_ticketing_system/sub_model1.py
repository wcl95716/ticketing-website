from flask import Blueprint, current_app, jsonify, request, send_file, render_template, url_for
from flask_cors import CORS
import os


api_bp = Blueprint('ticketing_system', __name__)

CORS(api_bp) # 解决跨域问题

# 定义用于测试的 API 路由
@api_bp.route('/api_endpoint_sub')
def api_endpoint():
    return "This is an API endpoint from api_module.py"


