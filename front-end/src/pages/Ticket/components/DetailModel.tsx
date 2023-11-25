import React, { useState, useEffect } from 'react';
import { Input, Button, List, message, Upload, Modal, Row, Col, Image } from 'antd';
import { PictureOutlined, UploadOutlined, PlusOutlined } from '@ant-design/icons';
import Style from '../components/DetailModel.module.less';
import type { RcFile, UploadProps } from 'antd/es/upload';
import {
   getTicketListRequest,
   getChatRequest,
   getUserDetail,
   getTicketDetail,
   postChatRequest,
   selectTicketRecordList,
   selecChatRecord,
   selecUserDetail,
   selecTicketDetail,
} from 'models/ticketing-website/index.model';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { useLocation } from 'react-router-dom';
import type { UploadFile } from 'antd/es/upload/interface';
import dayjs, { Dayjs } from 'dayjs';
import DetailSearch from './DetailSearch';
import { IChatRecord, MessageType, ChatPriority, ITicketRecord, TicketStatus, Priority } from 'models/ticketing-website/index.type';




const DetailModel = () => {
   const location = useLocation();
   const now = new Date();
   const [record,setRecord] = useState<ITicketRecord|undefined>(undefined)
   const searchParams = new URLSearchParams(location.search);
   const ticket_id = searchParams.get('ticket_id');

   const dispatch = useAppDispatch();
   const chatRecord = useAppSelector(selecChatRecord);
   const ifUserDetail = useAppSelector(selecUserDetail);
   // const record = useAppSelector(selecTicketDetail);
   const userInfo = useAppSelector(selecUserDetail);
   const isObjectEmpty = (obj) => {
      return Object.keys(obj).length === 0;
  };
   useEffect(()=>{
      const getRecord = async () => {
         try {
           const response = await fetch(`http://47.116.201.99:8001/test/get_ticket/${ticket_id}`);
           const record = await response.json();
           setRecord(record); // 更新详情
         } catch (error) {
           console.error("Error fetching messages:", error);
           message.error('获取信息失败');
         }
       }

       if (ticket_id) {
         getRecord();
       }
   },[])
   console.log("查看ifUserDetail",ifUserDetail)

   // const fetchMessages = async () => {
   //    if (ticket_id) {
   //       try {
   //          const response = await fetch(`http://47.116.201.99:8001/test/get_all_tickets/${ticket_id}`);
   //          const data = await response.json();
   //          setMessages(data); // 更新消息列表
   //       } catch (error) {
   //          console.error("Error fetching messages:", error);
   //          message.error('获取消息列表失败');
   //       }
   //    }
   // };

   // const addTicket = async (newMessageContent: any) => {
   //    try {
   //       const response = await fetch('http://47.116.201.99:8001/test/add_ticket', {
   //          method: 'POST',
   //          headers: {
   //             'Content-Type': 'application/json',
   //          },
   //          body: JSON.stringify({ message: newMessageContent }),
   //       });

   //       if (!response.ok) throw new Error('Network response was not ok.');
   //       // 假设POST请求成功后立即调用GET请求更新列表
   //       fetchMessages();
   //    } catch (error) {
   //       console.error("Error posting new ticket:", error);
   //       message.error('发送消息失败');
   //    }
   // };


   useEffect(() => {
      if (ticket_id) {
         dispatch(getChatRequest(ticket_id));
         // dispatch(getTicketDetail(ticket_id)).then(()=>{
         //    dispatch(getUserDetail(record?.assigned_to));
         // });

         const interval = setInterval(() => {
            dispatch(getChatRequest(ticket_id));
         }, 2000);

         return () => {
            clearInterval(interval); // 在组件卸载时清除定时器
         };
      }
   }, [ticket_id]);

   // useEffect(() => {
   //    dispatch(getUserDetail(record?.assigned_to));
   // }, [record])


   useEffect(() => {
      setMessages(chatRecord);
   }, [chatRecord]);

   const [messages, setMessages] = useState([]);
   const [newMessage, setNewMessage] = useState('');
   const handleSendMessage = () => {
      if (isObjectEmpty(ifUserDetail)) {
         message.error('请选择登陆人');
     } else{
        if (newMessage.trim() !== '') {
         const newMessages = [
            ...messages,
            {
               ticket_id: ticket_id,
               message_id: '',
               content: newMessage.trim(),
               message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
               sender: userInfo.name,
               message_type: MessageType.TEXT,
               chat_profile: ChatPriority.SERVICE,
               avatar_url: userInfo.avatar_url,
            }
         ];
         setMessages(newMessages);

         const updatedMessages = {
            ticket_id: ticket_id,
            message_id: '',
            content: newMessage.trim(),
            message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
            sender: userInfo.name,
            message_type: MessageType.TEXT,
            chat_profile: ChatPriority.SERVICE,
            avatar_url: userInfo.avatar_url,
         }

         dispatch(postChatRequest(updatedMessages)).then(() => {
            dispatch(getChatRequest(ticket_id));
         });
         setNewMessage('');
      }
     }
      
   };
   const handleUpload = (file) => {
      if (isObjectEmpty(ifUserDetail)) {
         message.error('请选择登陆人');
     } else{
      // 取出文件名中的后缀
      const fileExtension = file.file_id.split('.').pop().toLowerCase();
      const newMessages = [
         ...messages,
         {
            message_id: '',
            content: '',
            message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
            sender: userInfo.name,
            message_type: fileExtension === 'png' || fileExtension === 'jpg' ? MessageType.IMAGE : fileExtension === 'mp4' ? MessageType.VIDEO : '',
            file_url: file.file_url,
            file_id: file.file_id,
            chat_profile: ChatPriority.SERVICE,
            avatar_url: userInfo.avatar_url,
         }
      ];
      setMessages(newMessages);

      const updatedMessages: IChatRecord = {
         ticket_id: ticket_id,
         message_id: '',
         content: '',
         message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
         sender: userInfo.name,
         message_type: fileExtension === 'png' || fileExtension === 'jpg' ? MessageType.IMAGE : fileExtension === 'mp4' ? MessageType.VIDEO : '',
         file_url: file.file_url,
         file_id: file.file_id,
         chat_profile: ChatPriority.SERVICE,
         avatar_url: userInfo.avatar_url,
      }
      dispatch(postChatRequest(updatedMessages)).then(() => {
         dispatch(getChatRequest(ticket_id));
      });
      setNewMessage(''); // 清空输入框
   }
   };

   const handleKeyPress = (e) => {
      if (e.key === 'Enter') {
         handleSendMessage();
      }
   };

   const handleChange: UploadProps['onChange'] = ({ file }) => {
      if (file.status === 'done') {
         handleUpload(file?.response);
      }
   };
   const props = {
      
      action: 'http://47.116.201.99:8001/test/upload_file',
      onChange: handleChange,
   };
   // 修改renderItem函数，为每条消息添加头像和名字
   const renderMessageItem = (item: any) => {
      if (item.message_type === MessageType.IMAGE) {
         return <div>
            <div className={`${Style['message-item']} ${item.chat_profile === ChatPriority.SERVICE ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.chat_profile !== ChatPriority.SERVICE && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.chat_profile === ChatPriority.SERVICE ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']} style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}>
                     <Image alt={item.id} src={item.file_url} style={{ width: 100, height: 100, objectFit: 'cover' }} />
                  </div>
               </div>
               {item.chat_profile === ChatPriority.SERVICE && (  // 当消息是当前用户发送时
                  <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
            </div>
         </div>
      } else if (item.message_type === MessageType.VIDEO) {
         return <div>
            <div className={`${Style['message-item']} ${item.chat_profile === ChatPriority.SERVICE ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.chat_profile !== ChatPriority.SERVICE && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt="avatar" />
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.chat_profile === ChatPriority.SERVICE ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']} style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}>
                     {/* <video muted controls src={item.file_url} width="100px" height="100px" /> */}
                     <div className={Style['video-container']}>
                                <video
                                    controls
                                    src={item.file_url}
                                    poster="封面图片URL" // 设置视频封面
                                    preload="metadata"
                                >
                                    <source src={item.file_url} type="video/mp4" />
                                    您的浏览器不支持视频标签。
                                </video>
                                {/* 如果使用自定义播放按钮 */}
                                {/* <div className="custom-play-button"></div> */}
                            </div>
                  </div>
               </div>

               {item.chat_profile === ChatPriority.SERVICE && (  // 当消息是当前用户发送时
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
            <div style={{ backgroundColor: '' }} className={`${Style['message-item']} ${item.chat_profile === ChatPriority.SERVICE ? Style['current-user'] : ''} ${Style['bordered-list-item']}`}>
               {item.chat_profile !== ChatPriority.SERVICE && (  // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt="avatar"></img>
                     <p>{item.sender}</p>
                  </div>
               )}
               <div className={Style['message-content']} style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}>
                  <p className={Style['message-time']} style={{ textAlign: item.chat_profile === ChatPriority.SERVICE ? 'right' : 'left' }}>{item.message_time}</p>
                  <div className={Style['text']}>
                     <p>{item.content}</p>
                  </div>
               </div>
               {item.chat_profile === ChatPriority.SERVICE && (  // 当消息是当前用户发送时
                  <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                     <img src={item.avatar_url} alt="avatar"></img>
                     {/* <img src={item.avatar} alt="avatar" /> */}
                     <p>{item.sender}</p>
                  </div>
               )}
            </div>
         </div>
      );
   }


   return (
      <div>
         <Row justify='start' style={{ marginBottom: '20px', width: '100%' }}>
            {record&&
                        <div style={{ width: '100%', backgroundColor: '#fff' }}>
               
               <DetailSearch
                  onSubmit={async (value) => {
                     console.log(value);
                  }}
                  onCancel={() => { }}
                  record = {record}
               />
            </div>
            }

         </Row>
         <div style={{ width: '100%', height: '100%', backgroundColor: '#fff', paddingBottom: '20px' }}>
            <div style={{ paddingLeft: '4%', paddingTop: '10px', marginTop: '10px', marginBottom: '10px' }}>沟通记录</div>
            <List
               dataSource={messages}
               renderItem={renderMessageItem}  // 使用修改后的renderItem函数
            />
         </div>
         <div style={{ width: '100%', backgroundColor: '#fff' }}>
            <div className={Style['chat-input']} style={{ marginBottom: '0px', display: 'flex', flexDirection: 'column' }}>
               <Row justify="space-between" align="middle" >
                  <Col style={{ width: '50%', marginLeft: '4%', marginBottom: 'auto', marginTop: '30px' }}>
                     <Input
                        style={{ width: '100%' }}
                        placeholder="请输入聊天内容"
                        suffix={<Button type='primary' onClick={handleSendMessage}>发送</Button>}
                        value={newMessage}
                        onChange={(e: any) => setNewMessage(e.target.value)}
                        onKeyPress={handleKeyPress}
                     />
                  </Col>
                  <Col style={{ marginLeft: '0px', marginBottom: 'auto', marginRight: 'auto', marginTop: '30px' }}>
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