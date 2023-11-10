import { createAsyncThunk, createSlice } from '@reduxjs/toolkit';
import { RootStateModels } from 'models/store';
import { ITicketState } from './types/model.type';
import { ITicketRecord } from './index.type';

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
      // state.ticketRecordlist = action.payload;
    });
  },
});

export const { init, changeData } = ticketWebsiteSlice.actions;
// selector
export const selectTicketRecordList = (stateModels: RootStateModels) => [];

export default ticketWebsiteSlice.reducer;
