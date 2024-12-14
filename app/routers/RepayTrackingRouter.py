from fastapi import APIRouter, Depends,Body, Request
from app.config.db import get_db
from app.schemas import repayment_schema 
from sqlalchemy.orm import Session
from app.contollers.RepaymentController import add_new_repayment

router = APIRouter()

@router.get("/repay_tracking")
def repay_track():
    print("hello repay tracker !")


@router.post("/repayment_register")
def repayment_register(new_repayment_schema:repayment_schema.NewRepayRegisterSchema, db:Session=Depends(get_db)):
    response = add_new_repayment(new_repayment_schema,db)
    return response