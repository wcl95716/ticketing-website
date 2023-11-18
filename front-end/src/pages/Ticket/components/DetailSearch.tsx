import React, { useRef, useState, memo, useEffect } from 'react';
import {
  Row, Col,
  Breadcrumb, Layout, Menu, theme, Table, Form, Input, Button, Select, DatePicker
} from "antd";
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS } from '../consts';
import { FormInstanceFunctions, SubmitContext } from 'tdesign-react/es/form/type';
import { getTicketListRequest,getAllUserRequest,selecAllUser} from 'models/ticketing-website/index.model';
import Style from './DetailSearch.module.less';
import { useAppDispatch, useAppSelector } from 'modules/store';

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
  const dispatch = useAppDispatch();
  const formRef = useRef<FormInstanceFunctions>();
  const allUserList = useAppSelector(selecAllUser);
  const userOption = [];
    allUserList.forEach((item)=>{
        userOption.push({
            label: item?.name,
            value: item?.user_id
        })
    })

  useEffect(() => {
     dispatch(getTicketListRequest({}))
     dispatch(getAllUserRequest())
  }, []);
    // Filter `option.label` match the user type `input`
const filterOption = (input: string, option?: { label: string; value: string }) =>
(option?.label ?? '').toLowerCase().includes(input.toLowerCase());

  return (
    <div className={Style.ticketsearch}>
      <Form  >
        <Row>
          <Col flex='1'>
            <Row gutter={[16, 16]}>
              <Col >
                <Form.Item label='当前处理人' name='name' >
                <Select defaultValue={'001'} style={{ width: 120 }} placeholder="无处理人" allowClear showSearch filterOption={filterOption}
                  options={userOption} 
                >
                </Select>
                </Form.Item>
                
              </Col>
              <Col >
              <Form.Item  name='name' >
                <Select defaultValue={'001'} style={{ width: 120 }} placeholder="待处理" allowClear showSearch filterOption={filterOption}
                  options={[
                    {
                      value: 0,
                      label: '待处理',
                    },
                    {
                        value: 1,
                        label: '处理中',
                    },
                    {
                        value: 2,
                        label: '处理完成',
                    },
                    {
                        value: 3,
                        label: '关闭工单',
                    },
                  ]}
                >
                </Select>
                </Form.Item>
              </Col>
            </Row>
          </Col>
        </Row>
      </Form>
    </div>
  );
};

export default memo(SearchForm);
