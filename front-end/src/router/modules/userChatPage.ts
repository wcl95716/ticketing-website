import { lazy } from 'react';
import { ViewModuleIcon } from 'tdesign-icons-react';
import { IRouter } from '../index';
import DetailModel from '../../pages/Ticket/components/DetailModel';

const result: IRouter[] = [
  {
    path: '/user_chat_page',
    Component: lazy(() => import('pages/Login')),
    isFullPage: true,
    meta: {
      hidden: true,
    },
  },
];

export default result;

