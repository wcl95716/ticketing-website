import { IChatRecord, ITicketRecord, TicketFilter, UserProfile, UserDetail } from "./interface.type";

export interface ITicketState {
    ticketRecordlist: ITicketRecord[];
    chatRecord: IChatRecord[];
    allUser: UserProfile[];
    userDetail: UserDetail;
    ticketDetail: UserDetail;
    ticket_filter:TicketFilter,
}
