# Simulated in-memory transaction data
mock_transactions = []

def create_transaction(sender_id: int, receiver_id: int, amount: float):
    # Simulate a money transfer between accounts
    transaction = {"sender_id": sender_id, "receiver_id": receiver_id, "amount": amount, "id": len(mock_transactions) + 1}
    mock_transactions.append(transaction)
    return transaction

def get_transactions():
    # Simulate fetching all transactions
    return mock_transactions
