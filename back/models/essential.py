from pydantic import BaseModel, Field
from typing import List


class LoginModel(BaseModel):
    username: str = Field(example="111122223333", description="学号")
    password: str = Field(example="<PASSWORD>")


class GradeResponse(BaseModel):
    code: int = Field(example=20000, description="")
    message: str = Field(example="OK", description="")
    data: List[dict] = Field(example=[
        {
            "学期": "2022-2023-1",
            "课程名称": "体育(1)",
            "课程代码": "3200001",
            "课程类别1": "必修课",
            "课程类别2": "体育课",
            "教学班代码": "3200001.113",
            "成绩": "87",
            "学分": "0.0",
            "绩点": "3.7",
            "学分绩点": "0.0",
            "修读性质": "初修",
            "备注": "体育学院申请录入"
        }], description="")
