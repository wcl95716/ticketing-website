CREATE DATABASE ticket_system;

USE ticket_system;

CREATE TABLE chat_messages (
    message_id INT AUTO_INCREMENT PRIMARY KEY,
    ticket_id INT,
    sender VARCHAR(255),
    content TEXT,
    message_time DATETIME,
    message_type INT,
    INDEX idx_ticket_id (ticket_id),
    INDEX idx_message_time (message_time),
    INDEX idx_sender (sender)
);
