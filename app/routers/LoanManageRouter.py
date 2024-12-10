from fastapi import APIRouter

router = APIRouter()

@router.get("/loan_management")
def loan_management():
    print("hi loan management dashboard !")

