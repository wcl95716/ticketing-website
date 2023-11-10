import React, { useRef, memo } from 'react';
import {
  Row, Col,
  Breadcrumb, Layout, Menu, theme, Table, Form, Input, Button, Select, DatePicker
} from "antd";
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS } from '../consts';
import { FormInstanceFunctions, SubmitContext } from 'tdesign-react/es/form/type';
import Style from './SearchForm.module.less';

const { RangePicker } = DatePicker;


export type FormValueType = {
  name?: string;
  status?: string;
  number?: string;
  time?: string;
  type?: string;
};

export type SearchFormProps = {
  onCancel: () => void;
  onSubmit: (values: FormValueType) => Promise<void>;
};

const SearchForm: React.FC<SearchFormProps> = (props) => {
  const formRef = useRef<FormInstanceFunctions>();
  const onSubmit = (e: SubmitContext) => {
    if (e.validateResult === true) {
      // MessagePlugin.info('提交成功');
    }
    const queryValue = formRef?.current?.getFieldsValue?.(true);
    console.log('form 数据', queryValue);
  };

  const onReset = () => {
    props.onCancel();
    // MessagePlugin.info('重置成功');
  };

  return (
    <div className={Style.ticketsearch}>
      <Form  >
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
                <Form.Item label="日期">
                  <RangePicker />
                </Form.Item>
              </Col>
            </Row>
          </Col>
          <Col>
            <Button type='primary' style={{ margin: '0px 20px' }}>
              查询
            </Button>
            <Button>
              重置
            </Button>
          </Col>
        </Row>
      </Form>
    </div>
  );
};

export default memo(SearchForm);