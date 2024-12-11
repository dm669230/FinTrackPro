from fastapi import APIRouter, Depends,Body, Request
from app.config.db import get_db
from app.schemas import schema as auth_schema
from sqlalchemy.orm import Session
from app.contollers.LoginController import register_new_user

# db = get_db()

router = APIRouter()

@router.post("/login")
def login_fun(username:str, password:str):
    return {"message":"Login Success"}

@router.post("/registration")
def user_register(new_user_schema:auth_schema.NewUserRegister, db:Session=Depends(get_db)):
    response = register_new_user(new_user_schema,db)
    return response
