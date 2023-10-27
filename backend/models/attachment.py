

from backend.models.types import FileType


class Attachment:
    def __init__(self, attachment_id: int, ticket_id: int, filename: str, file_type: FileType, file_size: int, upload_time: str, file_url: str):
        self.attachment_id = attachment_id  # 附件ID
        self.ticket_id = ticket_id  # 关联的工单ID
        self.filename = filename  # 文件名
        self.file_type = file_type  # 文件类型
        self.file_size = file_size  # 文件大小
        self.upload_time = upload_time  # 上传时间
        self.file_url = file_url  # 附件文件的URL或路径

