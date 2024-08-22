from ..handler import HashHandler
from model import UserInfoManager

class SignupManager:
    @staticmethod
    def validate_password(password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char.islower() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char in "!@#$%^&*(),.?\":{}|<>" for char in password):
            return False
        return True

    @staticmethod
    def signup(username: str, password: str, retype_password: str) -> tuple[bool, str]:
        registered_users = UserInfoManager.get_registered_users_dict()

        if username in registered_users:
            return False, "User already exists. Please try another username."

        if not SignupManager.validate_password(password):
            return False, "Password must be at least 8 characters long, include both uppercase and lowercase letters, a number, and a special character."

        if password != retype_password:
            return False, "Retype your password correctly."
        
        hashed_password = HashHandler.hash_password(password=password)
        UserInfoManager.save_signup_user_info(data=registered_users, new_data={username: hashed_password})

        return True, "Signup successful"
