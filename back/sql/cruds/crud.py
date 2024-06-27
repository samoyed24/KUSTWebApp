import datetime
from typing import Union

from pydantic import EmailStr
from sqlalchemy import desc
from back.config import Config as GlobalConfig
from back.sql.database import SessionLocal
from back.sql.models import userModels
from back.sql.schemas import userSchemas
from back.utils import utils


# 管理一些与用户相关的CRUD操作，如注册、登录、修改账户信息等
class UserOperations:
    def __init__(self):
        self.session = SessionLocal()

    def createUser(self, user: userSchemas.UserCreate) -> userModels.User:
        user_created = userModels.User(**user.model_dump())
        self.session.add(user_created)
        self.session.commit()
        self.session.refresh(user_created)
        return user_created


# 这里用来管理一些与注册邮箱相关的操作，发送验证码与验证邮箱验证码
class RegisterEmailOperations:
    def __init__(self, email: userSchemas.EmailVerificationBase) -> None:
        self.session = SessionLocal()
        self.email = email

    def send(
            self,
    ) -> str:
        random_code: str = utils.random_six_digits()
        addition_email = userModels.EmailVerification(
            email=self.email.email,
            code=random_code,
        )
        self.session.add(addition_email)
        self.session.commit()
        self.session.refresh(addition_email)
        return random_code

    def getLatestCode(self) -> Union[str, None]:
        query = self.session.query(userModels.EmailVerification).filter_by(email=self.email.email)
        latest_query = query.order_by(desc('created_time')).first()
        if latest_query:
            if (latest_query.created_time + GlobalConfig.EMAIL_VERIFICATION_EXPIRE_TIME) < datetime.datetime.now():
                return None
            return latest_query.code
        return None


# 测试用例
if __name__ == "__main__":
    # user_operations = UserOperations()
    # user_data = userSchemas.UserCreate(email="123@qq.com", password="<PASSWORD>")
    # user_operations.createUser(user_data)
    email_data = userSchemas.EmailVerificationBase(email="samoyed24@qq.com")
    email_op = RegisterEmailOperations(email_data)
    email_op.send()
    res = email_op.getLatestCode()
    print(res)
    email_data = userSchemas.EmailVerificationBase(email='tet')
    email_op2 = RegisterEmailOperations(email_data)
    res = email_op2.getLatestCode()
    print(res)
