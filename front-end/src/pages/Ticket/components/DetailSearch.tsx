import React, { useRef, useState, memo, useEffect } from 'react';
import {
    Row, Col,
    Breadcrumb, Layout, Menu, theme, Table, Form, Input, Button, Select, DatePicker
} from "antd";
import { CONTRACT_STATUS_OPTIONS, CONTRACT_TYPE_OPTIONS, IOption } from '../consts';
import { FormInstanceFunctions, SubmitContext } from 'tdesign-react/es/form/type';
import { getTicketListRequest, getAllUserRequest, getTicketDetail, getUserDetail, updateTicket, selecAllUser, selecUserDetail, selecTicketDetail } from 'models/ticketing-website/index.model';
import Style from './DetailSearch.module.less';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { useNavigate } from 'react-router-dom';
import { ITicketRecord } from 'models/ticketing-website/index.type';


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
    record:ITicketRecord;
};

const SearchForm: React.FC<SearchFormProps> = (props) => {
    
    const { record } = props;
    const [selectedUser, setSelectedUser] = useState(record?.assigned_to);
    const [selectRecord, setSelectRecord] = useState(record);
    // console.log("reeeec",record)
    const dispatch = useAppDispatch();
    const navigate = useNavigate();
    const searchParams = new URLSearchParams(location.search);
    const ticket_id = searchParams.get('ticket_id');
    const formRef = useRef<FormInstanceFunctions>();
    
    const allUserList = useAppSelector(selecAllUser);
    // const userInfo = useAppSelector(selecUserDetail);
    // const record = useAppSelector(selecTicketDetail);
    // console.log("查看search的record",record)

    // const userOption: { label: string; value: string; }[] = [];
    // allUserList.forEach((item) => {
    //     userOption.push({
    //         label: item?.name || '',
    //         value: item?.user_id || ''
    //     });
    // });
    const [userOption, setUserOption] = useState<IOption[]>([]);

    useEffect(() => {
      // 在组件挂载或 allUserList 发生变化时更新 userOption
      const updatedUserOption = allUserList.map((item) => ({
        label: item?.name || '',
        value: item?.user_id || ''
      }));
      setUserOption(updatedUserOption);
    //   console.log("查看userOption",userOption)
    }, [allUserList,record]); // 监听 allUserList 的变化
    
    
    useEffect(() => {
        dispatch(getTicketListRequest({}))
        dispatch(getAllUserRequest())
    }, [ticket_id]);

    useEffect(() => {
        setSelectedUser(record.assigned_to);
        // dispatch(getUserDetail(record.assigned_to || ''));
    }, [record]);
    // useEffect(() => {
    //     dispatch(getUserDetail(record?.assigned_to));
    //  }, [record])

    const onUserChange = (value) => {
        setSelectedUser(value);
        const updateRecord = { ...record, assigned_to: value === undefined ? null : value };
        setSelectRecord(updateRecord);
        dispatch(updateTicket(updateRecord)).then(() => {
            // dispatch(getUserDetail(value));
            dispatch(getTicketListRequest({}));
        });
    }
    const onStatusChange = (value) => {
        const updateRecord = { ...record, status: value === undefined ? null : value };
        setSelectRecord(updateRecord);
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

    const [editedTitle, setEditedTitle] = useState(record?.title); // 用于存储编辑后的标题
  
    const handleTitleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
      setEditedTitle(event.target.value); // 当<input>的值发生变化时更新editedTitle的值
    };
  
    const handleSaveClick = () => {

      const updateRecord = { ...selectRecord, title: editedTitle };
      setSelectRecord(updateRecord);
      dispatch(updateTicket(updateRecord)).then(() => {
          // dispatch(getUserDetail(value));
          dispatch(getTicketListRequest({}));
      });
    };

    return (
        <div className={Style.ticketsearch}>
            <Form>
                <Row>
                    <Col flex='1'>
                        <Row gutter={[16, 16]} style={{ alignItems: 'center' }}>
                            <Col>
                                {/* <div style={{ margin: '10px', fontWeight: 'bold' }}>{`${record?.title}`}</div> */}
                                <div style={{ display: 'flex', alignItems: 'center', margin: '10px', fontWeight: 'bold' }}>
                                    <Input
                                        value={editedTitle}
                                        onChange={handleTitleChange}
                                    />
                                    <Button type="primary" onClick={handleSaveClick}>保存</Button>
                                </div>
                            </Col>
                            <Col>
                                <Button style={{borderRadius: '0px'}} size='small'  onClick={redirectToTicketList}>返回列表</Button>
                            </Col>
                        </Row>
                        <Row gutter={[16, 16]}>
                            <Col >
                                <Form.Item label='' name='name' >
                                    <Select  defaultValue={record.assigned_to} style={{ width: 120 }} placeholder="无处理人" allowClear showSearch filterOption={filterOption}
                                        options={userOption} onChange={onUserChange}
                                    >
                                    </Select>
                                </Form.Item>

                            </Col>
                            <Col >
                                <Form.Item name='status' >
                                    <Select defaultValue={record.status} style={{ width: 120 }} placeholder="请选择处理状态" allowClear showSearch filterOption={filterOption}
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