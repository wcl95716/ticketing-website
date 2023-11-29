import { lazy } from 'react';
import { ViewModuleIcon } from 'tdesign-icons-react';
import { IRouter } from '../index';
import DetailModel  from '../../pages/Ticket/components/DetailModel'
import Monitor from 'pages/Ticket/Monitor';

const result: IRouter[] = [
  {
    path: '/ticket',
    meta: {
      title: '工单管理',
      Icon: ViewModuleIcon,
    },
    children: [
      {
        path: 'index',
        Component: lazy(() => import('pages/Ticket')),
        meta: {
          title: '工单列表',
        },
      },
      {
         path: 'index/detail',
         Component: DetailModel,
         meta: {
            title: '工单详情',
            hidden: true
          },
       },
       {
        path: 'index/monitor',
        Component: Monitor,
        meta: {
           title: '监控日志分发',
         },
      },
    ],
  },
];

export default result;