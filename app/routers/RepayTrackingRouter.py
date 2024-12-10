from fastapi import APIRouter

router = APIRouter()

@router.get("/repay_tracking")
def repay_track():
    print("hello repay tracker !")
    