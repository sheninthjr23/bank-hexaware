from pydantic import BaseModel
from typing import Optional
import datetime

# Customer Schema
class CustomerBase(BaseModel):
    name: str
    email: str
    phone_number: str
    address: str
    dob: datetime.date
    pan_number: str
    aadhar_number: str
    gender: str

class CustomerCreate(CustomerBase):
    password: str

class Customer(CustomerBase):
    id: int
    class Config:
        orm_mode = True

# Account Schema
class AccountBase(BaseModel):
    account_number: str
    account_type: str
    balance: float

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    customer_id: int

    class Config:
        orm_mode = True

# Transaction Schema
class TransactionBase(BaseModel):
    transaction_type: str
    amount: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: int
    account_id: int
    timestamp: datetime.datetime

    class Config:
        orm_mode = True

# Loan Schema
class LoanBase(BaseModel):
    loan_type: str
    amount: float
    interest_rate: float
    tenure: int

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    customer_id: int
    status: str

    class Config:
        orm_mode = True
