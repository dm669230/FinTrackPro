from fastapi import FastAPI,APIRouter, Depends, HTTPException, Request
from functools import lru_cache
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.routers.LoginRouter import router as auth_router
from app.routers.AdminRouter import router as admin_router
from app.routers.LoanManageRouter import router as loan_manage_router
from app.routers.RepayTrackingRouter import router as repay_router
# from app.config.config import settings
from app.config.db import SessionLocal, get_db
from typing_extensions import Annotated
from .config import config

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
async def home():
    return {"message": "Hello world !"}

@lru_cache
def get_settings():
    return config.Settings()

print(get_settings())

@app.get("/info")
async def info(settings:Annotated[config.Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "admin_email": settings.admin_email,
        "items_per_user": settings.items_per_user
    }

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")  # Simple query to check DB connection
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}

app.include_router(auth_router, prefix="/auth", tags=["AuthenticationAPI's"])
app.include_router(admin_router, prefix="/admin_action", tags=["AdminAPI's"])
app.include_router(loan_manage_router, prefix="/loan_manage",tags=["LoanManageAPI's"])
app.include_router(repay_router, prefix="/repayment_track",tags=["RepaymentTrackAPI's"])


