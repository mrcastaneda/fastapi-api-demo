from enum import unique
from sqlalchemy import Column, String, Integer
from database import Base 

class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True, index = True)
    username = Column(String(50), unique=True)
    password = Column(String(300))
    fullname = Column(String(50), unique=True)

class Blog(Base):
    __tablename__ = 'blog'

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String(100))
    content = Column(String(200))