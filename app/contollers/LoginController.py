# from app.config.db import  get_db
from sqlalchemy.orm import Session
import bcrypt
import base64, hashlib
from app.schemas import schema as auth_schema
from app.models import model as mdl
from fastapi import Depends
import traceback


def register_new_user(new_user_schema:auth_schema.NewUserRegister, db):
    try:
        password=new_user_schema.password_hash.encode('utf-8')
        
        hash_pass = bcrypt.hashpw(base64.b64encode(hashlib.sha256(password).digest()),bcrypt.gensalt())
        print('hash_pass : ', hash_pass)
        db_user = mdl.Users(name=new_user_schema.name, 
                            email = new_user_schema.email,
                            phone_no = new_user_schema.phone_no,
                            username = new_user_schema.username,
                            password_hash = hash_pass)
        
        db.add(db_user)
        db.commit()

        return "User Added Sucessfully"
    except Exception as e:
        traceback.print_exc()
        print(f"Error occured due to : {e}")
        return f"Error occured due to : {e}"

    