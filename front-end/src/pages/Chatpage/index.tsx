import React, { useState, useEffect } from 'react';
import { Input, Button, List, message, Upload, Modal, Row, Col, Image } from 'antd';
import { PictureOutlined, UploadOutlined, PlusOutlined } from '@ant-design/icons';
import Style from './index.module.less';
import type { RcFile, UploadProps } from 'antd/es/upload';
import { useLocation } from 'react-router-dom';
import type { UploadFile } from 'antd/es/upload/interface';

const { TextArea } = Input;


const getBase64 = (file: RcFile): Promise<string> =>
    new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result as string);
        reader.onerror = (error) => reject(error);
    });
const PChart = () => {
    const location = useLocation();
    const { ticket_id } = location.state || {};
    console.log("传输进来key", ticket_id)
    const fetchMessages = async () => {
        if (ticket_id) {
            try {
                const response = await fetch(`http://47.103.45.149:8001/test/get_all_tickets/${ticket_id}`);
                const data = await response.json();
                setMessages(data); // 更新消息列表
            } catch (error) {
                console.error("Error fetching messages:", error);
                message.error('获取消息列表失败');
            }
        }
    };
    // useEffect(() => {
    //    fetchMessages();
    // }, [ticket_id]);

    const addTicket = async (newMessageContent: any) => {
        try {
            const response = await fetch('http://47.103.45.149:8001/test/add_ticket', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: newMessageContent }),
            });

            if (!response.ok) throw new Error('Network response was not ok.');
            // 假设POST请求成功后立即调用GET请求更新列表
            fetchMessages();
        } catch (error) {
            console.error("Error posting new ticket:", error);
            message.error('发送消息失败');
        }
    };

    const [messages, setMessages] = useState([
        { id: 1, text: '你好，有什么可以帮你的？', avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png', sender: '用户名1', time: '1970-03-04 14:23:44' },

    ]);
    const [newMessage, setNewMessage] = useState('');
    const handleSendMessage = () => {
        console.log("输出当前输入的内容", messages, newMessage.trim)
        if (newMessage.trim() !== '') {
            const updatedMessages = [
                ...messages,
                {
                    id: messages.length + 1,
                    text: newMessage,
                    avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
                    time: '1970-03-04 14:23:44',
                    sender: '当前用户'
                }
            ];
            setMessages(updatedMessages);
            setNewMessage(''); // 清空输入框
        }
    };
    const handleUpload = (file: RcFile) => {
        const updatedMessages = [
            ...messages,
            {
                id: 123,
                time: '1970-03-04 14:23:44',
                img: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
                avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
                sender: '当前用户'
            }
        ];
        setMessages(updatedMessages);
        setNewMessage(''); // 清空输入框
    };
    // 修改renderItem函数，为每条消息添加头像和名字
    const renderMessageItem = (item: any) => {
        if (item.img) {
            return <div>
                <div className={`${Style['message-item']} ${item.sender === '当前用户' ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
                    {item.sender !== '当前用户' && (  // 当消息不是当前用户发送时
                        <div className={Style['avatar']}>
                            <img src={item.avatar} alt="avatar" />
                            <p>{item.sender}</p>
                        </div>
                    )}
                    <div className={Style['message-content']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                        <p className={Style['message-time']} style={{ textAlign: item.sender === '当前用户' ? 'right' : 'left' }}>{item.time}</p>
                        <div className={Style['text']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                            <Image alt={item.id} src={item.img} style={{ width: 100, height: 100, objectFit: 'cover' }} />
                        </div>
                    </div>
                    {item.sender === '当前用户' && (  // 当消息是当前用户发送时
                        <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                            <img src={item.avatar} alt="avatar" />
                            <p>{item.sender}</p>
                        </div>
                    )}
                </div>
            </div>
        } else if (item.video) {
            return <div>
                <div className={`${Style['message-item']} ${item.sender === '当前用户' ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
                    {item.sender !== '当前用户' && (  // 当消息不是当前用户发送时
                        <div className={Style['avatar']}>
                            <img src={item.avatar} alt="avatar" />
                            <p>{item.sender}</p>
                        </div>
                    )}
                    <div className={Style['message-content']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                        <p className={Style['message-time']} style={{ textAlign: item.sender === '当前用户' ? 'right' : 'left' }}>{item.time}</p>
                        <div className={Style['text']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                            <video controls src={item.video} style={{ width: 100 }} />
                        </div>
                    </div>

                    {item.sender === '当前用户' && (  // 当消息是当前用户发送时
                        <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                            <img src={item.avatar} alt="avatar" />
                            <p>{item.sender}</p>
                        </div>
                    )}
                </div>
            </div>
        }
        return (
            <div>
                <div className={`${Style['message-item']} ${item.sender === '当前用户' ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
                    {item.sender !== '当前用户' && (  // 当消息不是当前用户发送时
                        <div className={Style['avatar']}>
                            <img src={item.avatar} alt="avatar" />
                            <p>{item.sender}</p>
                        </div>
                    )}
                    <div className={Style['message-content']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                        <p className={Style['message-time']} style={{ textAlign: item.sender === '当前用户' ? 'right' : 'left' }}>{item.time}</p>
                        <div className={Style['text']}>
                            <p>{item.text}</p>
                        </div>
                    </div>
                    {item.sender === '当前用户' && (  // 当消息是当前用户发送时
                        <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                            <img src={item.avatar} alt="avatar" />
                            <p>{item.sender}</p>
                        </div>
                    )}
                </div>
            </div>
        );
    }

    const handleChange: UploadProps['onChange'] = ({ file }) => {
        handleUpload(file.originFileObj as RcFile);
    };

    const props = {
        action: 'https://run.mocky.io/v3/435e224c-44fb-4773-9faf-380c5e6a2188',
        onChange: handleChange,
        // multiple: true,
    };

    return (
        <div style={{ backgroundColor: '#fff', height: '100vh', padding: '10px', display: 'flex', flexDirection: 'column' }}>
            <List
                dataSource={messages}
                renderItem={renderMessageItem}  // 使用修改后的renderItem函数
            />
            <div className={Style['chat-input']} style={{ marginTop: 'auto', padding: '10px' }}>
                <div style={{ display: 'flex', width: '100%' }}>
                    <Input
                        style={{ flex: 1, marginRight: '10px' }}
                        placeholder="请输入聊天内容"
                        suffix={<Button type='primary' onClick={handleSendMessage}>发送</Button>}
                        value={newMessage}
                        onChange={(e: any) => setNewMessage(e.target.value)}
                    />
                    <Upload {...props} showUploadList={false}>
                        <Button style={{ flex: '0 0 auto' }} shape="circle" icon={<PlusOutlined style={{ color: 'grey' }} />} />
                    </Upload>
                </div>
                {/* <Button type='primary' onClick={handleSendMessage} style={{ width: '100%', marginTop: '10px' }}>发送</Button> */}
            </div>
        </div>
        // <div style={{ backgroundColor: '#fff', height: '100vh', padding: '10px' }}>
        //    <div style={{ marginBottom: '10px' }}>沟通记录</div>
        //    <List
        //       dataSource={messages}
        //       renderItem={renderMessageItem}  // 使用修改后的renderItem函数
        //    />
        //    <div className={Style['chat-input']} style={{ position: 'fixed', bottom: 0, width: '100%', padding: '10px' }}>
        //       <Row align="middle">
        //          <Col flex={3} style={{ marginRight: '10px' }}>
        //             <Input
        //                placeholder="请输入聊天内容"
        //                suffix={<Button type='primary' onClick={handleSendMessage}>发送</Button>}
        //                value={newMessage}
        //                onChange={(e: any) => setNewMessage(e.target.value)}
        //             />
        //          </Col>
        //          <Col>
        //             <Upload {...props} showUploadList={false}>
        //                <Button shape="circle" icon={<PlusOutlined style={{ color: 'grey' }} />} />
        //             </Upload>
        //          </Col>
        //       </Row>
        //    </div>
        // </div>
    );
};

export default PChart;