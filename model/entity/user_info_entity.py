from typing import Any, List

class UserInfoEntity:
    def __init__(self, username: str, hashed_password: str) -> None:
        self._username = username
        self._hashed_password = hashed_password

    @property
    def username(self) -> str:
        return self._username

    @property
    def hashed_password(self) -> str:
        return self._hashed_password

    def check_is_same(self, other: Any) -> bool:
        return False

    @staticmethod
    def get_column_names() -> List[str]:
        return ["username", "hashed_password"]