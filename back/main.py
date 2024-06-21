import sys, os
from fastapi import FastAPI

sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))  # 解决导入问题，后续可以相应修改
from back.models import *
from cores import coreQuery
from models import essential

app = FastAPI()


@app.get('/')
async def root():
    return {"message": "Hello World"}


@app.post('/query/grade/')
def query_grade(student: essential.LoginModel):
    try:
        s = coreQuery.Student(student.username, student.password)
    except ValueError as e:
        return {"code": 40000, "message": "Login Failed"}
    else:
        s.get_grade()
        return {"code": 20000, "message": "OK", 'data': s.result}
