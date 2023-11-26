



from models.ticketing_system.utils import user_storage
from models.ticketing_system.types import user_profile
from models.ticketing_system.types.user_profile import UserProfile


def add_users(user_json: dict):
    user =  UserProfile.from_dict(user_json)
    user_storage.add_user_to_file(user)
    pass

def get_users() -> list[dict]:
    return user_storage.get_users_to_file()
    pass 

def get_user(user_id: str ) ->  UserProfile:
    if user_id is None:
        return None
    return user_storage.get_user_by_id(user_id)
    pass

def update_user(user_json: dict):
    user =  UserProfile.from_dict(user_json)
    user_storage.update_user(user)
    pass




