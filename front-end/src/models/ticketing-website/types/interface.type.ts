import { MessageType, Priority, TicketStatus } from "./enmu.type";

export interface ITicketRecord {
  ticket_id: string;
  title: string;
  created_time: string;
  status: TicketStatus; // You can use the enum type for TicketStatus here if needed
  priority: Priority; // You can use the enum type for Priority here if needed
  creator: string;
  assigned_to: string | null; // Use null for optional fields
  ticket_type: string;
  closed_time: string | null; // Use null for optional fields
}

export interface IChatRecord {
  message_id: number;
  ticket_id: number;
  sender: string;
  content: string;
  message_time: string;
  message_type: MessageType; // Assuming MessageType is a string enum
}
