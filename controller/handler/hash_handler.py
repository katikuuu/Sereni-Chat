import hashlib

class HashHandler:
    @staticmethod
    def hash_password(password: str) -> str:
        # パスワードをバイト列に変換する
        password_bytes = password.encode('utf-8')

        # ハッシュ化アルゴリズムを選択する
        hash_algorithm = hashlib.sha256()

        # パスワードをハッシュ化する
        hash_algorithm.update(password_bytes)

        # ハッシュ化されたパスワードを返す
        return hash_algorithm.hexdigest()