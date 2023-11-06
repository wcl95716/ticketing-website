// use configureStore to create a store

import { configureStore } from "@reduxjs/toolkit";
import exampleSliceReducer from "./models/example/index.model";

export const store = configureStore({
    reducer: {
        exampleData: exampleSliceReducer,
    },
});

// RootState is the type of the root state
export type RootState = ReturnType<typeof store.getState>;
