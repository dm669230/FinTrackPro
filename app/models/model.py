from sqlalchemy import Integer, Float, Column, String, PrimaryKeyConstraint, Text, TIMESTAMP, Boolean, func
from app.config.db import BASE
# from app.databases.query_mixin import QueryMixin


class Users(BASE):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    phone_no = Column(String(255))
    username = Column(String(255))
    password_hash = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())
    is_admin = Column(Boolean, default=False)

