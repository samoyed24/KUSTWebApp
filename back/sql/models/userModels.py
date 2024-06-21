from datetime import datetime

from back.sql.database import Base
from sqlalchemy import Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped


class User(Base):
    __tablename__ = 'User'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    create_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())

    student: Mapped['Student'] = relationship('Student', back_populates='user', uselist=False)


class Student(Base):
    __tablename__ = 'PlatformInfo'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[str] = mapped_column(String(255), unique=True)
    plt_pw: Mapped[str] = mapped_column(String(255))
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('User.id'), nullable=False)

    user: Mapped[User] = relationship('User', back_populates='student', uselist=False)
    grades: Mapped[list['Grade']] = relationship('Grade', back_populates='student')


class Grade(Base):
    __tablename__ = 'Grade'
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    term: Mapped[str] = mapped_column(String(255))
    code: Mapped[str] = mapped_column(String(255))
    type_1: Mapped[str] = mapped_column(String(255))
    type_2: Mapped[str] = mapped_column(String(255))
    class_code: Mapped[str] = mapped_column(String(255))
    mark: Mapped[int] = mapped_column(Integer)
    score: Mapped[float] = mapped_column(Float)
    point: Mapped[float] = mapped_column(Float)
    score_point: Mapped[float] = mapped_column(Float)
    prop: Mapped[str] = mapped_column(String(255))
    note: Mapped[str] = mapped_column(Text)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey(Student.id), nullable=False)

    student: Mapped[Student] = relationship('Student', back_populates='grades')
