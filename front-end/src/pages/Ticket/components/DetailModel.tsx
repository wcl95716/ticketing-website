import React, { useState, useEffect } from 'react';
import { Input, Button, List, message, Upload, Modal, Row, Col, Image } from 'antd';
import { PictureOutlined, ScissorOutlined, EyeOutlined, FolderOutlined } from '@ant-design/icons';
import Style from '../components/DetailModel.module.less';
import type { RcFile, UploadProps } from 'antd/es/upload';
import {
   getTicketListRequest,
   getChatRequest,
   getUserDetail,
   getTicketDetail,
   postChatRequest,
   postMegNotice,
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
import {
   IChatRecord,
   MessageType,
   ChatPriority,
   ITicketRecord,
   TicketStatus,
   Priority,
} from 'models/ticketing-website/index.type';
import FilePasteUpload from './copyUpload';

const { TextArea } = Input;

const DetailModel = () => {
   const location = useLocation();
   const now = new Date();
   const [record, setRecord] = useState<ITicketRecord | undefined>(undefined);
   const searchParams = new URLSearchParams(location.search);
   const ticket_id = searchParams.get('ticket_id');

   const [pastedImage, setPastedImage] = useState<File | null>(null); // 添加状态变量来保存粘贴的图片
   const [file, setFile] = useState<File | null>(null);

   const dispatch = useAppDispatch();
   const chatRecord = useAppSelector(selecChatRecord);
   const ifUserDetail = useAppSelector(selecUserDetail);
   const userInfo = useAppSelector(selecUserDetail);
   const isObjectEmpty = (obj) => {
      return Object.keys(obj).length === 0;
   };
   useEffect(() => {
      const getRecord = async () => {
         try {
            const response = await fetch(`http://47.116.201.99:8001/test/get_ticket/${ticket_id}`);
            const record = await response.json();
            setRecord(record); // 更新详情
         } catch (error) {
            // console.error('Error fetching messages:', error);
            message.error('获取信息失败');
         }
      };

      if (ticket_id) {
         getRecord();
      }
   }, []);

   useEffect(() => {
      if (ticket_id) {
         dispatch(getChatRequest(ticket_id));
         // dispatch(getTicketDetail(ticket_id)).then(()=>{
         //    dispatch(getUserDetail(record?.assigned_to));
         // });

         const interval = setInterval(() => {
            dispatch(getChatRequest(ticket_id));
         }, 3000);

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
      } else {
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
               },
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
            };

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
      } else {
         // 取出文件名中的后缀
         const fileExtension = file.file_id.split('.').pop().toLowerCase();
         const newMessages = [
            ...messages,
            {
               message_id: '',
               content: '',
               message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
               sender: userInfo.name,
               message_type:
                  fileExtension === 'png' || fileExtension === 'jpg' || fileExtension === 'jpeg' || fileExtension === 'gif'
                     ? MessageType.IMAGE
                     : fileExtension === 'mp4' ||
                        fileExtension === 'webm' ||
                        fileExtension === 'ogg' ||
                        fileExtension === 'mov'
                        ? MessageType.VIDEO
                        : '',
               file_url: file.file_url,
               file_id: file.file_id,/*  */
               chat_profile: ChatPriority.SERVICE,
               avatar_url: userInfo.avatar_url,
            },
         ];
         setMessages(newMessages);

         const updatedMessages: IChatRecord = {
            ticket_id: ticket_id,
            message_id: '',
            content: '',
            message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
            sender: userInfo.name,
            message_type:
               fileExtension === 'png' || fileExtension === 'jpg' || fileExtension === 'jpeg' || fileExtension === 'gif'
                  ? MessageType.IMAGE
                  : fileExtension === 'mp4' || fileExtension === 'webm' || fileExtension === 'ogg' || fileExtension === 'mov'
                     ? MessageType.VIDEO
                     : '',
            file_url: file.file_url,
            file_id: file.file_id,
            chat_profile: ChatPriority.SERVICE,
            avatar_url: userInfo.avatar_url,
         };
         dispatch(postChatRequest(updatedMessages)).then(() => {
            dispatch(getChatRequest(ticket_id));
         });
         setNewMessage(''); // 清空输入框
         setFile(null);
      }
   };
   // 微信消息提醒
   const messageNotice = (e) => {
      dispatch(postMegNotice({ticket_id:ticket_id}));
   }
   const handleKeyPress = (e) => {
      if (e.key === 'Enter') {
         e.preventDefault(); // 阻止默认的换行行为
         file ? uploadFileInput() : handleSendMessage();
         // handleSendMessage();
      }
   };

   const handleChange: UploadProps['onChange'] = ({ file }) => {
      if (file.status === 'done') {
         handleUpload(file?.response);
      }
   };
   const props = {
      accept: '.png,.jpg,.jpeg,.mp4', // 只允许上传 PNG, JPG/JPEG 和 MP4 文件
      action: 'http://47.116.201.99:8001/test/upload_file',
      onChange: handleChange,
   };
   // 修改renderItem函数，为每条消息添加头像和名字
   const renderMessageItem = (item: any) => {
      if (item.message_type === MessageType.IMAGE) {
         return (
            <div>
               <div
                  className={`${Style['message-item']} ${item.chat_profile === ChatPriority.SERVICE ? Style['current-user'] : ''
                     } ${Style['bordered-list-item']}`}
               >
                  {item.chat_profile !== ChatPriority.SERVICE && ( // 当消息不是当前用户发送时
                     <div className={Style['avatar']}>
                        <img src={item.avatar_url} alt='avatar' />
                        <p>{item.sender}</p>
                     </div>
                  )}
                  <div
                     className={Style['message-content']}
                     style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}
                  >
                     <p
                        className={Style['message-time']}
                        style={{ textAlign: item.chat_profile === ChatPriority.SERVICE ? 'right' : 'left' }}
                     >
                        {item.message_time}
                     </p>
                     <div
                        className={Style['text']}
                        style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}
                     >
                        <Image alt={item.id} src={item.file_url} style={{ width: 100, height: 100, objectFit: 'cover' }} />
                     </div>
                  </div>
                  {item.chat_profile === ChatPriority.SERVICE && ( // 当消息是当前用户发送时
                     <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                        <img src={item.avatar_url} alt='avatar' />
                        <p>{item.sender}</p>
                     </div>
                  )}
               </div>
            </div>
         );
      } else if (item.message_type === MessageType.VIDEO) {
         return (
            <div>
               <div
                  className={`${Style['message-item']} ${item.chat_profile === ChatPriority.SERVICE ? Style['current-user'] : ''
                     } ${Style['bordered-list-item']}`}
               >
                  {item.chat_profile !== ChatPriority.SERVICE && ( // 当消息不是当前用户发送时
                     <div className={Style['avatar']}>
                        <img src={item.avatar_url} alt='avatar' />
                        <p>{item.sender}</p>
                     </div>
                  )}
                  <div
                     className={Style['message-content']}
                     style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}
                  >
                     <p
                        className={Style['message-time']}
                        style={{ textAlign: item.chat_profile === ChatPriority.SERVICE ? 'right' : 'left' }}
                     >
                        {item.message_time}
                     </p>
                     <div
                        className={Style['text']}
                        style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}
                     >
                        {/* <video muted controls src={item.file_url} width="100px" height="100px" /> */}
                        <div className={Style['video-container']}>
                           <video
                              controls
                              src={item.file_url}
                              poster='封面图片URL' // 设置视频封面
                              preload='metadata'
                           >
                              <source src={item.file_url} type='video/mp4' />
                              您的浏览器不支持视频标签。
                           </video>
                           {/* 如果使用自定义播放按钮 */}
                           {/* <div className="custom-play-button"></div> */}
                        </div>
                     </div>
                  </div>

                  {item.chat_profile === ChatPriority.SERVICE && ( // 当消息是当前用户发送时
                     <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                        <img src={item.avatar_url} alt='avatar' />
                        <p>{item.sender}</p>
                     </div>
                  )}
               </div>
            </div>
         );
      }
      return (
         <div>
            <div
               style={{ backgroundColor: '' }}
               className={`${Style['message-item']} ${item.chat_profile === ChatPriority.SERVICE ? Style['current-user'] : ''
                  } ${Style['bordered-list-item']}`}
            >
               {item.chat_profile !== ChatPriority.SERVICE && ( // 当消息不是当前用户发送时
                  <div className={Style['avatar']}>
                     <img src={item.avatar_url} alt='avatar'></img>
                     <p>{item.sender}</p>
                  </div>
               )}
               <div
                  className={Style['message-content']}
                  style={{ flexDirection: item.chat_profile === ChatPriority.SERVICE ? 'row-reverse' : 'row' }}
               >
                  <p
                     className={Style['message-time']}
                     style={{ textAlign: item.chat_profile === ChatPriority.SERVICE ? 'right' : 'left' }}
                  >
                     {item.message_time}
                  </p>
                  <div className={Style['text']}>
                     <p>{item.content}</p>
                  </div>
               </div>
               {item.chat_profile === ChatPriority.SERVICE && ( // 当消息是当前用户发送时
                  <div className={Style['current-avatar']} style={{ marginLeft: '10px' }}>
                     <img src={item.avatar_url} alt='avatar'></img>
                     {/* <img src={item.avatar} alt="avatar" /> */}
                     <p>{item.sender}</p>
                  </div>
               )}
            </div>
         </div>
      );
   };

   
   const uploadFileInput = () => {
      if (file) {
         const formData = new FormData();
         formData.append('file', file);
         // 这里替换为你的上传API
         fetch('http://47.116.201.99:8001/test/upload_file', {
            method: 'POST',
            body: formData,
         })
            .then((response) => response.json())

            .then((data) => {
               console.log('data ', data);
               handleUpload(data);
            })
            .catch((error) => console.error('上传错误:', error));
      }
      
   };
   const handlePaste = (event: React.ClipboardEvent) => {
      const items = event.clipboardData.items;
      for (const item of items) {
         if (item.kind === 'file') {
            const pastedFile = item.getAsFile();
            if (pastedFile) {
               setPastedImage(pastedFile); // 保存粘贴的图片到状态变量
               setNewMessage(pastedFile.name); // 将文件名显示在TextArea中
               setFile(pastedFile);
               // 这里可以添加上传文件的逻辑
               console.log('文件已粘贴:', pastedFile);
            }
         }
      }
   };

   return (
      <div>
         <Row justify='start' style={{ marginBottom: '20px', width: '100%' }}>
            {record && (
               <div style={{ width: '100%', backgroundColor: '#fff' }}>
                  <DetailSearch
                     onSubmit={async (value) => {
                        console.log(value);
                     }}
                     onCancel={() => { }}
                     record={record}
                  />
               </div>
            )}
         </Row>
         <div style={{ width: '100%', height: '100%', backgroundColor: '#fff', paddingBottom: '20px' }}>
            <div style={{ paddingLeft: '4%', paddingTop: '10px', marginTop: '10px', marginBottom: '10px' }}>沟通记录</div>
            <List
               dataSource={messages}
               renderItem={renderMessageItem} // 使用修改后的renderItem函数
            />
         </div>
         <div style={{ width: '100%', backgroundColor: '#fff' }}>
            <div className={Style['chat-input']} style={{ marginBottom: '0px', display: 'flex', flexDirection: 'column' }}>
               <Row justify='space-between' align='middle'>
                  <Col style={{ width: '90%', marginLeft: '4%', marginBottom: '20px', marginTop: '30px' }}>
                     <div style={{ display: 'flex', flexDirection: 'column', border: '1px solid #d9d9d9' }}>
                        <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', marginTop: '10px' }}>
                           <div style={{ display: 'flex' }}>
                              <div style={{ marginRight: '5px' }}>
                                 <Upload {...props} showUploadList={false}>
                                    <div>
                                       <PictureOutlined style={{ fontSize: '25px', marginLeft: '15px' }} />
                                    </div>
                                 </Upload>
                              </div>
                              {/* 其他组件 */}
                           </div>
                           <div>
                              <Button
                                 type="primary"
                                 onClick={messageNotice}
                                 style={{ marginRight: '10px', marginBottom: '5px', borderRadius: '0px' }} // 按钮距离右边 10px
                              >微信客户提醒</Button>
                           </div>
                        </div>
                        <TextArea
                           className={Style['custom-textarea']}
                           rows={4}
                           onPaste={handlePaste}
                           style={{ width: '100%', border: 'none', outline: 'none', marginTop: '10px' }}
                           value={newMessage}
                           onChange={(e: any) => setNewMessage(e.target.value)}
                           onKeyPress={handleKeyPress}
                           autoSize={{ minRows: 3 }}
                        />
                        {/* <div
                  className={Style['custom-textarea']}
                  style={{ width: '100%',height:'150px', border: 'none', outline: 'none' }}
                  contentEditable={true}
                  
                  onPaste={handlePaste}
                  // ... 其他属性
                >
                  {newMessage}
                </div> */}

                        <div style={{ display: 'flex', justifyContent: 'flex-end' }}>
                           <Button
                              type='primary'
                              onClick={() => {
                                 file ? uploadFileInput() : handleSendMessage();
                              }}
                              disabled={!newMessage} // 只有当输入框有内容时启用按钮
                              style={{ marginRight: '10px', marginBottom: '5px', borderRadius: '0px' }} // 将按钮离右边10px
                           >
                              发送
                           </Button>
                        </div>
                     </div>
                  </Col>
               </Row>
            </div>
         </div>
      </div>
   );
};

export default DetailModel;