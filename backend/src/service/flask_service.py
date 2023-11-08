

import json
import logging
from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

CORS(app) # 解决跨域问题
app.logger.setLevel(logging.DEBUG)

from my_service.api_folder.api_module import api_bp

app.register_blueprint(api_bp, url_prefix='/test')

@app.route('/example')
def add():
    return 'hello world'

@app.route('/post_json', methods=['POST'])
def post_json_data():
    json_data = request.json
    param_value = json_data.get('param_name')  # 替换为实际的参数名
    return f"Value from JSON data: {param_value}"

# 创建api 用于获取视频文件 传入参数为视频文件名
# example: http://get:5000/getVideo?val=1.mp4
# example: http://localhost:5000/get?val=1.mp4
@app.route('/get', methods=['GET'])
def getVideo():
    # 添加默认参数
    val = request.args.get('val', default='test_val')
    return val
    pass

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
    #app.run(host='192.168.0.108',port=5000,debug=False)