import React, { useState, useEffect, useRef } from 'react';
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
import ErrorPage from './components/errorPage';
import '../../assets/font_4370488_wl3alye5i7/iconfont.css'



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
    const endOfMessagesRef = useRef(null);

    const location = useLocation();
    const queryParams = new URLSearchParams(location.search);
    const ticket_id = queryParams.get('ticket_id');
    const customer_id = queryParams.get('customer_id');

    const now = new Date();

    const [pastedImage, setPastedImage] = useState<File | null>(null); // 添加状态变量来保存粘贴的图片
    const [file, setFile] = useState<File | null>(null);


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
                    ticket_id: ticket_id,
                    message_id: '',
                    content: newMessage.trim(),
                    message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
                    sender: customer_id,
                    message_type: MessageType.TEXT,
                    chat_profile: ChatPriority.CUSTOMER,
                    avatar_url: "http://14.103.200.99:8001/test/uploads/94645ce7df1b4fcb8123f93b040dbcb1_617e9a689d4bc7779c46e2ab93791df.png",
                }
            ];
            setMessages(newMessages);

            const updatedMessages = {
                ticket_id: ticket_id,
                message_id: '',
                content: newMessage.trim(),
                message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
                sender: customer_id,
                message_type: MessageType.TEXT,
                chat_profile: ChatPriority.CUSTOMER,
                avatar_url: "http://14.103.200.99:8001/test/uploads/94645ce7df1b4fcb8123f93b040dbcb1_617e9a689d4bc7779c46e2ab93791df.png",
            }

            dispatch(postChatRequest(updatedMessages)).then(() => {
                dispatch(getChatRequest(ticket_id));
            });
            setNewMessage('');
        }
        // scrollToBottom();
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
                sender: customer_id,
                message_type: fileExtension === 'png' || fileExtension === 'jpg' || fileExtension === 'jpeg'|| fileExtension === 'gif' ? MessageType.IMAGE : fileExtension === 'mp4' || fileExtension === 'webm' || fileExtension === 'ogg' || fileExtension === 'mov' ? MessageType.VIDEO : '',
                file_url: file.file_url,
                file_id: file.file_id,
                chat_profile: ChatPriority.CUSTOMER,
                avatar_url: "http://14.103.200.99:8001/test/uploads/94645ce7df1b4fcb8123f93b040dbcb1_617e9a689d4bc7779c46e2ab93791df.png",
            }
        ];
        setMessages(newMessages);

        const updatedMessages: IChatRecord = {
            ticket_id: ticket_id,
            message_id: '',
            content: '',
            message_time: dayjs(now).format('YYYY-MM-DD HH:mm:ss'),
            sender: customer_id,
            message_type: fileExtension === 'png' || fileExtension === 'jpg' || fileExtension === 'jpeg'|| fileExtension === 'gif' ? MessageType.IMAGE : fileExtension === 'mp4' || fileExtension === 'webm' || fileExtension === 'ogg' || fileExtension === 'mov' ? MessageType.VIDEO : '',
            file_url: file.file_url,
            file_id: file.file_id,
            chat_profile: ChatPriority.CUSTOMER,
            avatar_url: "http://14.103.200.99:8001/test/uploads/94645ce7df1b4fcb8123f93b040dbcb1_617e9a689d4bc7779c46e2ab93791df.png",
        }
        dispatch(postChatRequest(updatedMessages)).then(() => {
            dispatch(getChatRequest(ticket_id));
        });
        setNewMessage(''); // 清空输入框
        setFile(null);
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
                            {/* <video controls src={item.file_url} style={{ width: 100 }} /> */}
                            {/* <video
                                controls
                                src={item.file_url}
                                style={{ width: '100%', maxWidth: '200px' }} // 控制视频大小，确保自适应且不过大
                                poster="封面图片URL" // 设置视频封面
                                preload="metadata" // 预加载视频元数据
                            >
                                <source src={item.file_url} type="video/mp4" />
                                您的浏览器不支持视频标签。
                            </video> */}
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
                            {/* <i className="iconfont icon-a-ziyuan90"></i> */}
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
        accept: "image/*,video/*", // 允许上传图片和视频
        action: 'http://14.103.200.99:8001/test/upload_file',
        onChange: handleChange,
    };


    const listRef = useRef<HTMLDivElement | null>(null);

    useEffect(() => {
        // 在数据更新后，滚动到列表底部
        if (listRef.current && newMessage.length == 0) {
            listRef.current.scrollTop = listRef.current.scrollHeight;
        }
    }, [newMessage]); // 监听数据的变化
    if (chatRecord == undefined) {
        return <ErrorPage />;
    }
    const uploadFileInput = () => {
        if (file) {
           const formData = new FormData();
           formData.append('file', file);
           // 这里替换为你的上传API
           fetch('http://14.103.200.99:8001/test/upload_file', {
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
        <div style={{ backgroundColor: '#fff', height: '100vh', padding: '10px', display: 'flex', flexDirection: 'column' }}>

            <div style={{ overflowY: 'scroll', height: '85vh' }} ref={listRef}>
                <List
                    dataSource={messages}
                    renderItem={renderMessageItem}  // 使用修改后的renderItem函数
                    style={{ flex: 1, overflow: 'auto' }}
                />
            </div>
            {/* <div style={{ overflowY: 'scroll', height: '2vh' }}>
         </div> */}
            <div className={Style['chat-input']} style={{ marginTop: 'auto', paddingBottom: '15px', width: 'auto' }}>
                <div style={{ display: 'flex', width: 'auto', marginBottom: '30px' }}>
                    <Input
                        inputMode="text"
                        style={{ flex: 1, marginRight: '2vh', fontSize: '16px' }}
                        placeholder="请输入聊天内容"
                        onPaste={handlePaste}
                        suffix={
                           <div>
                              <Button type='primary'  onClick={() => {
                                 file ? uploadFileInput() : handleSendMessage();
                              }}>发送</Button>
                              {/* <Upload
                                 {...props} showUploadList={false} >
                                    <Button style={{ flex: '0 0 auto', marginTop: '5px', marginLeft:"1vh" }} shape="circle" icon={<PlusOutlined style={{ color: 'grey' }} />} />
                              </Upload> */}
                           </div>
                     }
                        value={newMessage}
                        onChange={(e: any) => {
                            setNewMessage(e.target.value);
                        }
                        }
                    />
                    <Upload {...props} showUploadList={false} >
                        <Button style={{ flex: '0 0 auto', marginTop: '5px' }} shape="circle" icon={<PlusOutlined style={{ color: 'grey' }} />} />
                    </Upload>
                </div>
            </div>
        </div>
    );
};

export default PChart;
