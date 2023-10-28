from flask import Blueprint, request

api_bp = Blueprint('test', __name__)

#eg: http://127.0.0.1:5000/api/api_endpoint
@api_bp.route('/api_endpoint')
def api_endpoint():
    return "This is an API endpoint from api_module.py"

