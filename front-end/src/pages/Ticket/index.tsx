import React, { useState, memo, useEffect } from 'react';
// import { useAppDispatch, useAppSelector } from 'modules/store';
import { selectListSelect, getList, clearPageState } from 'modules/list/select';
import { getTicketListRequest, selectTicketRecordList } from 'models/ticketing-website/index.model';
import SearchForm from './components/SearchForm';
import { useNavigate } from 'react-router-dom';
import {
   DeleteOutlined,
} from "@ant-design/icons";
import {
   UserOutlined,
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

// //模拟列表数据
// for (let i = 0; i < 100; i++) {
//    data.push({
//       key: i,
//       name: `Edward ${i}`,
//       age: 32,
//       address: `London Park no. ${i}`,
//    });
// }
const ticketPage: React.FC = () => {
   const dispatch = useAppDispatch();
   const pageState = useAppSelector(selectListSelect);
   const [selectedRowKeys, setSelectedRowKeys] = useState<(string | number)[]>([0, 1]);
   const { loading, contractList, current, pageSize, total } = pageState;
   const [modal, contextHolder] = Modal.useModal();
   const [visible, setVisible] = useState(false);
   const [data, setData] = useState([]);
   const navigate = useNavigate();
   const config = {
      title: '删除工单!',
      content: (
         <>
            <span>是否确认删除？</span>
         </>
      ),
   };

   // useEffect(() => {
   //    dispatch(
   //       getList({
   //          pageSize: pageState.pageSize,
   //          current: pageState.current,
   //       }),
   //    );
   //    return () => {
   //       dispatch(clearPageState());
   //    };
   // }, []);



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
                  //    onClick={() => setVisible(!visible)}
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
   console.log("查看data",data)
   console.log("查看Style111", Style, Style.list_ticket_table)
   console.log("查看loading",loading)
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
         {/* <Dialog header='确认删除当前所选合同？' visible={visible} onClose={handleClose}>
            <p>删除后的所有合同信息将被清空,且无法恢复</p>
         </Dialog> */}
         {/* {visible && <DetailModel visible={visible} />} */}
      </div>
   );
}
export default memo(ticketPage);