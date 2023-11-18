

# 帮我创建一个用户类型
# 每个变量标注类型
# 用来创建用户对象
# 包含 id, name, phone , email,avatar , password
class UserProfile:
    def __init__(self, user_id:str, name:str, email:str = None, phone:str = None,avatar:str = None,avatar_url:str = None, info:dict = None,password:str = None):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.phone = phone
        self.avatar = avatar
        self.avatar_url = avatar_url
        self.info = info
        self.password = password
        
    def to_dict(self):
        return self.__dict__
        pass 
    
    @classmethod
    def from_dict(cls , user_dict:dict):
        return cls(**user_dict)
        pass
    

def test():
    test_user = UserProfile("1","2","3","4")
    print(1 ,test_user.to_dict())

    test2 = UserProfile.from_dict(test_user.to_dict())
    print(2, test2.to_dict())
    
    test3 = {'user_id': '1', 'name': '2', 'email': '3',}
    
    test4 = UserProfile.from_dict(test3)
    
    print(3, test4.to_dict())
    
def get_test_user():
    # 随机生成一个用户
    from faker import Faker

    # 创建 Faker 实例
    faker = Faker('zh_CN')
    name = faker.name()
    email = faker.email()
    phone = faker.phone_number()
    avatar = faker.image_url()
    avatar_url = faker.image_url()
    password = faker.password()
    user_id = str(faker.uuid4())  # 将 UUID 转换为字符串
    return UserProfile(user_id, name, email, phone, avatar,avatar_url, password=password)


