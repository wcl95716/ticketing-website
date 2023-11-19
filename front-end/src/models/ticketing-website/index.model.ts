import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { ITicketState } from './types/model.type';
import { IChatRecord, ITicketRecord, TicketFilter, TicketStatus, UserProfile, UserDetail } from './index.type';
import { RootState } from 'modules/store';
import { isNull } from 'lodash';

// get state from http://127.0.0.1:8001/getVideosDetail获取列表
export const getTicketListRequest = createAsyncThunk('test/postTestRequest', async (params?: TicketFilter) => {
  console.log('查询111', params);
  const response = await fetch(`http://47.116.201.99:8001/test/get_all_tickets`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // 如果你需要发送请求体数据，可以在这里添加
    body: JSON.stringify(params),
  });
  return response.json() as unknown as ITicketRecord[];
  // const response = await fetch('http://47.116.201.99:8001/test/get_all_tickets');
  // return response.json() as unknown as ITicketRecord[];
});

// 根据id删除列表信息
export const deleteTicketListRequest = createAsyncThunk('paramsTest', async (ticket_id: string) => {
  const response = await fetch(`http://47.116.201.99:8001/test/delete_ticket/${ticket_id}`);
  console.log('查看删除之后的response', response);
  return response.json() as unknown as IChatRecord[];
});

// 根据id获取聊天信息
export const getChatRequest = createAsyncThunk('paramsTest', async (ticket_id: string) => {
  const response = await fetch(`http://47.116.201.99:8001/test/get_chat_history/${ticket_id}`);
  return response.json() as unknown as IChatRecord[];
});

// 发送消息的post请求
export const postChatRequest = createAsyncThunk('postChatRequest', async (updatedMessages: IChatRecord) => {
  const response = await fetch(`http://47.116.201.99:8001/test/add_chat_record`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // 如果你需要发送请求体数据，可以在这里添加
    body: JSON.stringify(updatedMessages),
  });
  return response.json() as unknown as IChatRecord[];
});

// 获取全部客服列表
export const getAllUserRequest = createAsyncThunk('test/getAllUser', async () => {
  const response = await fetch('http://47.116.201.99:8001/test/get_users');
  return response.json() as unknown as ITicketRecord[];
});

// 根据user_id获取获取用户全部信息
export const getUserDetail = createAsyncThunk('getUserDetail', async (user_id: string) => {
  const response = await fetch(`http://47.116.201.99:8001/test/get_user/${user_id}`);
  return response.json() as unknown as UserDetail;
});



// 改变用户更新工单信息
export const updateTicket = createAsyncThunk('test/updateTicket', async (updatedTicket: IChatRecord) => {
  const response = await fetch(`http://47.116.201.99:8001/test/update_ticket`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    // 如果你需要发送请求体数据，可以在这里添加
    body: JSON.stringify(updatedTicket),
  });
  return response.json() as unknown as IChatRecord[];
});

const initialState: ITicketState = {
  ticketRecordlist: [],
  chatRecord: [],
  allUser: [],
  userDetail: {},
  ticket_filter: {
    search_criteria: null,
    status: null,
    start_date: null,
    end_date: null,
  },
};

// store initData
// use createSlice Modify initData
const ticketWebsiteSlice = createSlice({
  name: 'ticketWebsiteSlice',
  initialState,
  reducers: {
    init: (state, action) => {
      state.ticketRecordlist = action.payload;
    },
    changeData: (state, action) => {
      state.ticketRecordlist = [];
    },
    changeChatData: (state, action) => {
      state.chatRecord = [];
    },
    allUserData: (state, action) => {
      state.allUser = [];
    },
    userDetail: (state, action) => {
      state.userDetail = {};
    },
    // dispatch(updateTicketFilter({ search_criteria: 'test' , status: TicketStatus.NEW}));
    updateTicketFilter: (state, action) => {
      const ticketFilter: TicketFilter  = action.payload as TicketFilter;
      state.ticket_filter = { ...state.ticket_filter, ...ticketFilter };
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(getTicketListRequest.fulfilled, (state, action) => {
        state.ticketRecordlist = action.payload;
      })
      .addCase(getChatRequest.fulfilled, (state, action) => {
        state.chatRecord = action.payload;
      })
      .addCase(getUserDetail.fulfilled, (state, action) => {
        state.userDetail = action.payload;
      })
      .addCase(getAllUserRequest.fulfilled, (state, action) => {
        state.allUser = action.payload as unknown as UserProfile[];
      });
  },
});

export const { init, changeData, changeChatData, updateTicketFilter, userDetail } = ticketWebsiteSlice.actions;
// selector
export const selectTicketRecordList = (state: RootState) => state.ticketWebsiteData.ticketRecordlist;
export const selecChatRecord = (state: RootState) => state.ticketWebsiteData.chatRecord;
export const selecAllUser = (state: RootState) => state.ticketWebsiteData.allUser;
export const selecTicketFilter = (state: RootState) => state.ticketWebsiteData.ticket_filter;
export const selecUserDetail = (state: RootState) => state.ticketWebsiteData.userDetail;

export default ticketWebsiteSlice.reducer;
