
import React, { useState, memo, useEffect } from 'react';
import { getTicketListRequest, getAllUserRequest, updateTicket, selecAllUser, selectTicketRecordList, deleteTicketListRequest,selecTicketFilter } from 'models/ticketing-website/index.model';
import SearchForm from './components/SearchForm';
import { useNavigate } from 'react-router-dom';
import {
   DeleteOutlined,
} from "@ant-design/icons";
import type { MenuProps } from "antd";
import {
   Modal, Layout, Popconfirm, theme, Table, message, Input, Select, DatePicker, Button, Row, Badge
} from "antd";
import Style from './index.module.less';
import type { ColumnsType } from 'antd/es/table';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { concat } from 'lodash';

export interface DataType {
   key: React.Key;
   name: string;
   age: number;
   address: string;
}
const { Option } = Select;
const { RangePicker } = DatePicker;
const {
   Header, Content, Footer, Sider,
} = Layout;
type MenuItem = Required<MenuProps>["items"][number];

// const data: DataType[] = [];

const ticketPage: React.FC = () => {
   const dispatch = useAppDispatch();
   const [data, setData] = useState([]);
   const [loading, setLoading] = useState(false);
   const navigate = useNavigate();
   const ticketRecordList = useAppSelector(selectTicketRecordList);
   const allUserList = useAppSelector(selecAllUser);

   const ticketFilter = useAppSelector(selecTicketFilter);
   console.log("查看筛选filter",ticketFilter)

   const pageInit = async () => {
      setLoading(true);
      await dispatch(getTicketListRequest(ticketFilter));
      setLoading(false);
    };

   useEffect(() => {
      pageInit();
      // dispatch(getTicketListRequest({}))
      dispatch(getAllUserRequest())
   }, []);

   useEffect(() => {
      setData(ticketRecordList);
   }, [ticketRecordList]);


   const deleteConfirm = (record: DataType) => {
      dispatch(deleteTicketListRequest(record?.ticket_id)).then(() => {
         // dispatch(getTicketListRequest({}));
      });
   };

   // onView 函数
const onView = (record: DataType) => {
   // 检查 record 是否存在且包含 ticket_id
   if (record && record?.ticket_id) {
       // 构建新的 URL，将 ticket_id 作为查询参数
       const urlWithTicketId = `/ticket/index/detail?ticket_id=${record.ticket_id}`;
       // 使用新的 URL 进行导航
       navigate(urlWithTicketId);
   }
};

   const renderStatus = (status: any) => {
      let statusText;

      switch (status) {
         case 0:
            statusText = '待处理';
            status = "error"
            break;
         case 1:
            statusText = '处理中';
            status = "processing"
            break;
         case 2:
            statusText = '处理完成';
            status = 'success';
            break;
         case 3:
            statusText = '关闭工单';
            status = "default"
            break;
         default:
            statusText = '未知状态';
            status = "default"
      }

      return <Badge text={statusText} status={status} />;
   };
   // Filter `option.label` match the user type `input`
   const filterOption = (input: string, option?: { label: string; value: string }) =>
      (option?.label ?? '').toLowerCase().includes(input.toLowerCase());



   const renderCreator = (assigned_to: any, record: any) => {
      const userOption = [];
      allUserList.forEach((item) => {
         userOption.push({
            label: item?.name,
            value: item?.user_id
         })
      })
      // 定义内部函数，用于处理选择变更
      const onValueChange = (value) => {
         const updateRecord = {...record, assigned_to: value === undefined ? null : value };
         console.log(updateRecord)
         dispatch(updateTicket(updateRecord)).then(()=>{
            dispatch(getTicketListRequest({}));
         });
      };
      return <Select defaultValue={assigned_to} style={{ width: 120 }} allowClear showSearch filterOption={filterOption}
         options={userOption} onChange={onValueChange}
      >
      </Select>
   }
   const columns: ColumnsType<DataType> = [
      {
         title: "工单ID",
         width: 100,
         dataIndex: "ticket_id",
         key: "ticket_id",
         // fixed: "left",
      },
      {
         title: "标题",
         width: 100,
         dataIndex: "title",
         key: "title",
         //   fixed: 'left',
      },
      {
         title: "处理人",
         dataIndex: "assigned_to",
         key: "1",
         width: 150,
         render: (assigned_to, record) => renderCreator(assigned_to, record)
      },
      {
         title: "状态",
         dataIndex: "status",
         key: "2",
         width: 150,
         render: (status) => renderStatus(status)
      },
      {
         title: "创建时间",
         dataIndex: "created_time",
         key: "3",
         width: 150,
      },
      {
         title: "更新时间",
         dataIndex: "address",
         key: "4",
         width: 150,
      },
      {
         title: "操作",
         key: "operation",
         fixed: "right",
         width: 80,
         render: (text, record) => (
            <div style={{ display: "flex" }}>
               <Button
                  type="primary"
                  style={{ marginRight: 8 }}
                  onClick={() => onView(record)}
                  size="small"
               >
                  查看
               </Button>

               <Popconfirm
                  title="删除工单"
                  description="你确定删除此条工单吗?"
                  onConfirm={() => deleteConfirm(record)}
                  // onCancel={cancel}
                  okText="确定"
                  cancelText="取消"
               >
                  <Button
                     type="primary"
                     danger size="small"
                     shape="circle"
                  ><DeleteOutlined style={{ color: 'white' }} />
                  </Button>
               </Popconfirm>
            </div>
         ),
      }
   ]

   return (
      <div>
         <Row justify='start' style={{ marginBottom: '20px' }}>
            <div style={{ width: '100%', backgroundColor: '#fff' }}>
               <SearchForm
                  onSubmit={async (value) => {
                     console.log(value);
                  }}
                  onCancel={() => { }}
               />
            </div>
         </Row>
         <Table
            className={Style.list_ticket_table}
            loading={loading}
            size="large"
            dataSource={data}
            columns={columns}
            rowKey='ticket_id'
            scroll={{ x: 1300 }}
         />
      </div>
   );
}
export default memo(ticketPage);