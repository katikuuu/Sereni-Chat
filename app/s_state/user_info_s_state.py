from .base_s_state import BaseSState
from model import UserInfoEntity


class LoggedinUserInfoSState(BaseSState[UserInfoEntity]):
    @staticmethod
    def get_name() -> str:
        return "loggedin_user_info"