from app.config.db import db_session, SessionLocal
from app.schemas import schema as auth_schema
from app.models import models as mdl


def register_new_user(new_user_schema:auth_schema.NewUserRegister):
    try:
        # name = new_user_schema.name
        # email = new_user_schema.email
        # phone_no = new_user_schema.phone_no
        # username = new_user_schema.username
        # password_hash = new_user_schema.password_hash
        
        # new_user = db_session.query(mdl.Users)\
        #     .join(table_model2, table_model1.circle == table_model2.circle)\
        #     .filter(table_model1.month == latest_month)\
        #     .filter(
        #         (table_model1.batchid == latest_batchid_table1)
        #     ).all()
        db_user = mdl.Users(name=new_user_schema.name, 
                                                        email = new_user_schema.email,
                                                        phone_no = new_user_schema.phone_no,
                                                        username = new_user_schema.username,
                                                        password_hash = new_user_schema.password_hash)
        
        db_session.add(db_user)
        db_session.commit()

        return "User Added Sucessfully"
    except Exception as e:
        return f"Error occured due to : {e}"
    
    # new_user = db_session.insert(mdl.Users).values(name=new_user_schema.name, 
    #                                                 email = new_user_schema.email,
    #                                                 phone_no = new_user_schema.phone_no,
    #                                                 username = new_user_schema.username,
    #                                                 password_hash = new_user_schema.password_hash)

    