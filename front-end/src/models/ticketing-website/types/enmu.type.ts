enum TicketStatus {
  NEW = 0,
  IN_PROGRESS = 1,
  COMPLETED = 2,
  CLOSED = 3,
}

enum Priority {
  HIGHEST = 0,
  URGENT = 1,
  NORMAL = 2,
  NOT_URGENT = 3,
  NOT_NEEDED = 4,
}

enum MessageType {
  TEXT = 0,
  IMAGE = 1,
  VIDEO = 2,
  OPERATION = 3,
}

enum FileType {
  TEXT = 1,
  IMAGE = 2,
  AUDIO = 3,
  VIDEO = 4,
  PDF = 5,
  WORD = 6,
  EXCEL = 7,
  POWERPOINT = 8,
  ZIP = 9,
  OTHER = 10,
}

enum ChatPriority {
  LOw = 1,
  MEDIUM = 2,
  HIGH = 3,
  URGENT = 4,
  User = 1000,
  Customer = 1001,
}

export { TicketStatus, Priority, MessageType, FileType, ChatPriority };
