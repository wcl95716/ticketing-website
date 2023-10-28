CREATE DATABASE ticket_system;

USE ticket_system;

CREATE TABLE chat_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT,
    sender VARCHAR(255),
    content TEXT,
    message_time DATETIME,
    message_type ENUM('Type1', 'Type2', 'Type3') -- 根据消息类型的枚举定义
);