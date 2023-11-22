import { TicketStatus } from 'models/ticketing-website/index.type';
export interface IOption {
  value: string;
  label: string;
}

// 合同状态枚举
export const CONTRACT_STATUS = {
  FAIL: 0,
  AUDIT_PENDING: 1,
  EXEC_PENDING: 2,
  EXECUTING: 3,
  FINISH: 4,
};

export const CONTRACT_STATUS_OPTIONS: IOption[] = [
  { value: TicketStatus.NEW, label: '待处理' },
  { value: TicketStatus.IN_PROGRESS, label: '处理中' },
  { value: TicketStatus.COMPLETED, label: '完成' },
  { value: TicketStatus.CLOSED, label: '关闭' },
];

// 合同类型枚举
export const CONTRACT_TYPES = {
  MAIN: 0,
  SUB: 1,
  SUPPLEMENT: 2,
};

export const CONTRACT_TYPE_OPTIONS: Array<IOption> = [
  { value: CONTRACT_TYPES.MAIN, label: '主合同' },
  { value: CONTRACT_TYPES.SUB, label: '子合同' },
  { value: CONTRACT_TYPES.SUPPLEMENT, label: '补充合同' },
];
export const BASE_INFO_DATA = [
  {
    name: '集群名',
    value: 'helloworld',
  },
  {
    name: '集群ID',
    value: 'cls - 2ntelvxw',
    type: {
      key: 'color',
      value: 'blue',
    },
  },
  {
    name: '状态',
    value: '运行中',
    type: {
      key: 'color',
      value: 'green',
    },
  },
  {
    name: 'K8S版本',
    value: '1.7.8',
  },
  {
    name: '配置',
    value: '6.73 核 10.30 GB',
  },
  {
    name: '所在地域',
    value: '广州',
  },
  {
    name: '新增资源所属项目',
    value: '默认项目',
  },
  {
    name: '节点数量',
    value: '4 个',
  },
  {
    name: '节点网络',
    value: 'vpc - 5frmkm1x',
    type: {
      key: 'color',
      value: 'blue',
    },
  },
  {
    name: '容器网络',
    value: '172.16.0.0 / 16',
  },
  {
    name: '集群凭证',
    value: '显示凭证',
    type: {
      key: 'color',
      value: 'blue',
    },
  },
  {
    name: '创建/更新',
    value: '2018-05-31 22:11:44 2018-05-31 22:11:44',
    type: {
      key: 'contractAnnex',
      value: 'pdf',
    },
  },
  {
    name: '描述',
    value: 'istio_test',
  },
];
