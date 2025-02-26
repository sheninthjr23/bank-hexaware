from fastapi import APIRouter, HTTPException
from backend.app.services import auth_service

router = APIRouter()

@router.post("/login")
def login(email: str, password: str):
    auth_data = auth_service.authenticate_user(email, password)
    if not auth_data:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return auth_data

@router.post("/register")
def register(email: str, password: str):
    new_user = auth_service.register_user(email, password)
    return new_user
