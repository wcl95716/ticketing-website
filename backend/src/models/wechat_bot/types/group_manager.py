
import PyOfficeRobot


# def check_group(who_group ,customer_service_names = [] , group_mark = GroupMark.NULL ):

#     print("who_group: ",who_group ,group_mark  )
#     if group_mark == GroupMark.NULL:
#         res = is_find_customer_service(wx.GetAllMessage,customer_service_names)
#         print("寻找客户提问 ",res)
#         if res != None:
#             group_mark = GroupMark.FIND_START_MESSAGE
#             print("发现客户提问,开始计时")
#             wx.SendMsg("发现客户提问,开始计时,%s"%(datetime.datetime.now() ), who_group)
#             pass
    
#     if group_mark != GroupMark.CUSTOMER_SERVICE_REPLY or group_mark != GroupMark.NULL:
#         print("寻找客服回复")
#         if customer_service_reply(wx.GetAllMessage,customer_service_names) != None:
#             group_mark = GroupMark.NULL
#             print("客服回复了")
#             wx.SendMsg("客服回复,结束计时,%s"%(datetime.datetime.now()), who_group)
#         pass 
    
#     if group_mark == GroupMark.FIND_START_MESSAGE:
#         res = find_start_message(wx.GetAllMessage)
#         print("开始计时 ",res)
#         if res > 10: 
#             group_mark = GroupMark.FIND_PHONE_MESSAGE
#             print("超时,机器人正在电话联系客服",res)
#             wx.SendMsg("超时,机器人正在电话联系客服,%s"%(datetime.datetime.now()), who_group)
#             Sample.main(sys.argv[1:])
#             pass

class GroupChatManager:
    
    def __init__ (self, group_id: str,):
        self.group_id = group_id
        pass
    
    def send_chat_message(self, message: str):
        PyOfficeRobot.chat.send_message(who=self.group_id, message=message)
        pass
    
    def get_chat_message(self):
        pass
    pass 




class GroupManager:
    
    def __init__(self, group_list: list[GroupChatManager]):
        self.group_list = group_list
        pass
    
    
    pass 



keywords = {
    "我要报名": "你好，这是报名链接：www.python-office.com",
    "点赞了吗？": "点了",
    "关注了吗？": "必须的",
    "投币了吗？": "三连走起",
}
PyOfficeRobot.chat.chat_by_keywords(who='抖音：程序员晚枫', keywords=keywords)