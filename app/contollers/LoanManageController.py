# from app.config.db import  get_db
from sqlalchemy.orm import Session
import bcrypt
import base64, hashlib
from app.schemas import loan_manage_schema as LM_schema
from app.models import model as mdl
from fastapi import Depends
import traceback


def register_new_loan(new_loan_schema:LM_schema.NewLoanRegisterSchema, db):
    try:
        
        new_loan = mdl.LoansModel(user_id=new_loan_schema.user_id,
                            loan_amount=new_loan_schema.loan_amount, 
                            loan_status = new_loan_schema.loan_status,
                            interest_rate = new_loan_schema.interest_rate,
                            start_date = new_loan_schema.start_date,
                            end_date = new_loan_schema.end_date,
                            )
        
        db.add(new_loan)
        db.commit()

        return "Loan Added Sucessfully"
    except Exception as e:
        traceback.print_exc()
        print(f"Error occured due to : {e}")
        return f"Error occured due to : {e}"

    