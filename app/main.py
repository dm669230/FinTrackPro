from fastapi import FastAPI,APIRouter, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routers.LoginRouter import router as auth_router
from app.routers.AdminRouter import router as admin_router
from app.routers.LoanManageRouter import router as loan_manage_router
from app.routers.RepayTrackingRouter import router as repay_router

app = FastAPI()
origins = [
    "http://localhost"
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Hello world !"}

app.include_router(auth_router, prefix="/auth", tags=["AuthenticationAPI's"])
app.include_router(admin_router, prefix="/admin_action", tags=["AdminAPI's"])
app.include_router(loan_manage_router, prefix="/loan_manage",tags=["LoanManageAPI's"])
app.include_router(repay_router, prefix="/repayment_track",tags=["RepaymentTrackAPI's"])
