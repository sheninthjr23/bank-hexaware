from fastapi import FastAPI
from backend.app.api import auth, accounts, transactions

app = FastAPI()

# Include the API routers
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(accounts.router, prefix="/accounts", tags=["accounts"])
app.include_router(transactions.router, prefix="/transactions", tags=["transactions"])
