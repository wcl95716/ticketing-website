import sys
sys.path.append("./src")

from models.ticketing_system.types.enum_type import TicketStatus


from service import flask_service
from models.ticketing_system.types import chat_record,ticket_record

import requests

def test_add_chat_record():
    url = 'http://localhost:8001/test/add_chat_record'
    data = chat_record.getTestChatMessage().to_json()
    print(data)
    response = requests.post(url, json=data)
    print(response.json())  # 注意这里使用 () 调用 json() 方法

# def test_upload_file():
#     url = 'http://localhost:5000/upload_file'
#     files = {'file': ('2.mp4', open("/Users/panda/Desktop/github.nosync/ticketing-website/backend/src/unit_testing/service/2.mp4", 'rb'))}
#     response = requests.post(url, files=files)
#     print(response.text)
    

def test_get_users():
    url = 'http://localhost:8001/test/get_users'
    response = requests.get(url)  # 使用 GET 方法发送请求
    print(response.json())
    
    
def test_get_all_tickets():
    url = 'http://localhost:8001/test/get_all_tickets'
    ticket_filter = ticket_record.TicketFilter()
    # ticket_filter.search_criteria = "121"
    ticket_filter.start_date = None
    ticket_filter.end_date = None
    ticket_filter.status = TicketStatus.NEW
    # 使用post
    response = requests.post(url, json=ticket_filter.to_dict())

    
    # print(response.json())
    
def test_add_ticket():
    url = 'http://127.0.0.1:8001/test/add_ticket'
    send_ticket = ticket_record.getTestTicket()
    
    send_ticket.ticket_id = None
    print(send_ticket.to_dict())
    response = requests.post(url, json=send_ticket.to_dict())
    print(response.json())
    pass

if __name__ == "__main__":
    # flask_service.get_app().run(host='127.0.0.1',port=5000,debug=True)
    # test_get_all_tickets()
    # test_add_chat_record()
    # test_upload_file()
    test_add_ticket()
    pass 