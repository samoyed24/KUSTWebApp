import sys, os
from fastapi import FastAPI, Body, Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # 解决导入问题，后续可以相应修改
from back.models import essential
from back.cores import coreQuery
from back.config import Config
from back import sql
from back.sql.models.userModels import *
from back.sql.database import engine

sql.database.Base.metadata.create_all(bind=engine)
app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl=Config.tokenURL)


@app.post('/query/grade/', response_model=essential.GradeResponse)
def query_grade(student: Annotated[essential.LoginModel, Body()]):
    try:
        s = coreQuery.Student(student.username, student.password)
    except ValueError as e:
        return {"code": 40000, "message": "Login Failed"}
    else:
        s.get_grade()
        return {"code": 20000, "message": "OK", 'data': s.result}


@app.post('/query/register/email-verification', response_model=essential.SuccessResponse)
def student_register_email(student: Annotated[essential.RegisterEmailVerificationModel, Body()]):
    pass
