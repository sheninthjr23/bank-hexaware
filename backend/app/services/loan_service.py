from backend.app.models import Loan
from backend.app.schemas import LoanCreate
from backend.app.services import get_db

def apply_for_loan(loan: LoanCreate, db=Depends(get_db)):
    db_loan = Loan(**loan.dict())
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan
