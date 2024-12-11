from fastapi import APIRouter, Depends,Body, Request
from app.config.db import db_session, SessionLocal
from app.contollers.LoginController import register_new_user

# db = get_db()

router = APIRouter()

@router.post("/login")
def login_fun(username:str, password:str):
    return {"message":"Login Success"}

@router.post("/registration")
def user_register():
    response = register_new_user()
    return 'response'