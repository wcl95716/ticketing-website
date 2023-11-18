import { IChatRecord, ITicketRecord } from "./interface.type";

export interface ITicketState {
    ticketRecordlist: ITicketRecord[];
    chatRecord: IChatRecord[];
    allUser: ITicketRecord[];
}