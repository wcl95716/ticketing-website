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
                <Form.Item label='关键字' name='name'>
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
                  <RangePicker />
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