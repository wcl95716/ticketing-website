import mysql.connector

from models.ticketing_system.types.chat_message import ChatMessage
from models.ticketing_system.types.enum_type import MessageType



# 创建数据库连接
db_connection = mysql.connector.connect(
    host="localhost",  # 主机名或IP地址
    port=3306,          # 端口号
    user="root",        # 数据库用户名
    password="12345678",
    database="ticket_system"
)

# 创建游标
cursor = db_connection.cursor()

# 创建ChatMessage对象
message = ChatMessage(
    message_id=1,
    ticket_id=123,
    sender="John",
    content="Hello, how can I help you?",
    message_time="2023-10-28 14:30:00",
    message_type=MessageType.TEXT
)


def testChatMessage():
    # 假设 MessageType 类型有一个 value 属性表示消息类型的值
    message_type_value = message.message_type.value

    # 创建插入查询
    insert_query = "INSERT INTO chat_messages ( ticket_id, sender, content, message_time, message_type) VALUES ( %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, ( message.ticket_id, message.sender, message.content, message.message_time, message.message_type.value))

    # 提交更改
    db_connection.commit()

    # 关闭游标和数据库连接
    cursor.close()
    db_connection.close()




