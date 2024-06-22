from back.sql.database import SessionLocal
from back.sql.models import userModels
from back.sql.schemas import userSchemas


class UserOperations:
    def __init__(self):
        self.session = SessionLocal()

    def createUser(self, user: userSchemas.UserCreate) -> userModels.User:
        user_created = userModels.User(**user.model_dump())
        self.session.add(user_created)
        self.session.commit()
        self.session.refresh(user_created)
        return user_created


# 测试用例
if __name__ == "__main__":
    user_operations = UserOperations()
    user_data = userSchemas.UserCreate(email="123@qq.com", password="<PASSWORD>")
    user_operations.createUser(user_data)
