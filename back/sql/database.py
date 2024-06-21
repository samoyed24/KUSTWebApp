from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote_plus

# 用户名、密码、主机、端口、数据库
username = 'root'
password = '123456789qqq'
host = 'localhost'
port = 3307
database = 'KUST'

# 对密码进行 URL 编码
encoded_password = quote_plus(password)

# 创建连接字符串
SQLALCHEMY_DATABASE_URL = f'mysql://{username}:{encoded_password}@{host}:{port}/{database}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
