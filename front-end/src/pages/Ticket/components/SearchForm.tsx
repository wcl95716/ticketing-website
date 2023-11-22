import React, { useRef, memo, useEffect } from 'react';
import { Row, Col, Form, Input, Button, Select, DatePicker } from 'antd';
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS } from '../consts';
import Style from './SearchForm.module.less';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { getTicketListRequest, selecTicketFilter, updateTicketFilter } from 'models/ticketing-website/index.model';
import { TicketStatus } from 'models/ticketing-website/index.type';
import { number, use } from 'echarts';

const { RangePicker } = DatePicker;

const SearchForm: React.FC = () => {
  const dispatch = useAppDispatch();
  const ticketFilter = useAppSelector(selecTicketFilter);
  const [form] = Form.useForm();
  const onFinish = (values: any) => {
    console.log('Success:', values);
    const { time } = values;

    if (time && time.length === 2) {
      const start_date = time[0].format('YYYY-MM-DD HH:mm:ss');
      const end_date = time[1].format('YYYY-MM-DD HH:mm:ss');
      dispatch(
        updateTicketFilter({
          search_criteria: values?.search_criteria,
          status: values?.status,
          start_date,
          end_date,
        }),
      );
      // 在这里处理格式化后的时间值
    } else {
      dispatch(
        updateTicketFilter({
          search_criteria: values?.search_criteria,
          status: values?.status,
        }),
      );
    }
  };

  useEffect(() => {
    dispatch(getTicketListRequest(ticketFilter));
  }, [ticketFilter]);
  const onReset = () => {
    form.resetFields();
    dispatch(getTicketListRequest({}))
    // dispatch(
    //   updateTicketFilter({
    //     // 假设初始状态是空的
    //     search_criteria: '',
    //     status: null,
    //     start_date: null,
    //     end_date: null,
    //   }),
    // );
  };

  return (
    <div className={Style.ticketsearch}>
      <Form form={form} name='control-hooks' onFinish={onFinish}>
        <Row>
          <Col flex='1'>
            <Row gutter={[16, 16]}>
              <Col>
                <Form.Item label='关键字' name='search_criteria'>
                  <Input value="search_criteria" placeholder='请输入关键字' />
                </Form.Item>
              </Col>
              <Col>
                <Form.Item label='状态' name='status'>
                  <Select value="status" options={CONTRACT_STATUS_OPTIONS} placeholder='请选择状态' allowClear />
                </Form.Item>
              </Col>
              <Col>
                <Form.Item label='日期' name='time'>
                  <RangePicker value="time" placeholder={['开始时间', '结束时间']} format='YYYY-MM-DD' />
                </Form.Item>
              </Col>
            </Row>
          </Col>
          <Col>
            <Form.Item>
              <Button type='primary' htmlType='submit' style={{ margin: '0px 20px' }}>
                查询
              </Button>
              <Button htmlType='button' onClick={onReset}>
                重置
              </Button>
            </Form.Item>

          </Col>
        </Row>
      </Form>
    </div>
  );
};

export default memo(SearchForm);
