from fastapi import APIRouter, HTTPException
from backend.app.services import account_service

router = APIRouter()

@router.post("/create")
def create_account(account_data: dict):
    new_account = account_service.create_account(account_data)
    return new_account

@router.get("/{account_id}")
def get_account(account_id: int):
    account = account_service.get_account(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account

@router.put("/{account_id}")
def update_account(account_id: int, account_data: dict):
    updated_account = account_service.update_account(account_id, account_data)
    if not updated_account:
        raise HTTPException(status_code=404, detail="Account not found")
    return updated_account

@router.delete("/{account_id}")
def delete_account(account_id: int):
    result = account_service.delete_account(account_id)
    return result
