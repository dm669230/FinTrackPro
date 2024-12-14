from fastapi import APIRouter, Depends,Body, Request
from app.config.db import get_db
from app.schemas import loan_manage_schema as loan_manage_schema
from sqlalchemy.orm import Session
from app.contollers.LoanManageController import register_new_loan

router = APIRouter()

@router.get("/loan_management")
def loan_management():
    print("hi loan management dashboard !")

@router.post("/loan_register")
def loan_register(new_loan_schema:loan_manage_schema.NewLoanRegisterSchema, db:Session=Depends(get_db)):
    response = register_new_loan(new_loan_schema,db)
    return response

