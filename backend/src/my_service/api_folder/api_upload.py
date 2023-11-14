from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os

# 创建名为 'upload' 的蓝图
upload_bp = Blueprint('upload', __name__)

# 配置文件上传目录和允许的文件扩展名
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

# 辅助函数，检查文件扩展名是否允许
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 创建文件上传的路由
@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        # 为上传的文件生成一个安全的新文件名
        filename = secure_filename(file.filename)
        # 保存上传的文件到指定目录
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        return jsonify({'message': 'File uploaded successfully'})

    return jsonify({'error': 'File upload failed'})


# 在 Flask 应用中注册蓝图
from flask import Flask, request, send_file, send_from_directory
app = Flask(__name__)
app.register_blueprint(upload_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
