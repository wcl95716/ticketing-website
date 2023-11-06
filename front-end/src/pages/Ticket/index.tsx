import React, { useState, memo, useEffect } from 'react';
import { useAppDispatch, useAppSelector } from 'modules/store';
import { selectListSelect, getList, clearPageState } from 'modules/list/select';
import SearchForm from './components/SearchForm';
// import { StatusMap, ContractTypeMap, PaymentTypeMap } from '../Base';

// import './index.module.less';
// import classnames from 'classnames';
// import CommonStyle from '../../../styles/common.module.less';


import {
   UserOutlined,
} from "@ant-design/icons";
import type { MenuProps } from "antd";
import {
   Breadcrumb, Layout, Menu, theme, Table, Form, Input, Select, DatePicker, Button, Row
} from "antd";
// import { useStyles } from "./index.style";
// import { columns, DataType } from "./index.data";

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

const data: DataType[] = [];
for (let i = 0; i < 100; i++) {
   data.push({
      key: i,
      name: `Edward ${i}`,
      age: 32,
      address: `London Park no. ${i}`,
   });
}


export const SelectTable = () => {
   const dispatch = useAppDispatch();
   const pageState = useAppSelector(selectListSelect);
   const [selectedRowKeys, setSelectedRowKeys] = useState<(string | number)[]>([0, 1]);
   const [visible, setVisible] = useState(false);
   const { loading, contractList, current, pageSize, total } = pageState;

   useEffect(() => {
      dispatch(
         getList({
            pageSize: pageState.pageSize,
            current: pageState.current,
         }),
      );
      return () => {
         dispatch(clearPageState());
      };
   }, []);

   function onSelectChange(value: (string | number)[]) {
      setSelectedRowKeys(value);
   }

   function rehandleClickOp(record: any) {
      console.log(record);
   }

   function handleClickDelete(record: any) {
      console.log(record);
      setVisible(true);
   }

   function handleClose() {
      setVisible(false);
   }

   return (
      <>
         <Row justify='start' style={{ marginBottom: '20px' }}>
            <SearchForm
               onSubmit={async (value) => {
                  console.log(value);
               }}
               onCancel={() => { }}
            />
         </Row>
         <Table
            loading={loading}
            // data={contractList}
            columns={[
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
                  dataIndex: "address",
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
                        {/* <Button type="primary" style={{ marginRight: 8 }}  onClick={() => handleView(record.name)}>查看</Button>
                 <Button type="default" onClick={() => showModal(record.name)} danger><DeleteOutlined /></Button> */}
                     </div>
                  ),
               }
            ]}
            rowKey='index'
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
      </>
   );
};

const ticketPage: React.FC = () => (
   <div>
      <SelectTable />
   </div>
);

export default memo(ticketPage);