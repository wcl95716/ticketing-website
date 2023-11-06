import mysql.connector
from mysql.connector import pooling

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
connection_pool = pooling.MySQLConnectionPool(pool_name="chat_pool", pool_size=5, **db_connection)

def close_connection_pool():
    # 关闭连接池
    connection_pool.close()


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

def insert_message():
    try:
        # 从连接池获取连接
        connection = connection_pool.get_connection()

        # 创建一个游标对象
        cursor = connection.cursor()


        # 创建插入查询
        insert_query = "INSERT INTO chat_messages ( ticket_id, sender, content, message_time, message_type) VALUES ( %s, %s, %s, %s, %s)"
        cursor.execute(insert_query, ( message.ticket_id, message.sender, message.content, message.message_time, message.message_type.value))

        # 提交更改
        connection.commit()

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        # 释放连接回连接池
        if connection:
            cursor.close()
            connection.close()

# 示例插入数据
insert_message()





