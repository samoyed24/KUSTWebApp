from passlib.context import CryptContext
from typing import Union, Annotated
from pydantic import EmailStr

import back.config as globalConfig


class Register:
    def __init__(self, email: Union[EmailStr, None] = None) -> None:
        self.email: Union[EmailStr, None] = email


class Auth:
    def __init__(self, plain: Union[str, None] = None) -> None:
        self.pwd_context: CryptContext = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.hashed_pwd: Union[str, None] = None
        self.plain_pwd: Union[str, None] = plain

    def generate_hashed_pwd(self) -> None:
        self.hashed_pwd = self.pwd_context.hash(self.plain_pwd)


# 测试用例
if __name__ == '__main__':
    auth = Auth('123456')
    auth.generate_hashed_pwd()
    print(auth.hashed_pwd)
