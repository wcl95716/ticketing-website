import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { ITicketState } from './types/model.type';
import { ITicketRecord } from './index.type';
import { RootState } from 'modules/store';

// get state from http://127.0.0.1:5000/getVideosDetail
export const getTicketListRequest = createAsyncThunk('getTestRequest', async () => {
  // 获取数据
  const response = await fetch('http://47.103.45.149:8001/test/get_all_tickets');
  console.log('getTicketListRequest response ', response);
  // 返回数据
  return response.json() as unknown as ITicketRecord[];
});

export const paramsTest = createAsyncThunk('paramsTest', async (id: string) => {
  console.log('paramsTest id ', id);
  return id;
});

const initialState: ITicketState = {
  ticketRecordlist: [],
  test: 'test',
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
    changeData: (state) => {
      state.test = '111';
    },
    changeData2: (state, action) => {
      state.test = action.payload;
    },
  },
  extraReducers: (builder) => {
    builder
      .addCase(getTicketListRequest.fulfilled, (state, action) => {
        console.log('extraReducers fulfilled action ', action.payload);
        state.ticketRecordlist = action.payload;
        state.test = '2222';
      })
      .addCase(getTicketListRequest.pending, (state, action) => {
        console.log('extraReducers  pending action ', action.payload);
        state.ticketRecordlist = [];
      })
      .addCase(getTicketListRequest.rejected, (state, action) => {
        console.log('extraReducers  rejected action ', action.payload);
        state.ticketRecordlist = [];
      })
      .addCase(paramsTest.fulfilled, (state, action) => {
        state.test = action.payload;
      });
  },
});

export const { init, changeData, changeData2 } = ticketWebsiteSlice.actions;
// selector
export const selectTicketRecordList = (state: RootState) => state.ticketWebsiteData.ticketRecordlist;
export const selectTest = (state: RootState) => state.ticketWebsiteData.test;

export default ticketWebsiteSlice.reducer;
