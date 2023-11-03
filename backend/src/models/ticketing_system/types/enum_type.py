from enum import Enum

class TicketStatus(Enum):
    NEW = 0
    IN_PROGRESS = 1
    COMPLETED = 2
    CLOSED = 3

class Priority(Enum):
    HIGHEST = 0
    URGENT = 1
    NORMAL = 2
    NOT_URGENT = 3
    NOT_NEEDED = 4

class MessageType(Enum):
    TEXT = 0
    IMAGE = 1
    VIDEO = 2
    OPERATION = 3

class FileType(Enum):
    TEXT = 1
    IMAGE = 2
    AUDIO = 3
    VIDEO = 4
    PDF = 5
    WORD = 6
    EXCEL = 7
    POWERPOINT = 8
    ZIP = 9
    OTHER = 10
