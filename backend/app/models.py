from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

# Customer Model
class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone_number = Column(String)
    address = Column(String)
    dob = Column(DateTime)
    pan_number = Column(String, unique=True)
    aadhar_number = Column(String, unique=True)
    gender = Column(String)
    password = Column(String)

    accounts = relationship("Account", back_populates="owner")
    loans = relationship("Loan", back_populates="borrower")

# Account Model
class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True)
    balance = Column(Float, default=0.0)
    account_type = Column(String)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    
    owner = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")

# Transaction Model
class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    transaction_type = Column(String)
    amount = Column(Float)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    account_id = Column(Integer, ForeignKey("accounts.id"))
    
    account = relationship("Account", back_populates="transactions")

# Loan Model
class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    loan_type = Column(String)
    amount = Column(Float)
    interest_rate = Column(Float)
    tenure = Column(Integer)  # Loan duration in months
    status = Column(String)  # Pending, Approved, Rejected
    customer_id = Column(Integer, ForeignKey("customers.id"))
    
    borrower = relationship("Customer", back_populates="loans")
