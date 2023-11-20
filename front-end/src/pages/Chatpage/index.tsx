import React, { useState, useEffect } from 'react';
import { Input, Button, List, message, Upload, Modal, Row, Col, Image } from 'antd';
import { PictureOutlined, UploadOutlined, PlusOutlined } from '@ant-design/icons';
import Style from './index.module.less';
import dayjs, { Dayjs } from 'dayjs';
import { IChatRecord, MessageType, ChatPriority } from 'models/ticketing-website/index.type';
import type { RcFile, UploadProps } from 'antd/es/upload';
import { useLocation, useParams } from 'react-router-dom';
import {
   getTicketListRequest,
   getChatRequest,
   getUserDetail,
   postChatRequest,
   selectTicketRecordList,
   selecChatRecord,
   selecUserDetail,
} from 'models/ticketing-website/index.model';
import { useAppDispatch, useAppSelector } from 'modules/store';
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
   const dispatch = useAppDispatch();
   const chatRecord = useAppSelector(selecChatRecord);

   const location = useLocation();
   const queryParams = new URLSearchParams(location.search);
   const ticket_id = queryParams.get('ticket_id');
   const user_id = queryParams.get('user_id');

   const now = new Date();
   
   //  const fetchMessages = async () => {
   //      if (ticket_id) {
   //          try {
   //              const response = await fetch(`http://47.103.45.149:8001/test/get_all_tickets/${ticket_id}`);
   //              const data = await response.json();
   //              setMessages(data); // 更新消息列表
   //          } catch (error) {
   //              console.error("Error fetching messages:", error);
   //              message.error('获取消息列表失败');
   //          }
   //      }
   //  };

   //  const addTicket = async (newMessageContent: any) => {
   //      try {
   //          const response = await fetch('http://47.103.45.149:8001/test/add_ticket', {
   //              method: 'POST',
   //              headers: {
   //                  'Content-Type': 'application/json',
   //              },
   //              body: JSON.stringify({ message: newMessageContent }),
   //          });

   //          if (!response.ok) throw new Error('Network response was not ok.');
   //          // 假设POST请求成功后立即调用GET请求更新列表
   //          fetchMessages();
   //      } catch (error) {
   //          console.error("Error posting new ticket:", error);
   //          message.error('发送消息失败');
   //      }
   //  };
   useEffect(() => {
      if (ticket_id) {
         dispatch(getChatRequest(ticket_id))
      }
   }, [ticket_id]);

   useEffect(() => {
      setMessages(chatRecord);
   }, [chatRecord]);

   const [messages, setMessages] = useState([
      {
         ticket_id: ticket_id,
         text: '你好，有什么可以帮你的？可以在此留言',
         avatar: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
         sender: '系统消息',
         time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
         chat_profile: ChatPriority.SERVICE,
      },

   ]);
   const [newMessage, setNewMessage] = useState('');
   const handleSendMessage = () => {
      if (newMessage.trim() !== '') {
         const newMessages = [
            ...messages,
            {

               ticket_id: ticket_id,
               message_id: '',
               content: newMessage.trim(),
               message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
               sender: "用户1",
               message_type: MessageType.TEXT,
               chat_profile: ChatPriority.CUSTOMER,
               avatar_url: "https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png",
            }
         ];
         setMessages(newMessages);

         const updatedMessages = {
            ticket_id: ticket_id,
            message_id: '',
            content: newMessage.trim(),
            message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
            sender: "用户1",
            message_type: MessageType.TEXT,
            chat_profile: ChatPriority.CUSTOMER,
            avatar_url: "https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png",
         }

         dispatch(postChatRequest(updatedMessages)).then(() => {
            dispatch(getChatRequest(ticket_id));
         });
         setNewMessage('');
      }
   };
   const handleUpload = (file) => {
      // 取出文件名中的后缀
      const fileExtension = file.file_id.split('.').pop().toLowerCase();
      const newMessages = [
         ...messages,
         {
            message_id: '',
            content: '',
            message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
            sender: "用户1",
            message_type: fileExtension === 'png' || fileExtension === 'jpg' ? MessageType.IMAGE : fileExtension === 'mp4' ? MessageType.VIDEO : '',
            file_url: file.file_url,
            file_id: file.file_id,
            chat_profile: ChatPriority.CUSTOMER,
            avatar_url: "https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png",
         }
      ];
      setMessages(newMessages);

      const updatedMessages: IChatRecord = {
         ticket_id: ticket_id,
         message_id: '',
         content: '',
         message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
         sender: "用户1",
         message_type: fileExtension === 'png' || fileExtension === 'jpg' ? MessageType.IMAGE : fileExtension === 'mp4' ? MessageType.VIDEO : '',
         file_url: file.file_url,
         file_id: file.file_id,
         chat_profile: ChatPriority.CUSTOMER,
         avatar_url: "https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png",
      }
      dispatch(postChatRequest(updatedMessages)).then(() => {
         dispatch(getChatRequest(ticket_id));
      });
      setNewMessage(''); // 清空输入框
   };
   // 修改renderItem函数，为每条消息添加头像和名字
   const renderMessageItem = (item: any) => {
      if (item.message_type === MessageType.IMAGE) {
         return <div>
            <div className={`${Style['message-item']} ${item.chat_profile === ChatPriority.CUSTOMER ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.chat_profile !== ChatPriority.CUSTOMER && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.chat_profile === ChatPriority.CUSTOMER ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.chat_profile === ChatPriority.CUSTOMER ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']} style={{ flexDirection: item.chat_profile === ChatPriority.CUSTOMER ? 'row-reverse' : 'row' }}>
                     <Image alt={item.id} src={item.file_url} style={{ width: 100, height: 100, objectFit: 'cover' }} />
                  </div>
               </div>
               {item.chat_profile === ChatPriority.CUSTOMER && (  // 当消息是当前用户发送时
                  <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
            </div>
         </div>
      } else if (item.message_type === MessageType.VIDEO) {
         return <div>
            <div className={`${Style['message-item']} ${item.chat_profile === ChatPriority.CUSTOMER ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.chat_profile !== ChatPriority.CUSTOMER && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.chat_profile === ChatPriority.CUSTOMER ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.chat_profile === ChatPriority.CUSTOMER ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']} style={{ flexDirection: item.chat_profile === ChatPriority.CUSTOMER ? 'row-reverse' : 'row' }}>
                     <video controls src={item.file_url} style={{ width: 100 }} />
                  </div>
               </div>

               {item.chat_profile === ChatPriority.CUSTOMER && (  // 当消息是当前用户发送时
                  <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
            </div>
         </div>
      }
      return (
         <div>
            <div className={`${Style['message-item']} ${item.chat_profile === ChatPriority.CUSTOMER ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.chat_profile !== ChatPriority.CUSTOMER && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.chat_profile === ChatPriority.CUSTOMER ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.chat_profile === ChatPriority.CUSTOMER ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']}>
                     <p>{item.content}</p>
                  </div>
               </div>
               {item.chat_profile === ChatPriority.CUSTOMER && (  // 当消息是当前用户发送时
                  <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
            </div>
         </div>
      );
   }

   const handleChange: UploadProps['onChange'] = ({ file }) => {
      if (file.status === 'done') {
         handleUpload(file?.response);
      }
   };

   const props = {
      action: 'http://47.116.201.99:8001/test/upload_file',
      onChange: handleChange,
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
         </div>
      </div>
   );
};

export default PChart;
