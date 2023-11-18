import React, { useRef, memo } from 'react';
import {
  Row, Col, Form, Input, Button, Select, DatePicker
} from "antd";
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS } from '../consts';
import Style from './SearchForm.module.less';

const { RangePicker } = DatePicker;


const SearchForm: React.FC = () => {
  const [form] = Form.useForm();
  const onFinish = (values: any) => {
    console.log('Success:', values);
    const { time } = values;

    if (time && time.length === 2) {
      const formattedStartTime = time[0].format('YYYY-MM-DD HH:mm:ss');
      const formattedEndTime = time[1].format('YYYY-MM-DD HH:mm:ss');

      console.log('开始时间:', formattedStartTime);
      console.log('结束时间:', formattedEndTime);
      // 在这里处理格式化后的时间值
    }
  };
  const onReset = () => {
    form.resetFields();
  };

  return (
    <div className={Style.ticketsearch}>
      <Form
        name="control-hooks"
        onFinish={onFinish}
      >
        <Row>
          <Col flex='1'>
            <Row gutter={[16, 16]}>
              <Col >
                <Form.Item label='关键字' name='search_criteria'>
                  <Input placeholder='请输入关键字' />
                </Form.Item>
              </Col>
              <Col >
                <Form.Item label='状态' name='status'>
                  <Select options={CONTRACT_STATUS_OPTIONS} placeholder='请选择状态' />
                </Form.Item>
              </Col>
              <Col >
                <Form.Item label="日期" name='time'>
                  <RangePicker 
                  placeholder={['开始时间', '结束时间']}
                  format="YYYY-MM-DD"
                  />
                  
                </Form.Item>
              </Col>
            </Row>
          </Col>
          <Col>
            <Button type='primary' htmlType="submit" style={{ margin: '0px 20px' }}>
              查询
            </Button>
            <Button htmlType="button" onClick={onReset}>
              重置
            </Button>
          </Col>
        </Row>
      </Form>
    </div>
  );
};

export default memo(SearchForm);