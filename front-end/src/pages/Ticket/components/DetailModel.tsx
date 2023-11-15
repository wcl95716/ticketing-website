import React, { useState, useEffect } from 'react';
import { Input, Button, List, message, Upload, Modal, Row, Col, Image } from 'antd';
import { PictureOutlined, UploadOutlined, PlusOutlined } from '@ant-design/icons';
import Style from '../components/DetailModel.module.less';
import type { RcFile, UploadProps } from 'antd/es/upload';
import {
   getTicketListRequest,
   getChatRequest,
   postChatRequest,
   selectTicketRecordList,
   selecChatRecord,
} from 'models/ticketing-website/index.model';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { useLocation } from 'react-router-dom';
import type { UploadFile } from 'antd/es/upload/interface';
import SearchForm from './SearchForm';
import { IChatRecord, MessageType } from 'models/ticketing-website/index.type';


const getBase64 = (file: RcFile): Promise<string> =>
   new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.readAsDataURL(file);
      reader.onload = () => resolve(reader.result as string);
      reader.onerror = (error) => reject(error);
   });


const DetailModel = () => {
   const location = useLocation();
   const { ticket_id } = location.state || {};
   console.log("传输进来key", ticket_id)

   const dispatch = useAppDispatch();
   const chatRecord = useAppSelector(selecChatRecord);

   const fetchMessages = async () => {
      if (ticket_id) {
         try {
            const response = await fetch(`http://47.116.201.99:8001/test/get_all_tickets/${ticket_id}`);
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
         const response = await fetch('http://47.116.201.99:8001/test/add_ticket', {
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
   //  const handleSendMessage = () => {
   //    if (newMessage.trim() !== '') {
   //      addTicket(newMessage.trim()); // 调用addTicket函数发送新消息
   //      setNewMessage(''); // 清空输入框
   //    }
   //  };

   //  const handleUpload = (file: RcFile) => {
   //    getBase64(file).then(base64 => {
   //      const fileMessage = {
   //        id: messages.length + 1,
   //        img: base64, // 假设我们发送base64编码的图片文件
   //        // ...其他属性，如时间戳、发送者等
   //      };
   //      addTicket(fileMessage); // 发送文件消息
   //    });
   //  };


   useEffect(() => {
      console.log("是否有key", ticket_id)
      if (ticket_id) {
         dispatch(getChatRequest(ticket_id))
      }
   }, [ticket_id]);

   useEffect(() => {
      setMessages(chatRecord);
   }, [chatRecord]);


   const [messages, setMessages] = useState([]);
   const [newMessage, setNewMessage] = useState('');
   const handleSendMessage = () => {
      if (newMessage.trim() !== '') {
         const newMessages = [
            ...messages,
         {
            ticket_id:ticket_id,
            message_id:'',
            content: newMessage.trim(),
            message_time: '1970-03-04 14:23:44',
            sender:'客服',
            message_type: 0,
         }
         ];
         setMessages(newMessages);

         const updatedMessages = {
            ticket_id:ticket_id,
            message_id:'',
            content: newMessage.trim(),
            message_time: '1970-03-04 14:23:44',
            sender:'客服',
            message_type: 0,
         }
         
         dispatch(postChatRequest(updatedMessages)).then(()=>{
            dispatch(getChatRequest(ticket_id));
         });
         setNewMessage(''); 
      }
   };
   const handleUpload = (file) => {
      console.log("查看RCFile",file)
      // file.name = 'http://47.116.201.99:8001/test/uplods' + file.name
      console.log("查看图片链接",file.name)
      const newMessages = [
         ...messages,
         {
            message_id:'',
            content: '',
            message_time: '1970-03-04 14:23:44',
            sender:'客服',
            message_type: MessageType.TEXT,
            file_url: file.file_url,
            file_id:file.file_id
         }
      ];
      setMessages(newMessages);
      
      const updatedMessages:IChatRecord = {
            ticket_id:ticket_id,
            message_id:'',
            content: '',
            message_time: '1970-03-04 14:23:44',
            sender:'客服',
            message_type: MessageType.IMAGE,
            file_url: file.file_url,
            file_id:file.file_id
      }
      dispatch(postChatRequest(updatedMessages)).then(()=>{
         dispatch(getChatRequest(ticket_id));
      });
      setNewMessage(''); // 清空输入框
   };
   
   const handleChange: UploadProps['onChange'] = ({ file }) => {
      //接口备用
      if (file.status === 'done') {
         handleUpload(file?.response);
         console.log("上传成功了",file)
      }
   };

   const props = {
      action: 'http://47.116.201.99:8001/test/upload_file',
      onChange: handleChange,
      // multiple: true,
   };
   // 修改renderItem函数，为每条消息添加头像和名字
   const renderMessageItem = (item: any) => {
      if (item.message_type === MessageType.IMAGE) {
         return <div>
            <div className={`${Style['message-item']} ${item.sender === '当前用户' ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.sender !== '当前用户' && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.sender === '当前用户' ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                     <Image alt={item.id} src={item.file_url} style={{ width: 100, height: 100, objectFit: 'cover' }} />
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
      } else if (item.message_type === MessageType.VIDEO) {
         return <div>
            <div className={`${Style['message-item']} ${item.sender === '当前用户' ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.sender !== '当前用户' && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.sender === '当前用户' ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                     <video controls src={item.file_url} style={{ width: 100 }} />
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
            <div style={{ backgroundColor: '' }} className={`${Style['message-item']} ${item.sender === '当前用户' ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.sender !== '当前用户' && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.sender === '当前用户' ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.sender === '当前用户' ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']}>
                     <p>{item.content}</p>
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


   return (
      <div>
         <Row justify='start' style={{ marginBottom: '20px', width:'100%'}}>
            <div style={{ width: '100%', backgroundColor: '#fff'}}>
               <SearchForm
               onSubmit={async (value) => {
                  console.log(value);
               }}
               onCancel={() => { }}
            />
            </div>
            
         </Row>
         <div style={{ width: '100%', height: '100%', backgroundColor: '#fff' ,paddingBottom:'20px'}}>
            <div style={{ paddingLeft: '4%', paddingTop: '10px', marginTop: '10px', marginBottom: '10px' }}>沟通记录</div>
            <List
               dataSource={messages}
               renderItem={renderMessageItem}  // 使用修改后的renderItem函数
            />
         </div>
         <div style={{ width: '100%', backgroundColor: '#fff'}}>
            <div className={Style['chat-input']} style={{ marginBottom: '0px', display: 'flex', flexDirection: 'column' }}>
               <Row justify="space-between" align="middle" >
                  <Col  style={{ width: '40%', marginLeft: '4%', marginBottom: 'auto', marginTop: '30px' }}>
                     <Input
                        style={{ width: '100%' }}
                        placeholder="请输入聊天内容"
                        suffix={<Button type='primary' onClick={handleSendMessage}>发送</Button>}
                        value={newMessage}
                        onChange={(e: any) => setNewMessage(e.target.value)}
                     />
                  </Col>
                  <Col  style={{ marginLeft: '0px', marginBottom: 'auto', marginRight: 'auto' , marginTop: '30px'}}>
                     <Upload {...props} showUploadList={false} >
                        <Button icon={<UploadOutlined />} style={{ marginLeft: '50px' }}>上传文件</Button>
                        <p className={Style['model-add-drawer-p']}>支持扩展名： *.png,*.jpg,*.mp4</p>
                     </Upload>
                  </Col>
               </Row>
            </div>
         </div>

      </div>
   );
};

export default DetailModel;
