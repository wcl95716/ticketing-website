import React, { useState, memo, useEffect } from 'react';
import { getTicketListRequest, selectTicketRecordList } from 'models/ticketing-website/index.model';
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
   const navigate = useNavigate();
   const ticketRecordList = useAppSelector(selectTicketRecordList);

   useEffect(() => {
      dispatch(getTicketListRequest())
   }, []);

   useEffect(() => {
      setData(ticketRecordList);
   }, [ticketRecordList]);


   const deleteConfirm = (e: React.MouseEvent<HTMLElement>) => {
      console.log(e);
      message.success('Click on Yes');
   };

   const onView = (record: DataType) => {
      console.log("查看record", record)
      navigate('detail', { state: { ticket_id: record?.ticket_id } });
   };

   const cancel = (e: React.MouseEvent<HTMLElement>) => {
      console.log(e);
      message.error('Click on No');
   };

   const renderStatus = (status: any) => {
      let statusText;
      let statusColor;

      switch (status) {
         case 0:
            statusText = '待处理';
            //  statusColor = 'orange';
            status = "error"
            break;
         case 1:
            statusText = '处理中';
            //  statusColor = 'blue';
            status = "processing"
            break;
         case 2:
            statusText = '处理完成';
            //  statusColor = 'green';
            status = 'success';
            break;
         case 3:
            statusText = '关闭工单';
            //  statusColor = 'red';
            status = "default"
            break;
         default:
            statusText = '未知状态';
            status = "default"
         //  statusColor = 'default';
      }

      return <Badge text={statusText} status={status} />;
   };
   const renderCreator = (creator: any) => {
      return <Select defaultValue={creator} style={{ width: 120 }}>
         <Select.Option value="jack">客服1</Select.Option>
         <Select.Option value="lucy">客服2</Select.Option>
         <Select.Option value="Yiminghe">客服3</Select.Option>
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
         dataIndex: "creator",
         key: "1",
         width: 150,
         render: (creator) => renderCreator(creator)
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
                  onConfirm={deleteConfirm}
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
            // loading={loading}
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