import React, { useState, useEffect } from 'react';
import { Input, Button, List, message, Upload, Modal, Row, Col, Image } from 'antd';
import { PictureOutlined, UploadOutlined, PlusOutlined } from '@ant-design/icons';
import Style from '../components/DetailModel.module.less';
import type { RcFile, UploadProps } from 'antd/es/upload';
import { useLocation } from 'react-router-dom';
import type { UploadFile } from 'antd/es/upload/interface';
import SearchForm from './SearchForm';

const { TextArea } = Input;


const getBase64 = (file: RcFile): Promise<string> =>
   new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = (error) => reject(error);
   });
const DetailModel = () => {
   const location = useLocation();
   const { key } = location.state || {};
   const addTicket = async (newMessageContent) => {
      try {
        const response = await fetch('http://47.103.45.149:5000/test/add_ticket', {
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
    const handleSendMessage = () => {
      if (newMessage.trim() !== '') {
        addTicket(newMessage.trim()); // 调用addTicket函数发送新消息
        setNewMessage(''); // 清空输入框
      }
    };
    
    const handleUpload = (file: RcFile) => {
      getBase64(file).then(base64 => {
        const fileMessage = {
          id: messages.length + 1,
          img: base64, // 假设我们发送base64编码的图片文件
          // ...其他属性，如时间戳、发送者等
        };
        addTicket(fileMessage); // 发送文件消息
      });
    };
    const fetchMessages = async () => {
      if (key) {
        try {
          const response = await fetch(`http://47.103.45.149:5000/test/get_all_tickets/${key}`);
          const data = await response.json();
          setMessages(data); // 更新消息列表
        } catch (error) {
          console.error("Error fetching messages:", error);
          message.error('获取消息列表失败');
        }
      }
    };
    useEffect(() => {
      fetchMessages();
    }, [key]);
    
   useEffect(() => {
      if (key) {
        const fetchTickets = async () => {
          try {
            const response = await fetch(`http://47.103.45.149:5000/test/get_all_tickets/${key}`);
            const data = await response.json();
            // 如果接口返回的是消息数组，直接用setMessages更新状态
            setMessages(data);
          } catch (error) {
            console.error("Error fetching tickets:", error);
            message.error('获取数据失败'); // 可以使用Ant Design的message组件提示用户
          }
        };
  
        fetchTickets();
      }
    }, [key]);
  
   const [messages, setMessages] = useState(
      [
         { id: 1, text: '你说什么', avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png', sender: '用户名1', time: '1970-03-04 14:23:44' },
         { id: 2, text: '3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333', avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png', sender: '用户名2', time: '1970-03-04 14:23:44' },
         { id: 3, img: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png', avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png', sender: '用户名3', time: '1970-03-04 14:23:44' },
         { id: 3, video: ' https://profilesys.yangwangauto.com/upload-file/yangwang-personal-center/test/ed0c48be8636461e9e4d0e0272c66c3a.mp4', avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png', sender: '用户名4', time: '1970-03-04 14:23:44' },
      ]
   );
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
      //假上传
      // file.status = 'done'
      handleUpload(file.originFileObj as RcFile);
      //接口备用
      // if (file.status === 'done') {
      //    handleUpload(file.originFileObj as RcFile);
      // }
   };

   const props = {
      action: 'https://run.mocky.io/v3/435e224c-44fb-4773-9faf-380c5e6a2188',
      onChange: handleChange,
      // multiple: true,
   };

   return (
      <div>
         <Row justify='start' style={{ marginBottom: '20px' }}>
            <SearchForm
               onSubmit={async (value) => {
                  console.log(value);
               }}
               onCancel={() => { }}
            />
         </Row>
         <div style={{ width: '100%', backgroundColor: '#fff' }}>
            <div>沟通记录</div>
            <List
               dataSource={messages}
               renderItem={renderMessageItem}  // 使用修改后的renderItem函数
            />
            <div className={Style['chat-input']}>
               <Row justify="space-between" align="middle">
                  <Col flex="auto">
                     <TextArea
                        style={{ width: '800px' }}
                        placeholder="请输入聊天内容"
                        value={newMessage}
                        onChange={(e: any) => setNewMessage(e.target.value)}
                        autoSize={{ minRows: 3, maxRows: 6 }}
                     />
                  </Col>
                  <Col>
                     <Button type='primary' onClick={handleSendMessage}>发送</Button>
                  </Col>
                  <Col>
                     <Upload {...props} showUploadList={false}>
                        <Button icon={<UploadOutlined />}>上传文件</Button>
                     </Upload>
                  </Col>
               </Row>
            </div>
         </div>
      </div>
   );
};

export default DetailModel;