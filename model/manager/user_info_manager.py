from typing import Dict, List

from ..handler import JsonHandler

class UserInfoManager:   
    @staticmethod
    def get_registered_users_dict() -> Dict:
        return JsonHandler.load_json(json_file_path="./data/user_info.json")
    
    @staticmethod
    def get_registered_username_list() -> List:
        return JsonHandler.load_json(json_file_path="./data/user_info.json").keys()
    
    @staticmethod
    def get_registered_password_list() -> List:
        return JsonHandler.load_json(json_file_path="./data/user_info.json").values()
    
    @staticmethod
    def save_signup_user_info(data: Dict, new_data: Dict):
        JsonHandler.save_json(data=data, new_data=new_data, json_file_path="./data/user_info.json")