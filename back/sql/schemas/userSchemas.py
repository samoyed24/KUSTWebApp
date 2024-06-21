from typing import List
from pydantic import BaseModel


class GradeBase(BaseModel):
    term: str
    code: str
    type_1: str
    type_2: str
    class_code: str
    mark: int
    score: float
    point: float
    score_point: float
    prop: str
    note: str


class Grade(GradeBase):
    id: int

    class Config:
        from_attributes = True


class StudentBase(BaseModel):
    student_id: str


class StudentCreate(StudentBase):
    plt_pw: str


class Student(StudentBase):
    id: int
    grades: List[Grade]


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    create_time: str
    student: Student

    class Config:
        from_attributes = True
