import { IChatRecord, ITicketRecord, TicketFilter, UserProfile } from "./interface.type";

export interface ITicketState {
    ticketRecordlist: ITicketRecord[];
    chatRecord: IChatRecord[];
    allUser: UserProfile[];
    ticket_filter:TicketFilter,
}