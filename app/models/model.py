from sqlalchemy import Integer, Float, Column, String, PrimaryKeyConstraint, Text, TIMESTAMP, Boolean, func, ForeignKey, Date
from app.config.db import BASE
# from app.databases.query_mixin import QueryMixin


class UsersModel(BASE):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255))
    email = Column(String(255))
    phone_no = Column(String(255))
    username = Column(String(255))    
    password_hash = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())
    is_admin = Column(Boolean, default=False)
    salt = Column(String, nullable=False)

class LoansModel(BASE):
    __tablename__ = "loans"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey(UsersModel.id), index=True, primary_key=True)
    loan_amount = Column(Float, nullable=False, index = True)
    loan_status = Column(String(100),nullable=False, index= True,default="Pending")
    interest_rate = Column(Float, nullable=False, index= True)
    start_date = Column(Date, nullable= False, index = True)
    end_date = Column(Date, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())


class RepaymentsModel(BASE):
    __tablename__ = "repayments"
    id = Column(Integer, primary_key=True, index=True)
    loan_id = Column(Integer, ForeignKey(LoansModel.id), index=True)
    user_id = Column(Integer, ForeignKey(UsersModel.id), index=True)
    repayment_date = Column(Date, nullable= False, index = True)
    repayment_amount = Column(Float, nullable=False, index = True)
    remaining_amount = Column(Float, nullable=False, index = True)
    created_at = Column(TIMESTAMP, server_default=func.now())


class AdminActionsModel(BASE):
    __tablename__ = "admin_actions"
    id = Column(Integer, primary_key=True, index=True)
    admin_id = Column(Integer, ForeignKey(UsersModel.id), index=True)
    action_type = Column(String(100))
    target_user_id = Column(Integer, index=True)
    created_at = Column(TIMESTAMP, server_default=func.now())

