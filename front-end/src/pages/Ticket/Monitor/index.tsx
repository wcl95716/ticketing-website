import React, { useState } from 'react';
import { InboxOutlined } from '@ant-design/icons';
import type { UploadProps } from 'antd';
import { message, Upload, Flex } from 'antd';
import { Button } from 'tdesign-react';
import { updateIf } from 'typescript';

const { Dragger } = Upload;

const Monitor = () => {
  const [fileList, setFileList] = useState({
    vehicle_data_url: '',
    organization_group_url: '',
    language_template_url: '',
  });

  const monitorlog: UploadProps = {
    name: 'file',
    multiple: true,
    action: 'http://47.116.201.99:8001/test/upload_file',
    onChange(info) {
      const { status } = info.file;
      if (status !== 'uploading') {
        if (info.fileList.length <= 0) {
          setFileList((prevFileList) => ({
            ...prevFileList,
            vehicle_data_url: '',
          }));
        }
      }
      if (status === 'done') {
        message.success(`${info.file.name} 监控日志文件上传成功.`);
        const { response } = info.fileList[0];
        setFileList((prevFileList) => ({
          ...prevFileList,
          vehicle_data_url: response?.file_url,
        }));
      } else if (status === 'error') {
        message.error(`${info.file.name} 文件上传失败.`);
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };

  const distrirule: UploadProps = {
    name: 'file',
    multiple: true,
    action: 'http://47.116.201.99:8001/test/upload_file',
    onChange(info) {
      const { status } = info.file;
      if (status !== 'uploading') {
        if (info.fileList.length <= 0) {
          setFileList((prevFileList) => ({
            ...prevFileList,
            vehicle_data_url: '',
          }));
        }
      }
      if (status === 'done') {
        message.success(`${info.file.name} 分发规则文件上传成功.`);
        const { response } = info.file;
        setFileList((prevFileList) => ({
          ...prevFileList,
          organization_group_url: response?.file_url,
        }));
      } else if (status === 'error') {
        message.error(`${info.file.name} 文件上传失败.`);
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };

  const protocolrule: UploadProps = {
    name: 'file',
    multiple: true,
    action: 'http://47.116.201.99:8001/test/upload_file',
    onChange(info) {
      const { status } = info.file;
      if (status !== 'uploading') {
        if (info.fileList.length <= 0) {
          setFileList((prevFileList) => ({
            ...prevFileList,
            vehicle_data_url: '',
          }));
        }
      }
      if (status === 'done') {
        message.success(`${info.file.name} 话术规则文件上传成功.`);
        const { response } = info.file;
        setFileList((prevFileList) => ({
          ...prevFileList,
          language_template_url: response?.file_url,
        }));
      } else if (status === 'error') {
        message.error(`${info.file.name} 文件上传失败.`);
      }
    },
    onDrop(e) {
      console.log('Dropped files', e.dataTransfer.files);
    },
  };
  //提交接口
  const getRecord = async (fileListParams) => {
    try {
      const response = await fetch(`http://47.116.201.99:8001/wechat_robot_online/process_log`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        // 如果你需要发送请求体数据，可以在这里添加
        body: JSON.stringify(fileListParams),
      });
    } catch (error) {
      console.error('Error fetching messages:', error);
      message.error('获取信息失败');
    }
  };

  const onSubmit = () => {
    // console.log('查看fileList', fileList);
    if (fileList.vehicle_data_url === '') {
      message.error(`请上传监控日志文件`);
      return;
    } else if (fileList.organization_group_url === '') {
      message.error(`请上传分发规则`);
      return;
    } else if (fileList.language_template_url === '') {
      message.error(`请上传话术规则`);
      return;
    } else {
      getRecord(fileList);
    }
  };

  return (
    <div>
      <Flex vertical gap='small' style={{ width: '100%' }}>
        <Dragger {...monitorlog} maxCount={1}>
          <p className='ant-upload-drag-icon'>
            <InboxOutlined />
          </p>
          <p className='ant-upload-text'>点击上传监控日志/拖拽到此处</p>
          <p className='ant-upload-hint'>请上传监控日志文件</p>
        </Dragger>

        <Dragger {...distrirule} maxCount={1}>
          <p className='ant-upload-drag-icon'>
            <InboxOutlined />
          </p>
          <p className='ant-upload-text'>点击上传分发规则/拖拽到此处</p>
          <p className='ant-upload-hint'>请上传监控日志文件</p>
        </Dragger>

        <Dragger {...protocolrule} maxCount={1}>
          <p className='ant-upload-drag-icon'>
            <InboxOutlined />
          </p>
          <p className='ant-upload-text'>点击上传话术规则/拖拽到此处</p>
          <p className='ant-upload-hint'>请上传监控日志文件</p>
        </Dragger>

        <Button onClick={onSubmit}>提交</Button>
      </Flex>
    </div>
  );
};

export default Monitor;