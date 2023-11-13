from flask import Blueprint, jsonify, request
from flask_cors import CORS

from models import ticketing_system

api_bp = Blueprint('ticketing_system', __name__)
CORS(api_bp) # 解决跨域问题

#eg: http://127.0.0.1:5000/api/api_endpoint
@api_bp.route('/api_endpoint')
def api_endpoint():
    return "This is an API endpoint from api_module.py"

@api_bp.route('/add_chat_record', methods=['POST'])
def api_add_chat_record():
    try:
        chat_record_json = request.get_json()
        ticketing_system.chat_api.add_chat_record(chat_record_json)
        return jsonify({"message": "Chat record added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


# eg http://localhost:5000/api/get_chat_history/12345
@api_bp.route('/get_chat_history/<ticket_id>', methods=['GET'])
def api_get_chat_history(ticket_id):
    try:
        chats = ticketing_system.chat_api.get_chat_history(ticket_id)
        return jsonify(chats)
    except Exception as e:
        return jsonify({"error": str(e)})


# @api_bp.route('/add_ticket', methods=['POST'])
@api_bp.route('/add_ticket')
def api_add_ticket():
    try:
        # ticket_data = request.get_json()
        # 请确保根据需要创建 TicketRecord 对象并将数据传递给 add_ticket 函数
        # 例如：ticket = TicketRecord(**ticket_data)
        # 然后将 ticket 传递给 add_ticket 函数
        ticket_data = ticketing_system.ticket_api.get_test_ticket()
        print(ticket_data)
        ticketing_system.ticket_api.add_ticket(ticket_data)
        return jsonify({"message": "Ticket added successfully"})
    except Exception as e:
        return jsonify({"error": str(e)})


@api_bp.route('/get_ticket/<ticket_id>', methods=['GET'])
def api_get_ticket(ticket_id):
    try:
        ticket = ticketing_system.ticket_api.get_ticket(ticket_id)
        # 请确保将 ticket 转换为字典或使用其他方式以 JSON 格式返回
        # 例如：return jsonify(ticket.to_dict())
        return jsonify(ticket.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)})
    

@api_bp.route('/get_all_tickets', methods=['GET'])
def api_get_all_tickets():
    try:
        all_tickets = ticketing_system.ticket_api.get_all_tickets()
        # 请确保将所有票证数据转换为 JSON 格式并返回
        # 例如：return jsonify([ticket.to_dict() for ticket in all_tickets])
        return jsonify([ticket.to_dict() for ticket in all_tickets]) 
    except Exception as e:
        return jsonify({"error": str(e)})
    
    