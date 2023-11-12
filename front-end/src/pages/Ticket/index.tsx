import React, { useState, memo, useEffect } from 'react';
import { getTicketListRequest, selectTicketRecordList } from 'models/ticketing-website/index.model';
import SearchForm from './components/SearchForm';
import { useNavigate } from 'react-router-dom';
import {
   DeleteOutlined,
} from "@ant-design/icons";
import type { MenuProps } from "antd";
import {
   Modal, Layout, Popconfirm, theme, Table, message, Input, Select, DatePicker, Button, Row
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
   // const [selectedRowKeys, setSelectedRowKeys] = useState<(string | number)[]>([0, 1]);
   const [data, setData] = useState([]);
   const navigate = useNavigate();




   const ticketRecordList = useAppSelector(selectTicketRecordList);

   useEffect(() => {
      dispatch(getTicketListRequest())
   }, []);

   useEffect(() => {
      // dispatchModels(getTicketListRequest());
      console.log("ticketRecordList ", ticketRecordList,ticketRecordList instanceof Array)
      setData(ticketRecordList);
   }, [ticketRecordList]);


   const deleteConfirm = (e: React.MouseEvent<HTMLElement>) => {
      console.log(e);
      message.success('Click on Yes');
   };

   const onView = (record: DataType) => {
      navigate('detail', { state: { key: record.key } });
   };

   const cancel = (e: React.MouseEvent<HTMLElement>) => {
      console.log(e);
      message.error('Click on No');
   };
   const columns: ColumnsType<DataType> = [
      {
         title: "工单ID",
         width: 100,
         dataIndex: "name",
         key: "name",
         fixed: "left",
      },
      {
         title: "标题",
         width: 100,
         dataIndex: "age",
         key: "age",
         //   fixed: 'left',
      },
      {
         title: "处理人",
         dataIndex: "address",
         key: "1",
         width: 150,
      },
      {
         title: "状态",
         dataIndex: "address",
         key: "2",
         width: 150,
      },
      {
         title: "开始时间",
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
         width: 100,
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
                     type="default"
                     danger size="small"

                  ><DeleteOutlined />
                  </Button>
               </Popconfirm>
            </div>
         ),
      }
   ]

   return (
      <div>
         {/* <SelectTable /> */}
         <Row justify='start' style={{ marginBottom: '20px' }}>
            <SearchForm
               onSubmit={async (value) => {
                  console.log(value);
               }}
               onCancel={() => { }}
            />
         </Row>
         <Table
            className={Style.list_ticket_table}
            // loading={loading}
            size="large"
            dataSource={data}
            columns={columns}
            // rowKey='name'
            scroll={{ x: 1300 }}
         // selectedRowKeys={selectedRowKeys}
         // hover
         // onSelectChange={onSelectChange}
         // pagination={{
         //    pageSize,
         //    total,
         //    current,
         //    showJumper: true,
         //    onCurrentChange(current, pageInfo) {
         //       dispatch(
         //          getList({
         //             pageSize: pageInfo.pageSize,
         //             current: pageInfo.current,
         //          }),
         //       );
         //    },
         //    onPageSizeChange(size) {
         //       dispatch(
         //          getList({
         //             pageSize: size,
         //             current: 1,
         //          }),
         //       );
         //    },
         // }}
         />
      </div>
   );
}
export default memo(ticketPage);