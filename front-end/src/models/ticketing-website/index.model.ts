import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { ITicketState } from './types/model.type';
import { ITicketRecord } from './index.type';
import { RootState } from 'modules/store';

// get state from http://127.0.0.1:5000/getVideosDetail
export const getTicketListRequest = createAsyncThunk('test/getTestRequest', async () => {
  const response = await fetch('http://47.103.45.149:5000/test/get_all_tickets');
  return response.json() as unknown as ITicketRecord[];
});

const initialState: ITicketState = {
  ticketRecordlist: [],
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
  },
  extraReducers: (builder) => {
    builder.addCase(getTicketListRequest.fulfilled, (state, action) => {
      console.log('action ', action.payload);
      state.ticketRecordlist = action.payload;
    });
  },
});

export const { init, changeData } = ticketWebsiteSlice.actions;
// selector
export const selectTicketRecordList = (state: RootState ) => state.ticketWebsiteData.ticketRecordlist;

export default ticketWebsiteSlice.reducer;
