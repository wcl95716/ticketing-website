import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { ITicketState } from './types/model.type';
import { IChatRecord, ITicketRecord } from './index.type';
import { RootState } from 'modules/store';

// get state from http://127.0.0.1:8001/getVideosDetail
export const getTicketListRequest = createAsyncThunk('test/getTestRequest', async () => {
  const response = await fetch('http://47.116.201.99:8001/test/get_all_tickets');
  return response.json() as unknown as ITicketRecord[];
});

//根据id获取聊天信息
export const getChatRequest = createAsyncThunk('paramsTest', async (ticket_id: string) => {
  const response = await fetch(`http://47.116.201.99:8001/test/get_chat_history/${ticket_id}`);
  return response.json() as unknown as IChatRecord[];
});

//发送消息的post请求
export const postChatRequest = createAsyncThunk('postChatRequest', async (updatedMessages: IChatRecord) => {
  const response = await fetch(`http://47.116.201.99:8001/test/add_chat_record`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    // 如果你需要发送请求体数据，可以在这里添加
    body: JSON.stringify(updatedMessages)
  });
  return response.json() as unknown as IChatRecord[];
});


const initialState: ITicketState = {
  ticketRecordlist: [],
  chatRecord: []
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
    }
  },
  extraReducers: (builder) => {
    builder
    .addCase(getTicketListRequest.fulfilled, (state, action) => {
      console.log('action ', action.payload);
      state.ticketRecordlist = action.payload;
    })
    .addCase(getChatRequest.fulfilled, (state, action) => {
      state.chatRecord = action.payload;
    });
  },
});

export const { init, changeData, changeChatData } = ticketWebsiteSlice.actions;
// selector
export const selectTicketRecordList = (state: RootState ) => state.ticketWebsiteData.ticketRecordlist;
export const selecChatRecord = ( state: RootState ) => state.ticketWebsiteData.chatRecord;

export default ticketWebsiteSlice.reducer;