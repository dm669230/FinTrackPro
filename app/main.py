from fastapi import FastAPI,APIRouter, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.routers.LoginRouter import router as auth_router
from app.routers.AdminRouter import router as admin_router
from app.routers.LoanManageRouter import router as loan_manage_router
from app.routers.RepayTrackingRouter import router as repay_router
from app.config.db import SessionLocal, get_db

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

# @app.middleware("http")
# async def db_session_middleware(request:Request, call_next):
#     #create a new session for the incoming request
#     session = SessionLocal()
#     token = db_session.set(session)
#     try:
#         # process the request and pass it to the next handler
#         response = await call_next(request)
#     finally:
#         db_session.reset(token)
#         session.close()
#     return response

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


