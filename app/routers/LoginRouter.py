from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
def login_fun(username:str, password:str):
    return {"message":"Login Success"}

@router.post("/registration")
def user_register():
    response = register_new_user()
    return response