import mysql.connector
from src.models.types import MessageType

from src.models.chat_message import ChatMessage

# 创建数据库连接
db_connection = mysql.connector.connect(
    host="root@localhost:3306",
    user="root",
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

# 插入数据
insert_query = "INSERT INTO chat_messages (message_id, ticket_id, sender, content, message_time, message_type) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.execute(insert_query, (message.message_id, message.ticket_id, message.sender, message.content, message.message_time, message.message_type))

# 提交更改
db_connection.commit()

# 关闭游标和数据库连接
cursor.close()
db_connection.close()




