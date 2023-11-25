import hashlib

my_tuple = ('AI苏博蒂奇', '@Panda 工单通知  http://47.116.201.99:4000/user_chat_page?ticket_id=2023-11-26-934888605588&customer_id=Panda', '4219858241817')
hash_object = hashlib.sha256(repr(my_tuple).encode())
hash_value = hash_object.hexdigest()
print(hash_value)
