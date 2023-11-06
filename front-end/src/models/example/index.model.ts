import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import { RootState } from "store";

// get state from http://127.0.0.1:5000/getVideosDetail
export const getTestRequest = createAsyncThunk(
    "test/getTestRequest",
    async () => {
        const response = await fetch("http://127.0.0.1:5000/getVideosDetail");
        return response.json();
    },
);

const initialState = {
    initData: {},
    testData: "123",
};

// store initData
// use createSlice Modify initData
const exampleSlice = createSlice({
    name: "video",
    initialState,
    reducers: {
        init: (state, action) => {
            state.initData = action.payload;
        },
        changeData: (state, action) => {
            state.testData = "456";
        },
    },
    extraReducers:
    (builder) => {
        builder.addCase(getTestRequest.fulfilled, (state, action) => {
            state.initData = action.payload;
        });
    },
});

export const { init, changeData } = exampleSlice.actions;

// selector
export const selectInitData = (state: RootState) => state.exampleData.initData;
export const selectTestData = (state: RootState) => state.exampleData.testData;
export default exampleSlice.reducer;
// Path: src\componens\video\index.tsx
