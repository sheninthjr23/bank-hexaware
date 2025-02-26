from fastapi import APIRouter, Depends
from backend.app import schemas
from backend.app.services import loan_service

router = APIRouter()

@router.post("/apply", response_model=schemas.Loan)
def apply_for_loan(loan: schemas.LoanCreate):
    return loan_service.apply_for_loan(loan)

@router.get("/status/{loan_id}", response_model=schemas.Loan)
def get_loan_status(loan_id: int):
    return loan_service.get_loan_status(loan_id)
