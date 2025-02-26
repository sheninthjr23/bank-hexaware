from fastapi import APIRouter, HTTPException
from backend.app.services import transaction_service

router = APIRouter()

@router.post("/create")
def create_transaction(sender_id: int, receiver_id: int, amount: float):
    if sender_id == receiver_id:
        raise HTTPException(status_code=400, detail="Sender and receiver cannot be the same")
    transaction = transaction_service.create_transaction(sender_id, receiver_id, amount)
    return transaction

@router.get("/")
def get_transactions():
    transactions = transaction_service.get_transactions()
    return transactions
