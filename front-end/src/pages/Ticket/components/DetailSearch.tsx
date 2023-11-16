import React, { useRef, memo } from 'react';
import {
  Row, Col,
  Breadcrumb, Layout, Menu, theme, Table, Form, Input, Button, Select, DatePicker
} from "antd";
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS } from '../consts';
import { FormInstanceFunctions, SubmitContext } from 'tdesign-react/es/form/type';
import Style from './DetailSearch.module.less';

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
    // Filter `option.label` match the user type `input`
const filterOption = (input: string, option?: { label: string; value: string }) =>
(option?.label ?? '').toLowerCase().includes(input.toLowerCase());
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
                <Form.Item label='当前处理人' name='name' >
                <Select defaultValue={'001'} style={{ width: 120 }} placeholder="无处理人" allowClear showSearch filterOption={filterOption}
                  options={[
                    {
                      value: '001',
                      label: '客服1',
                    },
                    {
                      value: '002',
                      label: '客服2',
                    },
                    {
                      value: '003',
                      label: '客服3',
                    },
                  ]}
                >
                </Select>
                </Form.Item>
                
              </Col>
              <Col >
              <Form.Item  name='name' >
                <Select defaultValue={'001'} style={{ width: 120 }} placeholder="待处理" allowClear showSearch filterOption={filterOption}
                  options={[
                    {
                      value: '001',
                      label: '客服1',
                    },
                    {
                      value: '002',
                      label: '客服2',
                    },
                    {
                      value: '003',
                      label: '客服3',
                    },
                  ]}
                >
                </Select>
                </Form.Item>
              </Col>
              {/* <Col >
                <Form.Item label="日期">
                  <RangePicker />
                </Form.Item>
              </Col> */}
            </Row>
          </Col>
        </Row>
      </Form>
    </div>
  );
};

export default memo(SearchForm);
