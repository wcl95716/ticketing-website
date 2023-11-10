import React, { useState, memo, useEffect } from 'react';
import { Table, Dialog, Button, Row } from 'tdesign-react';
// import { useAppDispatch, useAppSelector } from 'modules/store';
import { selectListSelect, getList, clearPageState } from 'modules/list/select';
import SearchForm from './components/SearchForm';
import { StatusMap, ContractTypeMap, PaymentTypeMap } from '../Base';

import './index.module.less';
import classnames from 'classnames';
import CommonStyle from '../../../styles/common.module.less';
import { getTicketListRequest, selectTicketRecordList } from 'models/ticketing-website/index.model';
import { selectStateName } from 'models/example/index.model';
import { useSelector } from 'react-redux';
import { useAppDispatch, useAppSelector } from 'modules/store';


export const SelectTable = () => {
  const dispatch = useAppDispatch();

  
  const ticketRecordList = useAppSelector(selectTicketRecordList);

  useEffect(() => {
    dispatch(getTicketListRequest())
  }, []);

  useEffect(() => {
    // dispatchModels(getTicketListRequest());
    console.log("ticketRecordList ",ticketRecordList)
  }, [ticketRecordList]);


  return (
    <>
    </>
  );
};

const selectPage: React.FC = () => (
  <div className={classnames(CommonStyle.pageWithPadding, CommonStyle.pageWithColor)}>
    <SelectTable />
  </div>
);

export default memo(selectPage);
