

import json
import logging
from flask import Flask, request, send_file, send_from_directory
from flask_cors import CORS

app = Flask(__name__,template_folder='templates')

CORS(app) # 解决跨域问题
app.logger.setLevel(logging.DEBUG)

from service.api_folder.api_ticketing_system import api_bp as api_ticketing_system

app.register_blueprint(api_ticketing_system, url_prefix=api_ticketing_system.url_prefix)

def get_app():
    return app

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=5000,debug=True)
    #app.run(host='192.168.0.108',port=5000,debug=False)