import React, { useRef, useState, memo, useEffect } from 'react';
import {
    Row, Col,
    Breadcrumb, Layout, Menu, theme, Table, Form, Input, Button, Select, DatePicker
} from "antd";
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS } from '../consts';
import { FormInstanceFunctions, SubmitContext } from 'tdesign-react/es/form/type';
import { getTicketListRequest, getAllUserRequest, getTicketDetail, getUserDetail, updateTicket, selecAllUser, selecUserDetail, selecTicketDetail } from 'models/ticketing-website/index.model';
import Style from './DetailSearch.module.less';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { useNavigate } from 'react-router-dom';


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
    const { record } = props || {}
    console.log("reeeec",record)
    const dispatch = useAppDispatch();
    const navigate = useNavigate();
    const searchParams = new URLSearchParams(location.search);
    const ticket_id = searchParams.get('ticket_id');
    const formRef = useRef<FormInstanceFunctions>();
    
    const allUserList = useAppSelector(selecAllUser);
    const userInfo = useAppSelector(selecUserDetail);
    // const record = useAppSelector(selecTicketDetail);
    // console.log("查看search的record",record)
    
    const userOption = [];
    allUserList.forEach((item) => {
        userOption.push({
            label: item?.name,
            value: item?.user_id
        })
    })

    useEffect(() => {
        dispatch(getTicketListRequest({}))
        dispatch(getAllUserRequest())
    }, [ticket_id]);

    useEffect(() => {
        dispatch(getUserDetail(record?.assigned_to));
     }, [record])

    const onUserChange = (value) => {
        const updateRecord = { ...record, assigned_to: value === undefined ? null : value };
        dispatch(updateTicket(updateRecord)).then(() => {
            dispatch(getUserDetail(value));
            dispatch(getTicketListRequest({}));
        });
    }
    const onStatusChange = (value) => {
        const updateRecord = { ...record, status: value === undefined ? null : value };
        dispatch(updateTicket(updateRecord)).then(() => {
            dispatch(getTicketListRequest({}));
        });
    }
    // Filter `option.label` match the user type `input`
    const filterOption = (input: string, option?: { label: string; value: string }) =>
        (option?.label ?? '').toLowerCase().includes(input.toLowerCase());

    const redirectToTicketList = () => {
        navigate({
            pathname: '/ticket/index'
        });
    }

    return (
        <div className={Style.ticketsearch}>
            <Form  >
                <Row>
                    <Col flex='1'>
                        <Row gutter={[16, 16]} style={{ alignItems: 'center' }}>
                            <Col>
                                <div style={{ margin: '10px', fontWeight: 'bold' }}>{`${userInfo?.name}的工单详情`}</div>
                            </Col>
                            <Col>
                                <Button size='small' type='primary' onClick={redirectToTicketList}>返回列表</Button>
                            </Col>
                        </Row>
                        <Row gutter={[16, 16]}>
                            <Col >
                                <Form.Item label='' name='name' >
                                    <Select defaultValue={record?.assigned_to} style={{ width: 120 }} placeholder="无处理人" allowClear showSearch filterOption={filterOption}
                                        options={userOption} onChange={onUserChange}
                                    >
                                    </Select>
                                </Form.Item>

                            </Col>
                            <Col >
                                <Form.Item name='status' >
                                    <Select defaultValue={record?.status} style={{ width: 120 }} placeholder="请选择处理状态" allowClear showSearch filterOption={filterOption}
                                        options={CONTRACT_STATUS_OPTIONS} onChange={onStatusChange}
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