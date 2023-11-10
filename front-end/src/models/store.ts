// use configureStore to create a store

import { configureStore } from "@reduxjs/toolkit";
import exampleSliceReducer from "./example/index.model";
import ticketSliceReducer from "./ticketing-website/index.model";
import { TypedUseSelectorHook, useSelector, useDispatch } from 'react-redux';

export const storeModels = configureStore({
    reducer: {
        exampleData: exampleSliceReducer,
        ticketWebsiteData:ticketSliceReducer,
    },
});


export type RootStateModels = ReturnType<typeof storeModels.getState>;
export type AppDispatchModels = typeof storeModels.dispatch;

export const useModelsDispatch = () => useDispatch<AppDispatchModels>();
export const useModelsSelector: TypedUseSelectorHook<RootStateModels> = useSelector;

export default storeModels;

