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
  message_id: string;
  ticket_id: string;
  sender: string;
  content: string;
  message_time: string;
  message_type: MessageType; // Assuming MessageType is a string enum
  file_id: string;
  file_url: string;
}


export interface TicketFilter {
  search_criteria?: string;
  status?: TicketStatus;
  start_date?: string;
  end_date?: string;
}

export interface UserProfile {
  user_id: string;
  name: string;
  email?: string | null;
  phone?: string | null;
  avatar?: string | null;
  avatar_url?: string | null;
  info?: { [key: string]: any } | null;
  password?: string | null;
}
